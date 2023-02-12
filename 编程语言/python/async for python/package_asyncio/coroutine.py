"""
@date: 2021-05-04
@author: liberty
@file: coroutine

the is a part of "project-demo"

协程函数的作用：

result = yield from future
result = yield from coroutine
result = yield from task

return expression
raise exception

-----------------------------------------------------------------

获取时间循环对象的几种方式

loop = asyncio.get_running_loop()
loop = asyncio.set_event_loop(loop)
loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()

通过时间循环运行协程函数的方式:

asyncio.run
asyncio.run_until_complete

awaitable 对象: 可暂停等待的对象
    coroutines tasks futures
    coroutine可以自动封装成task，而Task是Future的子类。

"""

import asyncio
import time


async def say_after_time(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"开始时间为： {time.time()}")
    await say_after_time(1, "hello")
    await say_after_time(2, "world")
    print(f"结束时间为： {time.time()}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
