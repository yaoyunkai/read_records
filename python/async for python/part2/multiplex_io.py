# 通过多路复用 IO 实现http请求
# 实现方式：select + 回调 + 事件循环
# 好处是：并发性高
# 使用单线程

import socket
# 通常不实用  import select，而是使用 from selectors
# selectors 进行了封装。DefaultSelector 封装的更好用，调用 select 方法的时候，会根据平台选择使用 epoll 还是 select。避免了 epoll 在 Windows 下不能使用的情况。
# 在 Linux 下使用 epoll，在 Windows 下使用 select 方法
from selectors import DefaultSelector
from selectors import EVENT_READ
from selectors import EVENT_WRITE
from urllib.parse import urlparse

selector = DefaultSelector()
# 使用select完成http请求
urls = []
stop = False


class Fetcher:
    def connected(self, key):
        # 在 send 之前，需要取消注册。
        # key.kd 就是 self.client.fileno() 的返回值
        selector.unregister(key.fd)
        # 在这里不需要再 try/catch，因为 connected 函数在调用的时候就已经表示时间就绪了
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
            self.path, self.host).encode("utf8"))
        # 已经发送了数据，等到响应返回，故应该是读事件
        # 这里是 self.readable，不是 self.readable()
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # 这里读数据没有放在 While True 中
        # readable 函数在每次可读的时候，会被自动调用，不再需要自己不停的读
        # 将读完的数据放到一个外部的变量中 self.data
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        # 这里将 client 设置为 self，因为回调函数会用到
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册
        # 第一个参数：文件描述符；第二个参数：事件；第三个：回调函数，即当事件可写的时候，执行什么函数逻辑
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


# loop 函数是实现的核心
# 回调是需要自己来做的，并不是操作系统调用回调函数
def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    # 事件循环这种模式在使用 IO 多路复用方式时会大量存在。
    # 1. select本身是不支持register模式。selector 对 select 进行了封装，故可以支持 register
    # 2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        # 这里的 stop 是全局变量
        # selector.select() 在 Windows 下面调用的是 select 方法，注意，当传入的列表为空时，会报错
        # 这也是为啥设置了一个全局 stop 变量。注意和 readable() 中的代码结合起来看，需要仔细体会。为了解决这个问题，还设置了一个 urls = [] 和 self.spider_url = url
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调+事件循环+select(poll\epoll)


if __name__ == "__main__":
    # fetcher = Fetcher()
    import time

    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time() - start_time)
