"""
@date: 2021-05-04
@author: liberty
@file: yield_close

the is a part of "project-demo"

生成器的启动与关闭

next(g) or g.send(None)

"""


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


# g = my_generator()
# print(next(g))
# print(next(g))
# g.close()
# print(next(g))  # 在此处会显示错误
# print(next(g))


def g2():
    """
    如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
    如果在return后返回一个值，那么这个值为StopIteration异常的说明，不是程序的返回值。

    """

    yield 'a'
    return 'error info'
    yield 'b'


g = g2()
print(next(g))  # 程序停留在执行完yield 'a'语句后的位置。
print(next(g))
