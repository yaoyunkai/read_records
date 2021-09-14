"""
The code created by Liberty on 2021/9/13

Lib/asyncio/events.py,
Lib/asyncio/base_events.py

事件循环是每个 asyncio 应用的核心。 事件循环会运行异步任务和回调，执行网络 IO 操作，以及运行子进程。

    asyncio.get_running_loop()
    返回当前 OS 线程中正在运行的事件循环。

    asyncio.get_event_loop()
    获取当前事件循环。

    asyncio.set_event_loop(loop)
    将 loop 设置为当前 OS 线程的当前事件循环。

    asyncio.new_event_loop()
    创建一个新的事件循环。


事件循环方法集

1. 运行和停止循环
    loop.run_until_complete(future)
    loop.run_forever()
    loop.stop()
    loop.is_running()
    loop.is_closed()
    loop.close()

2. 安排回调
    loop.call_soon(callback, *args, context=None)
    loop.call_soon_threadsafe(callback, *args, context=None)

3. 调度延迟回调：
    loop.call_later(delay, callback, *args, context=None)
    loop.call_at(when, callback, *args, context=None)
    loop.time() : 根据时间循环内部的单调时钟，返回当前时间为一个 float 值。

4. 创建Future和Task
    loop.create_future()
    创建一个附加到事件循环中的 asyncio.Future 对象。

    loop.create_task(coro, *, name=None)
    安排一个 协程 的执行。返回一个 Task 对象。


"""
