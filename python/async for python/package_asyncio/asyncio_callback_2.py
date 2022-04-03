"""
@date: 2021-05-04
@author: liberty
@file: asyncio_callback_2

the is a part of "project-demo"

"""

import asyncio


def callback(a, _loop):
    print("我的参数为 {0}，执行的时间为{1}".format(a, _loop.time()))


# call_later, call_at
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        now = loop.time()
        loop.call_later(5, callback, 5, loop)  # 第一个参数设置的时间5.5秒后执行，
        loop.call_at(now + 2, callback, 2, loop)  # 在指定的时间，运行，当前时间+2秒
        loop.call_at(now + 1, callback, 1, loop)
        loop.call_at(now + 3, callback, 3, loop)
        loop.call_soon(callback, 4, loop)
        loop.run_forever()  # 要用这个run_forever运行，因为没有传入协程，这个函数在3.7中已经被取消
    except KeyboardInterrupt:
        print("Goodbye!")
