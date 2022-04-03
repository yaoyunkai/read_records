def example():
    value = yield 2
    print("get", value)
    return value


g = example()
# 使用send(None)启动生成器，我们应该会得到 2
got = g.send(None)
print(got)  # 2

try:
    # 再次启动 会显示 "get 4", 就是我们传入的值
    got = g.send('ads')
except StopIteration as e:
    # 生成器运行完成，将会print(4)，e.value 是生成器return的值
    print(e.value)
