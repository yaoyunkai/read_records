"""
@date: 2021-05-04
@author: liberty
@file: yield_from_demo2

the is a part of "project-demo"

"""


def average():
    total = 0.0  # 数字的总和
    count = 0  # 数字的个数
    avg = None  # 平均值
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total / count


def wrap_average(generator):
    yield from generator


# 定义一个函数，通过这个函数向average函数发送数值
def main(wrap):
    print(next(wrap))  # 启动生成器
    print(wrap.send(10))  # 10
    print(wrap.send(20))  # 15
    print(wrap.send(30))  # 20
    print(wrap.send(40))  # 25


g = average()
wrap_g = wrap_average(g)
main(wrap_g)
