"""
@date: 2021-05-05
@author: liberty
@file: freezing_3

the is a part of "project-demo"

"""

import asyncio
import threading


async def func(num):
    print(f'准备调用func,大约耗时{num}')
    await asyncio.sleep(num)
    print(f'耗时{num}之后,func函数运行结束')


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def main():
    cor1 = func(3)
    cor2 = func(2)
    cor3 = func(1)

    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(new_loop,))
    t.start()

    asyncio.run_coroutine_threadsafe(cor1, new_loop)
    asyncio.run_coroutine_threadsafe(cor2, new_loop)
    asyncio.run_coroutine_threadsafe(cor3, new_loop)

    print('xxxxxxxxxxxxxx')


if __name__ == '__main__':
    main()
