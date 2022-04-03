"""
@date: 2021-05-03
@author: liberty
@file: demo1

the is a part of "project-demo"

https://blog.csdn.net/qq_27825451/article/details/85234610
https://zhuanlan.zhihu.com/p/52976277

generator中的主要方法 send next throw


"""


def my_generator(n):
    print('starting...')
    for i in range(n):
        temp = yield i
        print('i am {}'.format(temp))


g = my_generator(5)

# 只有使用 next 激活之后
# yield后面的代码并不是在第一次迭代的时候执行的，而是第二次迭代的时候才执行第一次yield后面没有执行的代码。
print(next(g))  # 输出0
print('1 ------------------')

print(next(g))  # 输出1
print('2 ------------------')

# g.send 返回值是 yield [value] 就是 value
print(g.send(100))  # 本来输出2，但是传入新的值100，改为输出100

print(next(g))  # 输出3

print(next(g))  # 输出4
