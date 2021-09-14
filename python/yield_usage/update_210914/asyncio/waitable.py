"""
The code created by Liberty on 2021/9/13

可等待对象
可等待 对象有三种主要类型: 协程, 任务 和 Future.

    协程：
        协程函数: 定义形式为 async def 的函数;
        协程对象: 调用 协程函数 所返回的对象。 __call__

    任务：
        任务 被用来“并行的”调度协程
        当一个协程通过 asyncio.create_task() 等函数被封装为一个 任务，该协程会被自动调度执行:

    Future 对象：
        Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
        当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
        在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
        通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
        Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

        async def main():
            await function_that_returns_a_future_object()

            # this is also valid:
            await asyncio.gather(
                function_that_returns_a_future_object(),
                some_python_coroutine()
            )

运行 asyncio 程序：

    asyncio.run(coro, *, debug=False)

    asyncio.create_task(coro, *, name=None)
    将 coro 协程 封装为一个 Task 并调度其执行。返回 Task 对象。
    asyncio.ensure_future(coro())

并发运行任务：
    asyncio.gather(*aws, loop=None, return_exceptions=False)
    并发 运行 aws 序列中的 可等待对象。
    如果 aws 中的某个可等待对象为协程，它将自动被作为一个任务调度。
    如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。

屏蔽取消操作：
    asyncio.shield(aw, *, loop=None)
    保护一个 可等待对象 防止其被 取消。
    如果 aw 是一个协程，它将自动被作为任务调度。

超时：
    asyncio.wait_for(aw, timeout, *, loop=None)
    等待 aw 可等待对象 完成，指定 timeout 秒数后超时。
    如果 aw 是一个协程，它将自动被作为任务调度。

    asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
    并发地运行 aws 可迭代对象中的 可等待对象 并进入阻塞状态直到满足 return_when 所指定的条件。


在线程中运行：
    asyncio.to_thread(func, /, *args, **kwargs)
    在不同的线程中异步地运行函数 func。

    返回一个可被等待以获取 func 的最终结果的协程。
    这个协程函数主要是用于执行在其他情况下会阻塞事件循环的 IO 密集型函数/方法。

跨线程调度：
    asyncio.run_coroutine_threadsafe(coro, loop)
    向指定事件循环提交一个协程。（线程安全）

    返回一个 concurrent.futures.Future 以等待来自其他 OS 线程的结果。
    此函数应该从另一个 OS 线程中调用，而非事件循环运行所在线程。


内省：
    asyncio.current_task(loop=None)
    返回当前运行的 Task 实例，如果没有正在运行的任务则返回 None。

    asyncio.all_tasks(loop=None)
    返回事件循环所运行的未完成的 Task 对象的集合。


Task对象
    一个与 Future 类似 的对象，可运行 Python 协程。非线程安全。
    Task 对象被用来在事件循环中运行协程。如果一个协程在等待一个 Future 对象，
    Task 对象会挂起该协程的执行并等待该 Future 对象完成。当该 Future 对象 完成，被打包的协程将恢复执行。


"""

import asyncio


# async def nested():
#     return 42


# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()
#
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
#
#
# asyncio.run(main())


# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     await task


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
