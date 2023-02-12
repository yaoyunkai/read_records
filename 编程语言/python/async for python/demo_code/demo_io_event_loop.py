"""
The code created by Liberty on 2021/9/12

"""

"""
# 操作系统的IO复用示例伪代码
io_register(io_id, io_type)  # 向操作系统io注册自己关注的io操作的id和类型
io_register(io_id, io_type)
# 获取完成的io操作, 使用 epoll() in Linux and kqueue() in Unix
events = io_get_finished()

for (io_id, io_type) in events:
    if io_type == READ:
        data = read_data(io_id)
    elif io_type == WRITE:
        write_data(io_id，data)


-----------------------------------------------------------------------------------
call_backs = {}

def handler(req):
    # do jobs here
    io_register(io_id, io_type)
    def call_back(result):
        # do something
        # ......
    # 使用返回的result完成剩余工作
    call_backs[io_id] = call_back

# 新的循环
while True：
    # 获取已经完成的io事件
    events = io_get_finished()
    for (io_id, io_type) in events:
        if io_type == READ: # 读取
            data = read(io_id)
            call_back = call_backs[io_id]
            call_back(data)
        else:
            # 其他类型io事件的处理
            pass

    # 获取一个新请求
    request = accept()
    # 根据路由映射获取到用户写的业务逻辑函数
    handler = get_handler(request)
    # 运行用户的handler，处理请求
    handler(request)

我们的handler对于IO操作，注册了回调就立刻返回，
同时每次迭代都会对已完成的IO执行回调，网络请求不再阻塞整个服务器。

而且就连接受新请求也是在从操作系统得到监听端口的IO事件后进行的。
我们如果把循环部分还有call_backs字典拆分到单独模块，就能得到一个EventLoop，也就是python标准库 asyncio包中提供的ioloop

"""