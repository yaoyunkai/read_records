"""
@date: 2021-05-04
@author: liberty
@file: yield_send3

the is a part of "project-demo"

"""


def my_generator():
    while True:
        try:
            yield 'a'
            yield 'b'
            yield 'c'
            yield 'd'
            yield 'e'
        except ValueError:
            print('触发“ValueError"了')
        except TypeError:
            print('触发“TypeError"了')


g = my_generator()
print(next(g))
print(next(g))
print('-------------------------')
# 此时 异常被捕捉， 然后程序又走到 while true 遇到 第一个 yield 停下 并返回结果
print(g.throw(ValueError))
print('-------------------------')
print(next(g))
print(next(g))
print('-------------------------')
print(g.throw(TypeError))
print('-------------------------')
print(next(g))
