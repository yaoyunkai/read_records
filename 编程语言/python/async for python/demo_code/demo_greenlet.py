import time

from greenlet import greenlet


def task_1():
    while True:
        print("--This is task 1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)


def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)


if __name__ == "__main__":
    g1 = greenlet(task_1)  # 定义greenlet对象
    g2 = greenlet(task_2)

    g1.switch()  # 切换到g1中运行
