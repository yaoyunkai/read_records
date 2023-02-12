# 理解Python协程的本质

## IO多路复用 ##

所有的网络服务程序都是一个巨大的死循环，你的业务逻辑都在这个循环的某个时刻被调用：

```python
def handler(request):
    # 处理请求
    pass

# 你的 handler 运行在 while 循环中
while True:
    # 获取一个新请求
    request = accept()
    # 根据路由映射获取到用户写的业务逻辑函数
    handler = get_handler(request)
    # 运行用户的handler，处理请求
    handler(request)
```

IO多路复用可以做到不使用线程解决问题，它是由操作系统内核提供的功能，可以说专门为这类场景而生。简单来讲，你的程序遇到网络IO时，告诉操作系统帮你盯着，同时操作系统提供给你一个方法，让你可以随时获取到有哪些io操作已经完成。就像这样：

```python
# 操作系统的IO复用示例伪代码
io_register(io_id, io_type)  # 向操作系统io注册自己关注的io操作的id和类型
io_register(io_id, io_type)
# 获取完成的io操作, 使用 epoll() in Linux and kqueue() in Unix
events = io_get_finished()

for (io_id, io_type) in events:
    if io_type == READ:
        data = read_data(io_id)
    elif io_type == WRITE:
        write_data(io_id，data)
```

把IO复用逻辑融合到我们的服务器中，大概会像这样：

```python
call_backs = {}

def handler(req):
    # do jobs here
    io_register(io_id, io_type)
    def call_back(result):
    # 使用返回的result完成剩余工作
    call_backs[io_id] = call_back

# 新的循环
while True：
    # 获取已经完成的io事件
    events = io_get_finished()
    for (io_id, io_type) in events:
        if io_type == READ: # 读取
            data = read(io_id)
            call_back = call_backs[io_id]
            call_back(data)
        else:
            # 其他类型io事件的处理
            pass

    # 获取一个新请求
    request = accept()
    # 根据路由映射获取到用户写的业务逻辑函数
    handler = get_handler(request)
    # 运行用户的handler，处理请求
    handler(request)
```

## 用生成器消除 callback ##

着重看下我们业务中经常写的handler函数，在有独立的ioloop后，它现在变成类似这样：

```python
def handler(request):
    # 业务逻辑代码

    # 需要执行一次API请求
    def call_back(result):
        # 使用API返回的result完成剩余工作
        print(result)
    # 注册回调，没有io_call这个方法，仅示意，表示注册一个io操作
    asyncio.get_event_loop().io_call(api, call_back)
```

如果我们把我们的`handler`用`yield`关键字转换成一个生成器，运行它来把**IO操作的具体内容**返回，IO完成后的回调函数中把IO结果放回并恢复生成器运行，那就解决了业务代码不流畅的问题了：

```python
def handler(request):
    # 业务逻辑代码

    # 需要执行一次API请求，直接把IO请求信息yield出去
    result = yield io_info
    # 使用API返回的result完成剩余工作
    print(result)

# 这个函数注册到ioloop中，用来当有新请求的时候回调
def on_request(request):
    # 根据路由映射获取到用户写的业务逻辑函数
    handler = get_handler(request)
    g = handler(request)
    # 首次启动获得io_info
    io_info = g.send(None)

    # io完成回调函数
    def call_back(result):
        g.send(result)  # 重新启动生成器

    asyncio.get_event_loop().io_call(io_info, call_back)
```

上面的例子，用户写的`handler`代码已经不会被打散到callback 中，`on_request`函数使用callback和`ioloop`交互，但它会被实现在web框架中，对用户不可见。上面代码足以给我们提供用生成器消灭的callback的启发，但局限性有两点：

1. 业务逻辑中仅发起一次网络IO，但实际中往往更多
1. 业务逻辑没有调用其他异步函数（协程），但实际中我们往往会调用其他协程

## 解决完整调用链 ##

我们来看一个更复杂的例子：

函数调用链路图。

其中`request` 执行真正的IO，`func1` `func2` 仅调用。显然我们的代码只能写成这样：

```python
def func1():
    ret = yield request("http://test.com/foo")
    ret = yield func2(ret)
    return ret

def func2(data):
    result = yield request("http://test.com/"+data)
    return result

def request(url):
    # 这里模拟返回一个io操作，包含io操作的所有信息，这里用URL简化
    result = yield "iojob of %s" % url
    return result
```

对于`request`，我们把IO操作通过yield暴露给框架。**对于`func1` 和 `func2`，调用`request`显然也要加`yield`关键字**，否则`request`调用返回一个生成器后不会暂停，继续执行后续逻辑显然会出错。

要运行整个调用栈，大概流程如下： 1. 调用`func1()`得到生成器 2. 调用`send(None)`启动它得到会得到`request("http://test.com/foo")`的结果，还是生成器对象 3. `send(None)`启动由`request()`产生的生成器，会得到IO操作，由框架注册到ioloop并指定回调 4. IO完成后的回调函数内唤醒`request`生成器，生成器会走到`return`语句结束 5. 捕获异常得到`request`生成器的返回值，将上一层`func1`唤醒，同时又得到`func2()`生成器 6. ... 继续执行。

借助栈，我们可以**把整个调用链上串联的所有生成器对表现为一个生成器**，对其不断send就能不断得到所有io操作信息并推动调用链前进，实现方法如下：

1. 第一个生成器入栈
1. 调用`send`，如果得到生成器就入栈并进入下一轮迭代
1. 遇到到IO请求`yield`出来，让框架注册到ioloop
1. IO操作完成后被唤醒，缓存结果并出栈，进入下一轮迭代，目的让上层函数使用IO结果恢复运行
1. 如果一个生成器运行完毕，也需要和4一样让上层函数恢复运行

```python
def wrapper(gen):
    # 第一层调用 入栈
    stack = Stack()
    stack.push(gen)

    # 开始逐层调用
    while True:
        # 获取栈顶元素
        item = stack.peak()

        result = None
        if isgenerator(item):  # 生成器，
            try:
                # 尝试获取下个生成器调用，并入栈
                # result 初始为None，之后迭代中将为下层调用的返回值
                child = item.send(result)
                result = None
                stack.push(child)
                # 入栈后直接进入下次循环，继续深入调用链
                continue
            except StopIteration as e:
                # 如果自己运行结束了，就暂存result，下一步让自己出栈
                result = e.value
        else:  # io 操作
            # 遇到了io操作，yield出去
            # IO完成后会被用IO结果唤醒并暂存到result
            result = yield item

        # 走到这里则本层已经执行完毕，出栈，下次迭代将回到调用链上一层
        stack.pop()
        # 没有上一层的话，那整个调用链都执行完成了，return
        if stack.empty():
            print("finished")
            return result
```

对于上面示例中的调用链，存在上面这种方法产生如下效果：

```python
w = wrapper(func1())
# 启动 wrpper, 将会得到 "iojob of http://test.com/foo"
w.send(None)
# 上个iojob foo 完成后的结果"bar"传入，继续运行，得到  "iojob of http://test.com/bar"
w.send("bar")
# 上个iojob bar 完成后的结构"barz"传入，继续运行，结束。
w.send("barz")
```

```python
# 维护一个就绪列表，存放所有完成的IO事件，格式为（wrapper，result）
ready = []

def on_request(request):
    handler = get_handler(request)
    # 使用 wrapper 包装后，可以只通过send处理IO了
    g = wrapper(func1())
    # 把开始状态直接视为结果为None的就绪状态
    ready.append((g, None))

# 让ioloop每轮循环都执行此函数，用来处理的就绪的IO，
def process_ready(self):
    def call_back(g, result):
        ready.append((g, result))

    # 遍历所有已经就绪生成器，将其向下推进
    for g, result in self.ready:
        # 用result唤醒生成器，并得到下一个io操作
        io_job = g.send(result)
        # 注册io操作
        asyncio.get_event_loop().io_call(
            io_job,
            # 完成后把生成器加入就绪列表，等待下一轮处理
            lambda result: ready.append((g, result))
        )
```

这里核心思想是维护一个就绪列表，ioloop每轮迭代都来扫一遍，推动就绪的状态的生成器向下运行，并把新的到到IO操作注册，IO完成后再次加入就绪，经过几轮ioloop的迭代一个`handler`最终会被执行完成。

## 提高扩展性 ##

我们的协程框架有一个限制，我们只能把IO操作异步化，虽然在网络编程和web编程的世界里，阻塞的基本只有IO操作，但也有一些例外，比如我想让当前操作`sleep`几秒，用`time.sleep()`又会让整个线程阻塞住，就需要特殊实现。再比如，可以把一些cpu密集的操作通过多线程异步化，让另一个线程通知事件已经完成后再执行后续。

所以，协程最好能与网络解耦开，让等待网络IO只是其中一种场景，提高扩展性。Python官方的解决方案是让用户自己处理阻塞代码，至于是向ioloop来注册IO事件还是开一个线程完全由你自己，并提供了一个标准「占位符」`Future`，表示他的结果等到未来才会有，其部分原型如下:

```python
class Future：
    # 设置结果
    def set_result(result): pass
    # 获取结果
    def result():  pass
    # 表示这个future对象是fou已被设置过结果
    def done(): pass
    # 设置在他被设置结果时应该执行的回调函数，可以设置多个
    def add_done_callback(callback):  pass
```

我们的稍加改动就能支持future，让扩展性变得更强。对于用户代码的中的网络请求函数`request`：

```python
# 现在 request 函数，不是生成器，它返回future
def request(url):
    # future 理解为占位符
    fut = Future()

    def callback(result):
        # 当网络IO完成回调的时候给占位符赋值
        fut.set_result(result)
    # 注册回调
    asyncio.get_event_loop().io_call(url, callback)

    # 返回占位符
    return future
```

现在，`request`不再是一个生成器，而是直接返回future。而对于位于框架中处理就绪列表的函数：

```python
def process_ready(self):
    def callback(fut):
        # future被设置结果会被放入就绪列表
        ready.append((g, fut.result()))

    # 遍历所有已经就绪生成器，将其向下推进
    for g, result in self.ready:
        # 用result唤醒生成器，得到的不再是io操作，而是future
        fut = g.send(result)
        # future被设置结果的时候会调用callback
        fut.add_done_callback(callback)
```