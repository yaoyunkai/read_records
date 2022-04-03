def consumer():
    print('--4、开始执行生成器代码--')
    resp = None
    while True:
        print('--5、yield，中断，保存上下文--')
        n = yield resp
        print('--8、获取上下文，继续往下执行--')
        if n == 'stop':
            return
        print("[Consumer]: consuming {} ..".format(n))
        resp = "OK"


def produce(c):
    print("--3、启动生成器，开始执行生成器consumer--")
    c.send(None)  # 3、启动生成器，开始执行生成器consumer
    print("--6、继续往下执行--")
    n = 0
    while n < 5:
        n += 1
        print("[Producer]: producing {} ..".format(n))
        print("--7、第{}次唤醒生成器，从yield位置继续往下执行！--".format(n + 1))
        r = c.send(n)  # 第二次唤醒生成器
        print("--9、从第8步往下--")
        print("[Producer]: consumer return {} ..".format(r))

    c.close()


if __name__ == '__main__':
    produce(consumer())
