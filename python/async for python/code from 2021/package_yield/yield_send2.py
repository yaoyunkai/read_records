"""
@date: 2021-05-04
@author: liberty
@file: yield_send2

the is a part of "project-demo"

"""


def my_generator():
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

# g.throw 会返回 StopIteration
print(g.throw(ValueError))
print('-------------------------')
print(next(g))
print(next(g))
print('-------------------------')
print(g.throw(TypeError))
print('-------------------------')
