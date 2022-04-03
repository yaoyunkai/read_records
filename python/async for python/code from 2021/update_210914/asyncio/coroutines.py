"""
The code created by Liberty on 2021/9/13

协程 通过 async/await 语法进行声明，是编写 asyncio 应用的推荐方式。

要真正运行一个协程，asyncio 提供了三种主要机制:
    asyncio.run() 函数用来运行最高层级的入口点 "main()" 函数
    asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。

"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


#
# # <coroutine object main at 0x000002949CF63BC8>
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())


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


asyncio.run(main())
