# High Level API #

## 协程与任务 ##

### 协程 ###

协程 通过 async/await 语法进行声明，是编写 asyncio 应用的推荐方式

```
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world
```

简单地调用一个协程并不会使其被调度执行

```
>>> main()
<coroutine object main at 0x1053bb7c8>
```

要真正运行一个协程，asyncio 提供了三种主要机制:

- `asyncio.run()` 函数用来运行最高层级的入口点 "main()" 函数

- 等待一个协程 `await`

  ```python
  import asyncio
  import time
  
  async def say_after(delay, what):
      await asyncio.sleep(delay)
      print(what)
  
  async def main():
      print(f"started at {time.strftime('%X')}")
  
      await say_after(1, 'hello')
      await say_after(2, 'world')
  
      print(f"finished at {time.strftime('%X')}")
  
  asyncio.run(main())
  ```

- `asyncio.create_task()` 函数用来并发运行作为 asyncio 任务 的多个协程。

  ```python
  async def main():
      task1 = asyncio.create_task(
          say_after(1, 'hello'))
  
      task2 = asyncio.create_task(
          say_after(2, 'world'))
  
      print(f"started at {time.strftime('%X')}")
  
      # Wait until both tasks are completed (should take
      # around 2 seconds.)
      await task1
      await task2
  
      print(f"finished at {time.strftime('%X')}")
  ```

### 可等待对象 ###

如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。许多 asyncio API 都被设计为接受可等待对象。

可等待对象有三种主要类型: **协程**, **任务** 和 **Future**.

**协程**

Python 协程属于 可等待 对象，因此可以在其他协程中被等待:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

在本文档中 "协程" 可用来表示两个紧密关联的概念:

- 协程函数: 定义形式为 `async def` 的函数;
- 协程对象：调用协程函数所返回的对象。

**任务**

任务被用来“并行的”调度协程

当一个协程通过 `asyncio.create_task()` 等函数被封装为一个 任务，该协程会被自动调度执行:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```

**Futures**

Future 是一种特殊的低层级可等待对象，表示一个异步操作的 最终结果。

当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。

通常情况下 没有必要 在应用层级的代码中创建 Future 对象。

Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

### 运行asyncio程序 ###

`asyncio.run(coro, *, debug=False)`

执行 coroutine  并返回结果

此函数会运行传入的协程，负责管理 asyncio 事件循环，*终结异步生成器*，并关闭线程池。

当有其他 asyncio 事件循环在同一线程中运行时，此函数不能被调用。

此函数总是会创建一个新的事件循环并在结束时关闭之。它应当被用作 asyncio 程序的主入口点，理想情况下应当只被调用一次。

### 创建任务 ###

`asyncio.create_task(coro, *, name=None)`

将 coro 协程 封装为一个 Task 并调度其执行。返回 Task 对象。

该任务会在 `get_running_loop()` 返回的循环中执行，如果当前线程没有在运行的循环则会引发 `RuntimeError`。

```python
async def coro():
    ...

# In Python 3.7+
task = asyncio.create_task(coro())
...

# This works in all Python versions but is less readable
task = asyncio.ensure_future(coro())
...
```

### 休眠 ###

`coroutine asyncio.sleep(delay, result=None)`

如果指定了 *result*，则当协程完成时将其返回给调用者。

`sleep()` 总是会挂起当前任务，以允许其他任务运行。

将 delay 设为 0 将提供一个经优化的路径以允许其他任务运行。 这可供长期间运行的函数使用以避免在函数调用的全过程中阻塞事件循环。

```python
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
```

### 并发运行任务 ###

`awaitable asyncio.gather(*aws, return_exceptions=False)`

并发运行aws序列中的可等待对象

如果 *aws* 中的某个可等待对象为协程，它将自动被作为一个任务调度。

如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 *aws* 中可等待对象的顺序一致。

如果 `return_exceptions` 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。

如果 `return_exceptions` 为 True，异常会和成功的结果一样处理，并聚合至结果列表。

如果 `gather()` 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。

如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
```

### 屏蔽取消操作 ###

`awaitable asyncio.shield(aw)`

保护一个 可等待对象 防止其被 取消。

如果 aw 是一个协程，它将自动被作为任务调度。

以下语句:

```
res = await shield(something())
```

相当于:

```
res = await something()
```

不同之处 在于如果包含它的协程被取消，在 something() 中运行的任务不会被取消。从 something() 的角度看来，取消操作并没有发生。然而其调用者已被取消，因此 "await" 表达式仍然会引发 CancelledError。

### 超时 ###

`coroutine asyncio.wait_for(aw, timeout)`

等待 aw 可等待对象 完成，指定 timeout 秒数后超时。

如果 aw 是一个协程，它将自动被作为任务调度。

timeout 可以为 None，也可以为 float 或 int 型数值表示的等待秒数。如果 timeout 为 None，则等待直到完成。

如果发生超时，任务将取消并引发 asyncio.TimeoutError.

要避免任务 取消，可以加上 shield()。

此函数将等待直到 Future 确实被取消，所以总等待时间可能超过 timeout。 如果在取消期间发生了异常，异常将会被传播。

如果等待被取消，则 aw 指定的对象也会被取消。

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())
```

### 简单等待 ###

`coroutine asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)`

并发地运行 aws 可迭代对象中的 可等待对象 并进入阻塞状态直到满足 return_when 所指定的条件。

aws 可迭代对象必须不为空。

返回两个 Task/Future 集合: `(done, pending)`。

```
done, pending = await asyncio.wait(aws)
```

如指定 *timeout* (float 或 int 类型) 则它将被用于控制返回之前等待的最长秒数。

请注意此函数不会引发 `asyncio.TimeoutError`。当超时发生时，未完成的 Future 或 Task 将在指定秒数后被返回。

`return_when` 指定此函数应在何时返回。它必须为以下常数之一:

| 常量              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| `FIRST_COMPLETED` | 函数将在任意可等待对象结束或取消时返回。                     |
| `FIRST_EXCEPTION` | 函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 `ALL_COMPLETED`。 |
| `ALL_COMPLETED`   | 函数将在所有可等待对象结束或取消时返回。                     |

与 `wait_for()` 不同，wait() 在超时发生时不会取消可等待对象。

```python
# wait() 会自动以任务的形式调度协程，之后将以 (done, pending) 集合形式返回显式创建的任务对象。因此以下代码并不会有预期的行为:
async def foo():
    return 42

coro = foo()
done, pending = await asyncio.wait({coro})

if coro in done:
    # This branch will never be run!

# 以上代码段的修正方法如下:
async def foo():
    return 42

task = asyncio.create_task(foo())
done, pending = await asyncio.wait({task})

if task in done:
    # Everything will work as expected now.
```

### 在线程中运行 ###

`coroutine asyncio.to_thread(func, /, *args, **kwargs)`

在不同的线程中异步地运行函数 func。

向此函数提供的任何 *args 和 **kwargs 会被直接传给 func。 并且，当前 contextvars.Context 会被传播，允许在不同的线程中访问来自事件循环的上下文变量。

返回一个可被等待以获取 func 的最终结果的协程。

这个协程函数主要是用于执行在其他情况下会阻塞事件循环的 IO 密集型函数/方法。 例如:

```python
def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54
```

在任何协程中直接调用 blocking_io() 将会在调用期间阻塞事件循环，导致额外的 1 秒运行时间。 而通过改用 asyncio.to_thread()，我们可以在不同的线程中运行它从而不会阻塞事件循环。

### 跨线程调度 ###

`asyncio.run_coroutine_threadsafe(coro, loop)`

向指定事件循环提交一个协程。（线程安全）

返回一个 `concurrent.futures.Future` 以等待来自其他 OS 线程的结果。

此函数应该从另一个 OS 线程中调用，而非事件循环运行所在线程。

### 内省 ###

`asyncio.current_task(loop=None)`

返回当前运行的 Task 实例，如果没有正在运行的任务则返回 None。

`asyncio.all_tasks(loop=None)`

返回事件循环所运行的未完成的 Task 对象的集合。

### Task对象 ###

与 Future类似的对象，可以运行Python协程。非线程安全

Task 对象被用来在事件循环中运行协程。如果一个协程在等待一个 Future 对象，Task 对象会挂起该协程的执行并等待该 Future 对象完成。当该 Future 对象 完成，被打包的协程将恢复执行。

事件循环使用协同日程调度: 一个事件循环每次运行一个 Task 对象。而一个 Task 对象会等待一个 Future 对象完成，该事件循环会运行其他 Task、回调或执行 IO 操作。

使用高层级的 asyncio.create_task() 函数来创建 Task 对象，也可用低层级的 loop.create_task() 或 ensure_future() 函数。不建议手动实例化 Task 对象。

要取消一个正在运行的 Task 对象可使用 cancel() 方法。调用此方法将使该 Task 对象抛出一个 CancelledError 异常给打包的协程。如果取消期间一个协程正在等待一个 Future 对象，该 Future 对象也将被取消。

cancelled() 可被用来检测 Task 对象是否被取消。如果打包的协程没有抑制 CancelledError 异常并且确实被取消，该方法将返回 True。

asyncio.Task 从 Future 继承了其除 Future.set_result() 和 Future.set_exception() 以外的所有 API。

Task 对象支持 contextvars 模块。当一个 Task 对象被创建，它将复制当前上下文，然后在复制的上下文中运行其协程。

- `cancel(msg=None)`: 请求取消 Task 对象。
- `cancelled()`: 如果 Task 对象 被取消 则返回 True。
- `done()` 如果 Task 对象 已完成 则返回 True。
- `result()` 返回 Task 的结果。
- `exception()` 返回 Task 对象的异常。
- `add_done_callback(callback, *, context=None)` 添加一个回调，将在 Task 对象 完成 时被运行。
- `remove_done_callback(callback)`
- `get_stack(*,limit=None)` 返回此 Task 对象的栈框架列表。
- `print_stack(*,limit=None,file=None)` 
- `get_coro()` 
- `get_name()`
- `set_name(value)`

### 基于生成器的协程 ###

基于生成器的协程是 async/await 语法的前身。它们是使用 `yield from` 语句创建的 Python 生成器，可以等待 Future 和其他协程。

基于生成器的协程应该使用 @asyncio.coroutine 装饰，虽然这并非强制。

```python
@asyncio.coroutine
def old_style_coroutine():
    yield from asyncio.sleep(1)

async def main():
    await old_style_coroutine()
```

- `asyncio.iscoroutine(obj)` 如果 obj 是一个 协程对象 则返回 True。
- `asyncio.iscoroutinefunction(func)` 如果 func 是一个 协程函数 则返回 True。

## 流 ##

流是用于处理网络连接的支持 async/await 的高层级原语。 流允许发送和接收数据，而不需要使用回调或低级协议和传输。

**Stream 函数**

`coroutine asyncio.open_connection(host=None, port=None, *, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, happy_eyeballs_delay=None, interleave=None)`

建立网络连接并返回一对 (reader, writer) 对象。

返回的 reader 和 writer 对象是 StreamReader 和 StreamWriter 类的实例。

limit 确定返回的 StreamReader 实例使用的缓冲区大小限制。默认情况下，limit 设置为 64 KiB 。



`coroutine asyncio.start_server(client_connected_cb, host=None, port=None, *, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)`

启动套接字服务。

当一个新的客户端连接被建立时，回调函数 client_connected_cb 会被调用。该函数会接收到一对参数 (reader, writer) ，reader是类 StreamReader 的实例，而writer是类 StreamWriter 的实例。

client_connected_cb 即可以是普通的可调用对象也可以是一个 协程函数; 如果它是一个协程函数，它将自动作为 Task 被调度。

limit 确定返回的 StreamReader 实例使用的缓冲区大小限制。默认情况下，limit 设置为 64 KiB 。

### StreamReader ###

这个类表示一个读取器对象，该对象提供api以便于从IO流中读取数据。

不推荐直接实例化 StreamReader 对象，建议使用 `open_connection()` 和 `start_server()` 来获取 StreamReader 实例。

```
read(n=-1)
readline()
readexactly(n)
readutil(separator=b'\n')
at_eof()
```

### StreamWriter ###

这个类表示一个写入器对象，该对象提供api以便于写数据至IO流中。

不建议直接实例化 StreamWriter；而应改用 `open_connection()` 和 `start_server()`。

### Demo ###

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'))

import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

## 同步原语 ##

- asyncio 原语不是线程安全的，因此它们不应被用于 OS 线程同步 (而应当使用 threading)；
- 这些同步原语的方法不接受 timeout 参数；请使用 asyncio.wait_for() 函数来执行带有超时的操作。

### Lock ###

实现一个用于 asyncio 任务的互斥锁。 非线程安全。asyncio 锁可被用来保证对共享资源的独占访问。

```python
lock = asyncio.Lock()

# ... later
async with lock:
    # access shared state

    
lock = asyncio.Lock()

# ... later
await lock.acquire()
try:
    # access shared state
finally:
    lock.release()
```

### 事件 Event ###

事件对象。 该对象不是线程安全的。

asyncio 事件可被用来通知多个 asyncio 任务已经有事件发生。

Event 对象会管理一个内部旗标，可通过 `set()` 方法将其设为 true 并通过 `clear()` 方法将其重设为 false。 `wait()` 方法会阻塞直至该旗标被设为 true。 该旗标初始时会被设为 false。

```python
async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task

asyncio.run(main())
```

### Condition ###

## 子进程集 ##

### 创建子进程 ###

`coroutine asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`

创建一个子进程。

limit 参数为 Process.stdout 和 Process.stderr 设置 StreamReader 包装器的缓冲区上限（如果将 subprocess.PIPE 传给了 stdout 和 stderr 参数）。

返回一个 Process 实例。

`coroutine asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`

运行 cmd shell 命令。

limit 参数为 Process.stdout 和 Process.stderr 设置 StreamReader 包装器的缓冲区上限（如果将 subprocess.PIPE 传给了 stdout 和 stderr 参数）。

返回一个 Process 实例。

### 常量 ###

`asyncio.subprocess.PIPE`

可以被传递给 *stdin*, *stdout* 或 *stderr* 形参。

`asyncio.subprocess.STDOUT`

可以用作 *stderr* 参数的特殊值，表示标准错误应当被重定向到标准输出。

`asyncio.subprocess.DEVNULL`

可以用作 stdin, stdout 或 stderr 参数来处理创建函数的特殊值。 它表示将为相应的子进程流使用特殊文件 os.devnull。

### 与子进程交互 ###

`create_subprocess_exec()` 和 `create_subprocess_shell()` 函数都返回 Process 类的实例。 Process 是一个高层级包装器，它允许与子进程通信并监视其完成情况。

`class asyncio.subprocess.Process`

一个用于包装 create_subprocess_exec() and create_subprocess_shell() 函数创建的 OS 进程的对象。

这个类被设计为具有与 subprocess.Popen 类相似的 API，但两者有一些重要的差异:

- 不同于 Popen，Process 实例没有与 [`poll()`](https://docs.python.org/zh-cn/3.10/library/subprocess.html#subprocess.Popen.poll) 方法等价的方法；
- [`communicate()`](https://docs.python.org/zh-cn/3.10/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.communicate) 和 [`wait()`](https://docs.python.org/zh-cn/3.10/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.wait) 方法没有 *timeout* 形参；要使用 [`wait_for()`](https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#asyncio.wait_for) 函数；
- [`Process.wait()`](https://docs.python.org/zh-cn/3.10/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.wait) 方法是异步的，而 [`subprocess.Popen.wait()`](https://docs.python.org/zh-cn/3.10/library/subprocess.html#subprocess.Popen.wait) 方法则被实现为阻塞型忙循环；
- *universal_newlines* 形参不被支持。

#### 子进程和线程 ####

标准 asyncio 事件循环默认支持从不同线程中运行子进程。

在 Windows 上子进程（默认）只由 ProactorEventLoop 提供，SelectorEventLoop 没有子进程支持。

在 UNIX 上会使用 child watchers 来让子进程结束等待，详情请参阅 进程监视器。

在 3.8 版更改: UNIX 对于从不同线程中无限制地生成子进程会切换为使用 ThreadedChildWatcher。

使用 不活动的 当前子监视器生成子进程将引发 RuntimeError。

## 队列集 ##

asyncio 队列被设计成与 queue 模块类似。尽管 asyncio队列不是线程安全的，但是他们是被设计专用于 async/await 代码。

注意asyncio 的队列没有 timeout 形参；请使用 asyncio.wait_for() 函数为队列添加超时操作。

### Queue ###

先进，先出（FIFO）队列

如果 maxsize 小于等于零，则队列尺寸是无限的。如果是大于 0 的整数，则当队列达到 maxsize 时， await put() 将阻塞至某个元素被 get() 取出。

不像标准库中的并发型 queue ，队列的尺寸一直是已知的，可以通过调用 qsize() 方法返回。

### PriorityQueue ###

### LifoQueue ###

## 异常 ##

