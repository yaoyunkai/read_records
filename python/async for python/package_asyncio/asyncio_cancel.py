"""
@date: 2021-05-04
@author: liberty
@file: asyncio_cancel

the is a part of "project-demo"

"""

import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')
    try:
        await asyncio.sleep(3600)  # 模拟一个耗时任务
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    task = asyncio.create_task(cancel_me())
    await asyncio.sleep(1)
    print('main is sleep down')
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


if __name__ == '__main__':
    asyncio.run(main())
