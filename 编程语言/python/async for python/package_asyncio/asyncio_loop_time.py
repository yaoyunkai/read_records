"""
@date: 2021-05-04
@author: liberty
@file: asyncio_loop_time

the is a part of "project-demo"

"""

import asyncio


async def hello1(a, b):
    print('准备做加法运算')
    await asyncio.sleep(3)
    return a + b


loop = asyncio.get_event_loop()
t1 = loop.time()
print(t1)

loop.run_until_complete(hello1(3, 4))
t2 = loop.time()
print(t2)
print(t2 - t1)
