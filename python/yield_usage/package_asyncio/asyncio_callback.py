"""
@date: 2021-05-04
@author: liberty
@file: asyncio_callback

the is a part of "project-demo"

"""

import asyncio


def callback(n):
    print('我是回调函数，参数为： {0} '.format(n))


async def main(_loop):
    print('在异步函数中注册回调函数')
    _loop.call_later(2, callback, 1)
    _loop.call_later(1, callback, 2)
    _loop.call_soon(callback, 3)

    await asyncio.sleep(4)


loop = asyncio.get_event_loop()
print('进入事件循环')
loop.run_until_complete(main(loop))
print('关闭事件循环')
loop.close()
