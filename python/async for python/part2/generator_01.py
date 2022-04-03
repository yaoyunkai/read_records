def gen_func():
    # 下面这行代码有两个作用：
    # 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
    # 在运行 html = "bobby" 和 gen.send(html) 之后，会打印 bobby，表明可以接收外面传进来的值
    html = yield "http://projectsedu.com"
    print(html)
    return "bobby"


if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非none值之前，我们必须启动一次生成器， 方式有两种1. gen.send(None), 2. next(gen)
    url = gen.send(None)
    # download url
    html = "bobby"
    print(gen.send(html))  # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    print(gen.send(html))
