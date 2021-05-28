"""
@date: 2021-05-03
@author: liberty
@file: yield_send

the is a part of "project-demo"

"""


def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'


g = my_generator()

print(next(g))

print(next(g))

print('xxxxxxxxxxxxxxxxxxxx')

print(g.throw(StopIteration))

# print(next(g))
