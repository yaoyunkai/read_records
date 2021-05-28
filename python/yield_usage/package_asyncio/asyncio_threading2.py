"""
@date: 2021-05-04
@author: liberty
@file: asyncio_threading2

the is a part of "project-demo"

"""

import asyncio
import threading
import time

a = time.time()


async def hello1():
    print(f"Hello world 01 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(3)
    print("Hello again 01 end")


async def hello2():
    print(f"Hello world 02 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(2)
    print("Hello again 02 end")


async def hello3():
    print(f"Hello world 03 begin,my thread is:{threading.currentThread()}")
    await hello2()
    await hello1()
    print("Hello again 03 end")


loop = asyncio.get_event_loop()
tasks = [hello3()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

b = time.time()
print('---------------------------------------')
print(b - a)
