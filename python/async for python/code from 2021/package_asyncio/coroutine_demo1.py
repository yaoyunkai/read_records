"""
@date: 2021-05-04
@author: liberty
@file: coroutine_demo1.py

the is a part of "project-demo"

"""

import asyncio


async def func1():
    print('let\'s func1 start now...')
    await asyncio.sleep(3600)
    print('finally func1 execute down...')


async def main():
    try:
        print('wait you 3 seconds.....')
        await asyncio.wait_for(func1(), timeout=3)
    except asyncio.TimeoutError:
        print('timeout .....')


asyncio.run(main())
