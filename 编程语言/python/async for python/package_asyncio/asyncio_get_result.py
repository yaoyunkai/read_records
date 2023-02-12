"""
@date: 2021-05-04
@author: liberty
@file: asyncio_get_result

the is a part of "project-demo"

"""

import asyncio


async def hello(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


def callback(f):
    print(f.result())


# coroutine = hello(10, 5)
# loop = asyncio.get_event_loop()  # 第一步：创建事件循环
# task = asyncio.ensure_future(coroutine)  # 第二步:将多个协程函数包装成任务列表
# loop.run_until_complete(task)  # 第三步：通过事件循环运行
# print('-------------------------------------')
# print(task.result())
# loop.close()


loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(hello(10, 5))  # 第二步:将多个协程函数包装成任务
task.add_done_callback(callback)  # 并被任务绑定一个回调函数

loop.run_until_complete(task)  # 第三步：通过事件循环运行
loop.close()
