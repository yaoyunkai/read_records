"""
@date: 2021-05-04
@author: liberty
@file: coroutines_demo2

the is a part of "project-demo"

"""

import asyncio
import time

a = time.time()


async def hello1():  # 大约2秒
    print("Hello world 01 begin")
    await asyncio.sleep(2)
    print("Hello again 01 end")


async def hello2():  # 大约3秒
    print("Hello world 02 begin")
    await asyncio.sleep(3)
    print("Hello again 02 end")


async def hello3():  # 大约4秒
    print("Hello world 03 begin")
    await asyncio.sleep(4)
    print("Hello again 03 end")


async def main():  # 入口函数
    done, pending = await asyncio.wait({hello1(), hello2(), hello3()}, return_when=asyncio.FIRST_COMPLETED)
    for i in done:
        print(i)
    for j in pending:
        print(j)


asyncio.run(main())  # 运行入口函数

b = time.time()
print('---------------------------------------')
print(b - a)
