"""
The code created by Liberty on 2021/9/13

Lib/asyncio/locks.py

    asyncio 原语不是线程安全的，因此它们不应被用于 OS 线程同步 (而应当使用 threading)；
    这些同步原语的方法不接受 timeout 参数；请使用 asyncio.wait_for() 函数来执行带有超时的操作。

Lock : 实现一个用于 asyncio 任务的互斥锁。 非线程安全。
Event
Condition
Semaphore
BoundedSemaphore


"""
