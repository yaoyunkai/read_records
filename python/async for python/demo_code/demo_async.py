"""
The code created by Liberty on 2021/9/12

"""

import asyncio


async def g():
    print('g 1')
    await asyncio.sleep(1)
    print('g 2')


async def f():
    print('xxxxxxxxxxxxxxxxxx')
    a = asyncio.create_task(g())
    print('-----------------------')
    await asyncio.sleep(1)
    print('f 1')
    await a
    print('f 2')


asyncio.run(f())
