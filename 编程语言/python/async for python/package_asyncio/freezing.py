"""
@date: 2021-05-05
@author: liberty
@file: freezing

the is a part of "project-demo"

"""

import asyncio


async def hello1(a, b):
    print(f"异步函数开始执行")
    await asyncio.sleep(3)
    print("异步函数执行结束")
    return a + b


async def main():
    c = await hello1(10, 20)
    print(c)
    print('main is running')


loop = asyncio.get_event_loop()
tasks = [main()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
