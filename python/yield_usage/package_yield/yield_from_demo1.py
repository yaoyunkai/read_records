"""
@date: 2021-05-04
@author: liberty
@file: yield_from_demo1

the is a part of "project-demo"

1. yield 无法获取生成器 return 的返回值

"""

"""
def generator1():
    yield 1
    yield 2
    yield 3


def generator2():
    yield 'a'
    yield 'b'
    yield 'c'
    yield from generator1()
    yield from [1, 2, 4, 5]
    yield from tuple([1, 3, 4])
    yield from range(5)


for i in generator2():
    print(i)
"""


"""

（1）上面的my_generator是原始的生成器，main是调用方，使用yield的时候，只涉及到这两个函数，
    即“调用方”与“生成器（协程函数）”是直接进行交互的，不涉及其他方法，即“调用方——>生成器函数(协程函数)”；

（2）在使用yield from的时候，多了一个对原始my_generator的包装函数，
    然后调用方是通过这个包装函数（后面会讲到它专有的名词）来与生成器进行交互的，即“调用方——>生成器包装函数——>生成器函数(协程函数)”；

（3）yield from iteration结构会在内部自动捕获 iteration生成器的StopIteration 异常。这种处理方式与 for 循环处理 StopIteration 异常的方式一样。
    而且对 yield from 结构来说，解释器不仅会捕获 StopIteration 异常，
    还会把return返回的值或者是StopIteration的value 属性的值变成 yield from 表达式的值，即上面的result。


"""


def my_generator():
    for i in [0, 1, 2, 3, 4]:
        if i == 2:
            return 'suspend'
        else:
            yield i


def wrapper_generator(gene):
    result = yield from gene
    print(result)


def main(gene):
    for j in gene:
        print(j)


if __name__ == '__main__':
    main(wrapper_generator(my_generator()))
