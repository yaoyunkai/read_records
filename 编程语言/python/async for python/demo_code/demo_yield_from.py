"""
The code created by Liberty on 2021/9/14

"""


# def my_generator():
#     for i in range(5):
#         if i == 2:
#             return '我被迫中断了'
#         else:
#             yield i
#
#
# def main(generator):
#     try:
#         for i in generator:  # 不会显式触发异常，故而无法获取到return的值
#             print(i)
#     except StopIteration as exc:
#         print(exc.value)
#
#
# g = my_generator()  # 调用
# main(g)


# def my_generator():
#     for i in range(5):
#         if i == 2:
#             return '我被迫中断了'
#         else:
#             yield i
#
#
# def main(generator):
#     try:
#         print(next(generator))  # 每次迭代一个值，则会显式出发StopIteration
#         print(next(generator))
#         print(next(generator))
#         print(next(generator))
#         print(next(generator))
#     except StopIteration as exc:
#         print(exc.value)  # 获取返回的值
#
#
# g = my_generator()
# main(g)


# def my_generator():
#     for i in range(5):
#         if i == 2:
#             return '我被迫中断了'
#         else:
#             yield i
#
#
# def wrap_my_generator(generator):  # 定义一个包装“生成器”的生成器，它的本质还是生成器
#     result = yield from generator  # 自动触发StopIteration异常，并且将return的返回值赋值给yield from表达式的结果，即result
#     print(result)
#
#
# def main(generator):
#     for j in generator:
#         print(j)
#
#
# g = my_generator()
# wrap_g = wrap_my_generator(g)
# main(wrap_g)


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
def main(wrap_func):
    # 数据传输管道的作用
    print(next(wrap_func))  # 启动生成器
    print(wrap_func.send(10))  # 10
    print(wrap_func.send(20))  # 15
    print(wrap_func.send(30))  # 20
    print(wrap_func.send(40))  # 25


g = average()
wrap = wrap_average(g)
main(wrap)
