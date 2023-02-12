"""
The code created by Liberty on 2021/9/12

"""
from inspect import isgenerator

"""
def handler(request):
    # 业务逻辑代码

    # 需要执行一次API请求
    def call_back(result):
        # 使用API返回的result完成剩余工作
        print(result)
    # 注册回调，没有io_call这个方法，仅示意，表示注册一个io操作
    asyncio.get_event_loop().io_call(api, call_back)

---------------------------------------------------------------------
def handler(request):
    # 业务逻辑代码

    # 需要执行一次API请求，直接把IO请求信息yield出去
    result = yield io_info  # 关键是利用yield把执行权让出去
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

---------------------------------------------------------------------------------
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

1. 第一个生成器入栈
2. 调用send，如果得到生成器就入栈并进入下一轮迭代
3. 遇到到IO请求yield出来，让框架注册到ioloop
4. IO操作完成后被唤醒，缓存结果并出栈，进入下一轮迭代，目的让上层函数使用IO结果恢复运行
5. 如果一个生成器运行完毕，也需要和4一样让上层函数恢复运行


"""

"""

def example():
    value = yield 2
    print("get", value)
    return value


g = example()
# 使用send(None)启动生成器，我们应该会得到 2
got = g.send(None)
print(got)  # 2

try:
    # 再次启动 会显示 "get 4", 就是我们传入的值,
    # 但是这里已经没有yield了，所以生成器会报错，但是3.0版本的python在报错之后会 call return
    got = g.send(got * 2)
except StopIteration as e:
    # 生成器运行完成，将会print(4)，e.value 是生成器return的值
    print(e.value)
"""


def func1():
    ret = yield request("http://test.com/foo")
    ret = yield func2(ret)
    return ret


def func2(data):
    result = yield request("http://test.com/" + str(data))
    return result


def request(url):
    # 这里模拟返回一个io操作，包含io操作的所有信息，这里用URL简化
    result = yield "iojob of %s" % url
    return result


class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def peak(self):
        return self.arr[-1]

    def pop(self):
        tmp = self.arr[-1]
        self.arr = self.arr[:-1]
        return tmp

    def empty(self):
        return len(self.arr) == 0


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


w = wrapper(func1())
# 启动 wrpper, 将会得到 "iojob of http://test.com/foo"
w.send(None)
# 上个iojob foo 完成后的结果"bar"传入，继续运行，得到  "iojob of http://test.com/bar"
w.send("bar")
# 上个iojob bar 完成后的结构"barz"传入，继续运行，结束。
w.send("barz")
