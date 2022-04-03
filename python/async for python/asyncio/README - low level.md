# Asyncio Low Level #

## 事件循环 ##

事件循环是每个 asyncio 应用的核心。 事件循环会运行异步任务和回调，执行网络 IO 操作，以及运行子进程。

应用开发者通常应当使用高层级的 asyncio 函数，例如 asyncio.run()，应当很少有必要引用循环对象或调用其方法。 本节所针对的主要是低层级代码、库和框架的编写者，他们需要更细致地控制事件循环行为。

**获取事件循环**

以下低层级函数可被用于获取、设置或创建事件循环:

`asyncio.get_running_loop()`

返回当前 OS 线程中正在运行的事件循环。

如果没有正在运行的事件循环则会引发 RuntimeError。 此函数只能由协程或回调来调用。

`asyncio.get_event_loop()`

获取当前事件循环。

如果当前 OS 线程没有设置当前事件循环，该 OS 线程为主线程，并且 set_event_loop() 还没有被调用，则 asyncio 将创建一个新的事件循环并将其设为当前事件循环。

由于此函数具有相当复杂的行为（特别是在使用了自定义事件循环策略的时候），更推荐在协程和回调中使用 get_running_loop() 函数而非 get_event_loop()。

`asyncio.set_event_loop(loop)`

将 *loop* 设置为当前 OS 线程的当前事件循环。

`asyncio.new_event_loop()`

Create and return a new event loop object.

### 事件循环方法集 ###

事件循环有下列 **低级** APIs：

#### 运行和停止循环 ####

- `loop.run_until_complete(future)`

  运行直到 future ( Future 的实例 ) 被完成。

  如果参数是 coroutine object ，将被隐式调度为 asyncio.Task 来运行。

  返回 Future 的结果 或者引发相关异常。

- `loop.run_forever()`

  运行事件循环直到 stop() 被调用。

  如果 stop() 在调用 run_forever() 之前被调用，循环将轮询一次 I/O 选择器并设置超时为零，再运行所有已加入计划任务的回调来响应 I/O 事件（以及已加入计划任务的事件），然后退出。

  如果 stop() 在 run_forever() 运行期间被调用，循环将运行当前批次的回调然后退出。 请注意在此情况下由回调加入计划任务的新回调将不会运行；它们将会在下次 run_forever() 或 run_until_complete() 被调用时运行。

- `loop.stop()`

- `loop.is_running()`

- `loop.is_closed()`

- `loop.close()`

  关闭事件循环。

  当这个函数被调用的时候，循环必须处于非运行状态。pending状态的回调将被丢弃。

  此方法清除所有的队列并立即关闭执行器，不会等待执行器完成。

  这个方法是幂等的和不可逆的。事件循环关闭后，不应调用其他方法。

- `coroutine loop.shutdown_asyncgens()`

- `coroutine loop.shutdown_default_executor()`

#### 安排回调 ####

- `loop.call_soon(callback, *args, context=None)`

  安排 callback callback 在事件循环的下一次迭代时附带 args 参数被调用。

  回调按其注册顺序被调用。每个回调仅被调用一次。

  可选键值类的参数 context 允许 callback 运行在一个指定的自定义 contextvars.Context 对象中。如果没有提供 context ，则使用当前上下文。

- `loop.call_soon_threadsafe(callback, *args, context=None)`

#### 调度延迟回调 ####

事件循环提供安排调度函数在将来某个时刻调用的机制。事件循环使用单调时钟来跟踪时间。

- `loop.call_later(delay, callback, *args, context=None)`

  安排 callback 在给定的 delay 秒（可以是 int 或者 float）后被调用。

  返回一个 asyncio.TimerHandle 实例，该实例能用于取消回调。

  callback 只被调用一次。如果两个回调被安排在同样的时间点，执行顺序未限定。

- `loop.call_at(when, callback, *args, context=None)`

  安排 callback 在给定的绝对时间戳 when (int 或 float) 被调用，使用与 loop.time() 同样的时间参考。

  本方法的行为和 call_later() 方法相同。

  返回一个 asyncio.TimerHandle 实例，该实例能用于取消回调。

- `loop.time()`

  根据时间循环内部的单调时钟，返回当前时间为一个 float 值。

#### 创建Future和Task ####

- loop.create_future

  创建一个附加到事件循环中的 asyncio.Future 对象。

  这是在asyncio中创建Futures的首选方式。这让第三方事件循环可以提供Future 对象的替代实现(更好的性能或者功能)。

- loop.create_task

  安排一个 协程 的执行。返回一个 Task 对象。

  第三方的事件循环可以使用它们自己的 Task 子类来满足互操作性。这种情况下结果类型是一个 Task 的子类。

  如果提供了 name 参数且不为 None，它会使用 Task.set_name() 来设为任务的名称。

- loop.set_task_factory

  设置一个任务工厂，它将由 loop.create_task() 来使用。

- loop.get_task_factory

#### 打开网络连接 ####

`coroutine loop.create_connection(protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, happy_eyeballs_delay=None, interleave=None)`

打开一个流式传输连接，连接到由 host 和 port 指定的地址。

套接字族可以是 AF_INET 或 AF_INET6，具体取决于 host (或 family 参数，如果有提供的话)。

套接字类型将为 SOCK_STREAM。

protocol_factory 必须为一个返回 asyncio 协议 实现的可调用对象。

这个方法会尝试在后台创建连接。当创建成功，返回 (transport, protocol) 组合。

底层操作的大致的执行顺序是这样的：

- 创建连接并为其创建一个 传输。
- 不带参数地调用 protocol_factory 并预期返回一个 协议 实例。
- 协议实例通过调用其 connection_made() 方法与传输进行配对。
- 成功时返回一个 (transport, protocol) 元组。

创建的传输是一个具体实现相关的双向流。

#### 创建网络服务 ####

`coroutine loop.create_server(protocol_factory, host=None, port=None, *, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)`

创建TCP服务 (socket 类型 SOCK_STREAM ) 监听 host 地址的 port 端口。

返回一个 Server 对象。

#### 传输文件 ####

`coroutine loop.sendfile(transport, file, offset=0, count=None, *, fallback=True)`

将 *file* 通过 *transport* 发送。 返回所发送的字节总数。

#### 监控文件描述符 ####

- `loop.add_reader(fd, callback, *args)`

  开始监视 *fd* 文件描述符以获取读取的可用性，一旦 *fd* 可用于读取，使用指定的参数调用 *callback* 。

- `loop.remove_reader(fd)`

  停止对文件描述符 *fd* 读取可用性的监视。

- `loop.add_writer(fd, callback, *args)`

  开始监视 *fd* 文件描述符的写入可用性，一旦 *fd* 可用于写入，使用指定的参数调用 *callback* 。

- `loop.remove_writer(fd)`

  停止对文件描述符 *fd* 的写入可用性监视。

#### 直接使用socket对象 ####

通常，使用基于传输的 API 的协议实现，例如 loop.create_connection() 和 loop.create_server() 比直接使用套接字的实现更快。 但是，在某些应用场景下性能并不非常重要，直接使用 socket 对象会更方便。

#### 在线程或者进程池中执行代码 ####

`awaitable loop.run_in_executor(executor, func, *args)`

安排在指定的执行器中调用 *func* 。

```python
import asyncio
import concurrent.futures

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)
        print('custom process pool', result)

asyncio.run(main())
```

#### 错误处理API ####

允许自定义事件循环中如何去处理异常。

`loop.set_exception_handler(handler)`

`loop.get_exception_handler()`

`loop.default_exception_handler(context)`

`loop.call_exception_handler(context)`

#### 运行子进程 ####

本小节所描述的方法都是低层级的。 在常规 async/await 代码中请考虑改用高层级的 `asyncio.create_subprocess_shell()` 和 `asyncio.create_subprocess_exec()` 便捷函数。

`coroutine loop.subprocess_exec(protocol_factory, *args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)`

用 args 指定的一个或者多个字符串型参数创建一个子进程。

args 必须是个由下列形式的字符串组成的列表：str;或者由 文件系统编码格式 编码的 bytes。

第一个字符串指定可执行程序，其余的字符串指定其参数。 所有字符串参数共同组成了程序的 argv。

此方法类似于调用标准库 subprocess.Popen 类，设置 shell=False 并将字符串列表作为第一个参数传入；但是，Popen 只接受一个单独的字符串列表参数，而 subprocess_exec 接受多个字符串参数。

protocol_factory 必须为一个返回 asyncio.SubprocessProtocol 类的子类的可调用对象。

`coroutine loop.subprocess_shell(protocol_factory, cmd, *, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)`

基于 cmd 创建一个子进程，该参数可以是一个 str 或者按 文件系统编码格式 编码得到的 bytes ，使用平台的 "shell" 语法。

这类似与用 shell=True 调用标准库的 subprocess.Popen 类。

protocol_factory 必须为一个返回 SubprocessProtocol 类的子类的可调用对象。

### 回调处理 ###

`class asyncio.Handle`

由 `loop.call_soon()`, `loop.call_soon_threadsafe()` 所返回的回调包装器对象。

- `cancel()` 取消回调。 如果此回调已被取消或已被执行，此方法将没有任何效果。
- `cancelled()` 如果此回调已被取消则返回 True。

`class asyncio.TimerHandle`

由 `loop.call_later()` 和 `loop.call_at()` 所返回的回调包装器对象。这个类是 Handle 的子类。

- `when()`  返回加入计划任务的回调时间，以 float 值表示的秒数。时间值是一个绝对时间戳，使用与 loop.time() 相同的时间引用。

### Server对象 ###

Server 对象可使用 `loop.create_server()`, `loop.create_unix_server()`, `start_server()` 和 `start_unix_server()` 等函数来创建。

### 事件循环实现 ###

asyncio 带有两种不同的事件循环实现: `SelectorEventLoop` 和 `ProactorEventLoop`。

默认情况下 asyncio 被配置为在 Unix 上使用 SelectorEventLoop 而在 Windows 上使用 ProactorEventLoop。

## Futures ##

Future 对象用来链接 底层回调式代码 和高层异步/等待式代码。

### Future函数 ###

`asyncio.isfuture(obj)`

如果 obj 为下面任意对象，返回 True：

- 一个 asyncio.Future 类的实例，
- 一个 asyncio.Task 类的实例，
- 带有 _asyncio_future_blocking 属性的类似 Future 的对象。

`asyncio.ensure_future(obj, *, loop=None)`

返回值：

- obj 参数会是保持原样，如果 obj 是 Future、 Task 或 类似 Future 的对象( isfuture() 用于测试。)
- 封装了 obj 的 Task 对象，如果 obj 是一个协程 (使用 iscoroutine() 进行检测)；在此情况下该协程将通过 ensure_future() 加入执行计划。
- 等待 obj 的 Task 对象，如果 obj 是一个可等待对象( inspect.isawaitable() 用于测试)

`asyncio.wrap_future(future, *, loop=None)`

将一个 concurrent.futures.Future 对象封装到 asyncio.Future 对象中。

### Future对象 ###

`class asyncio.Future(*, loop=None)`

一个 Future 代表一个异步运算的最终结果。线程不安全。

Future 是一个 awaitable 对象。协程可以等待 Future 对象直到它们有结果或异常集合或被取消。

通常 Future 用于支持底层回调式代码(例如在协议实现中使用asyncio transports) 与高层异步/等待式代码交互。

经验告诉我们永远不要面向用户的接口暴露 Future 对象，同时建议使用 loop.create_future() 来创建 Future 对象。这种方法可以让 Future 对象使用其它的事件循环实现，它可以注入自己的优化实现。

- `result()`

  返回 Future 的结果。

  如果 Future 状态为 完成 ，并由 set_result() 方法设置一个结果，则返回这个结果。

  如果 Future 状态为 完成 ，并由 set_exception() 方法设置一个异常，那么这个方法会引发异常。

  如果 Future 已 取消，方法会引发一个 CancelledError 异常。

  如果 Future 的结果还不可用，此方法会引发一个 InvalidStateError 异常。

- `set_result(result)`

  将 Future 标记为 完成 并设置结果。

  如果 Future 已经 完成 则抛出一个 InvalidStateError 错误。

- `set_exception(exception)`

  将 Future 标记为 完成 并设置一个异常。

  如果 Future 已经 完成 则抛出一个 InvalidStateError 错误。

- `done()`

  如果 Future 为已 完成 则返回 True 。

  如果 Future 为 取消 或调用 set_result() 设置了结果或调用 set_exception() 设置了异常，那么它就是 完成 。

- `cancelled()`

  如果 Future 已 取消 则返回 True

  这个方法通常在设置结果或异常前用来检查 Future 是否已 取消 。

- `add_done_callback(callback, *, context=None)`

  添加一个在 Future 完成 时运行的回调函数。

  调用 callback 时，Future 对象是它的唯一参数。

  如果调用这个方法时 Future 已经 完成，回调函数会被 loop.call_soon() 调度。

  可选键值类的参数 context 允许 callback 运行在一个指定的自定义 contextvars.Context 对象中。如果没有提供 context ，则使用当前上下文。

- `remove_done_callback(callback)`

  从回调列表中移除 callback 。

  返回被移除的回调函数的数量，通常为1，除非一个回调函数被添加多次。

- `cancel(msg=None)`

  取消 Future 并调度回调函数。

  如果 Future 已经 完成 或 取消 ，返回 False 。否则将 Future 状态改为 取消 并在调度回调函数后返回 True 

- `exception()`

  返回 Future 已设置的异常。

  只有 Future 在 完成 时才返回异常（或者 None ，如果没有设置异常）。

  如果 Future 已 取消，方法会引发一个 CancelledError 异常。

  如果 Future 还没 完成 ，这个方法会引发一个 InvalidStateError 异常。

- `get_loop()`

  返回 Future 对象已绑定的事件循环。

```python
async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)

asyncio.run(main())
```

## 传输和协议 ##

传输和协议会被像 loop.create_connection() 这类 底层 事件循环接口使用。它们使用基于回调的编程风格支持网络或IPC协议（如HTTP）的高性能实现。

基本上，传输和协议应只在库和框架上使用，而不应该在高层的异步应用中使用它们。

在最顶层，传输只关心 怎样 传送字节内容，而协议决定传送 哪些 字节内容(还要在一定程度上考虑何时)。

也可以这样说：从传输的角度来看，传输是套接字(或类似的I/O终端)的抽象，而协议是应用程序的抽象。

换另一种说法，传输和协议一起定义网络I/0和进程间I/O的抽象接口。

传输对象和协议对象总是一对一关系：协议调用传输方法来发送数据，而传输在接收到数据时调用协议方法传递数据。

### 传输 ###

传输属于 asyncio 模块中的类，用来抽象各种通信通道。

传输对象总是由 异步IO事件循环 实例化。

异步IO实现TCP、UDP、SSL和子进程管道的传输。传输上可用的方法由传输的类型决定。

![image-20220403150616233](D:\Projects\Python\simple\demos\asynchronous\asyncio\.assets\image-20220403150616233.png)

### 协议 ###

asyncio 提供了一组抽象基类，它们应当被用于实现网络协议。 这些类被设计为与 传输 配合使用。

抽象基础协议类的子类可以实现其中的部分或全部方法。 所有这些方法都是回调：它们由传输或特定事件调用，例如当数据被接收的时候。 基础协议方法应当由相应的传输来调用。

![image-20220403150654238](D:\Projects\Python\simple\demos\asynchronous\asyncio\.assets\image-20220403150654238.png)

## 策略 ##

事件循环策略是各个进程的全局对象 ，它控制事件循环的管理。每个事件循环都有一个默认策略，可以使用策略API更改和定制该策略。

策略定义了“上下文”的概念，每个上下文管理一个单独的事件循环。默认策略将 context 定义为当前线程。

通过使用自定义事件循环策略，可以自定义 get_event_loop() 、 set_event_loop() 和 new_event_loop() 函数的行为。

策略对象应该实现 AbstractEventLoopPolicy 抽象基类中定义的API。

### 获取和设置策略 ###

- `asyncio.get_event_loop_policy()` 返回当前进程域的策略。
- `asyncio.set_event_loop_policy(policy)`  将 policy 设置为当前进程域策略。如果 policy 设为 None 将恢复默认策略。

### 策略对象 ###

![image-20220403150945101](D:\Projects\Python\simple\demos\asynchronous\asyncio\.assets\image-20220403150945101.png)

