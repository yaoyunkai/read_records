"""
The code created by Liberty on 2021/9/13

Lib/asyncio/streams.py
流是用于处理网络连接的支持 async/await 的高层级原语。 流允许发送和接收数据，而不需要使用回调或低级协议和传输。

asyncio.open_connection(host=None, port=None, *, loop=None, limit=None, ssl=None, family=0,
                        proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None)

asyncio.start_server(...)

StreamReader
StreamWriter


"""

import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 9999)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client('Hello World!'))
