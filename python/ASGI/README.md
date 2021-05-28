# ASGI

## How does ASGI work? ##

ASGI的结构是单一的、异步的、可调用的。它接受一个范围，该范围是一个包含特定连接detail info `dict`。

```python
async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...})
```

每一个收到的或者发送的 `event` 都是一个Python dict, 使用预定义的格式。这些事件都有一个定义好的类型键( `type` )，可以用来推断事件的结构。

```python
{
    "type": "http.request",
    "body": b"Hello World",
    "more_body": False,
}
```

## Specifications ##

### ASGI Specification ###

Asynchronous Server Gateway Interface

#### Abstract ####

此基本规范旨在修复这些服务器交互和运行应用程序代码所需的api集;每个受支持的协议(比如HTTP)都有一个子规范，概述了如何将该协议编码和解码为消息。

#### Rationale 基本原理 ####

它还采用了将协议转换为python兼容、异步友好的消息集的原则，并将其概括为两部分;用于构建服务器的标准化通信接口(本文档)，以及针对每种协议的一组标准消息格式。

它的主要目标是提供一种编写HTTP/2和WebSocket代码以及普通HTTP处理代码的方法，

#### Overview ####

ASGI包含两个不同的组件:

- A *protocol server*, which terminates sockets and translates them into connections and per-connection event messages.
- An *application*, which lives inside a *protocol server*, is called once per connection, and handles event messages as they happen, emitting its own event messages back when necessary.

与WSGI类似，服务器在其内部承载应用程序，并以标准格式向其发送传入请求。然而，与WSGI不同的是，应用程序是异步可调用的，而不是简单的可调用的，它们通过接收和发送异步事件消息与服务器通信，而不是接收单个输入流并返回单个可迭代对象。ASGI应用程序必须以 `async` / `await` 兼容的协程运行(即asyncio-compatible)(在主线程中;如果需要同步代码，它们可以自由使用线程或其他进程)。

there are two separate parts to an ASGI connection:

- A *connection scope*, which represents a protocol connection to a user and survives until the connection closes.
- *Events*, which are messages sent to the application as things happen on the connection, and messages sent back by the application to be received by the server, including data to be transmitted to the client.

应用程序通过连接范围和两个可等待的可调用对象被调用 and two awaitable callables to `receive` event messages and `send` event messages back. All this happening in an asynchronous event loop.

可调用的应用程序的每个调用都映射到一个传入的“套接字”或连接，并且预计将持续到该连接的生命周期，如果有清理工作要做，则会延长一点时间.

#### Specification Details ####

**连接域：connection scope**

用户与ASGI应用程序的每个连接都会导致可调用该应用程序的调用，以完全处理该连接。 它的寿命以及描述每个特定连接的信息称为连接范围。

Depending on the protocol spec, applications may have to wait for an initial opening message before communicating with the client.

**Events**

ASGI将协议分解成一系列应用程序必须接收和响应的事件，以及应用程序可能发送响应的事件。

对于HTTP， this is as simple as *receiving* two events in order - `http.request` and `http.disconnect`, and *sending* the corresponding event messages back. 

每个事件都是一个字典，其最顶层的key: `type` 包含消息类型的Unicode字符串。

`type` 对应的value必须是可序列化的。

**Applications**

```python
coroutine application(scope, receive, send)
# receive: an awaitable callable that will yield a new event dictionary when one is available
# send: an awaitable callable taking a single event dictionary as a positional argument that will return once the send has been completed or the connection has been closed
```

`scope.type` `scope.asgi.version`

**Protocol Specifications**

在 `scope` 中， type 必须是 unicode string, like `"http"` or `"websocket"`, as defined in the relevant protocol specification.

在 `message` 中, the `type` should be namespaced as `protocol.message_type`, where the `protocol` matches the scope type

**Middleware**

**Error Handling**

**Extra Coroutines**

**Extensions**

通过扩展 scope字典来实现。

### HTTP and WebSocket protocol ###

#### Spec Versions ####

- `2.0`: The first version of the spec, released with ASGI 2.0
- `2.1`: Added the `headers` key to the WebSocket Accept response
- `2.2`: Allow `None` in the second item of `server` scope value.

#### HTTP ####

HTTP格式包括HTTP/1.0、HTTP/1.1和HTTP/2，因为HTTP/2的变化主要在传输级别。协议服务器应该在相同的HTTP/2连接上为不同的请求提供不同的作用域，并正确地将响应多路复用回它们到达的同一流。HTTP版本以字符串的形式出现在作用域中。

在HTTP中，具有相同名称的多个报头字段很复杂。RFC 7230指出，对于任何可以出现多次的报头字段，它完全等价于只发送该报头字段一次，并使用逗号连接所有的值。

Notice: Cookie and Set-Cookie

##### HTTP Connection Scope #####

HTTP连接有一个单请求连接范围——也就是说，您的应用程序将在请求开始时被调用，并将持续到特定请求结束时，即使底层套接字仍然打开并服务多个请求。

如果将响应保持为长轮询或类似的打开状态，则连接范围将持续存在，直到响应从客户端或服务器端关闭为止。

- `type` (*Unicode string*) – `"http"`.
- `asgi["version"]` (*Unicode string*) – Version of the ASGI spec.
- `asgi["spec_version"]` (*Unicode string*) – Version of the ASGI HTTP spec this server understands; one of `"2.0"` or `"2.1"`. Optional; if missing assume `2.0`.
- `http_version` (*Unicode string*) – One of `"1.0"`, `"1.1"` or `"2"`.
- `method` (*Unicode string*) – The HTTP method name, uppercased.
- `scheme` (*Unicode string*) – URL scheme portion (likely `"http"` or `"https"`). Optional (but must not be empty); default is `"http"`.
- `path` (*Unicode string*) – HTTP request target excluding any query string, with percent-encoded sequences and UTF-8 byte sequences decoded into characters.
- `raw_path` (*byte string*) – The original HTTP path component unmodified from the bytes that were received by the web server. Some web server implementations may be unable to provide this. Optional; if missing defaults to `None`.
- `query_string` (*byte string*) – URL portion after the `?`, percent-encoded.
- `root_path` (*Unicode string*) – The root path this application is mounted at; same as `SCRIPT_NAME` in WSGI. Optional; if missing defaults to `""`.
- `headers` (*Iterable[[byte string, byte string]]*) – An iterable of `[name, value]` two-item iterables, where `name` is the header name, and `value` is the header value. Order of header values must be preserved from the original HTTP request; order of header names is not important. Duplicates are possible and must be preserved in the message as received. Header names must be lowercased. Pseudo headers (present in HTTP/2 and HTTP/3) must be removed; if `:authority` is present its value must be added to the start of the iterable with `host` as the header name or replace any existing host header already present.
- `client` (*Iterable[Unicode string, int]*) – A two-item iterable of `[host, port]`, where `host` is the remote host’s IPv4 or IPv6 address, and `port` is the remote port as an integer. Optional; if missing defaults to `None`.
- `server` (*Iterable[Unicode string, Optional[int]]*) – Either a two-item iterable of `[host, port]`, where `host` is the listening address for this server, and `port` is the integer listening port, or `[path, None]` where `path` is that of the unix socket. Optional; if missing defaults to `None`. 

##### Request 'receive' event #####

- type: http.request
- body: request body
- more_body: 表示是否有额外的内容要来(作为请求消息的一部分)。

##### Response Start 'send' event #####

由应用程序发送，以开始向客户机发送响应。后面必须至少有一条响应内容消息。在接收到至少一个响应体事件之前，协议服务器不能开始向客户端发送响应。

- type: http.response.start
- status: HTTP status code (int)
- headers: 

##### Response Body 'send' event #####

继续向客户端发送响应。在从send调用返回之前，协议服务器必须将传递给它们的任何数据刷新到send缓冲区。如果more_body设置为False，将关闭连接。

- type: http.response.body
- body: HTTP body content
- more_body：

##### Disconnect 'receive' event #####

当HTTP连接关闭或在发送响应后调用receive时发送到应用程序。这主要适用于长轮询，在这种情况下，如果连接提前关闭，您可能希望触发清理代码。

- type: http.disconnect

#### WebSocket ####

#### WSGI Compatibility ####

- `REQUEST_METHOD` is the `method`
- `SCRIPT_NAME` is `root_path`
- `PATH_INFO` can be derived from `path` and `root_path`
- `QUERY_STRING` is `query_string`
- `CONTENT_TYPE` can be extracted from `headers`
- `CONTENT_LENGTH` can be extracted from `headers`
- `SERVER_NAME` and `SERVER_PORT` are in `server`
- `REMOTE_HOST`/`REMOTE_ADDR` and `REMOTE_PORT` are in `client`
- `SERVER_PROTOCOL` is encoded in `http_version`
- `wsgi.url_scheme` is `scheme`
- `wsgi.input` is a `StringIO` based around the `http.request` messages
- `wsgi.errors` is directed by the wrapper as needed

start_response --> http.response.start

application call --> http.response.body

### Lifespan ###

ASGI生命周期子规范概述了如何在ASGI中通信生命周期事件，比如启动和关闭。这指的是主事件循环的生命周期。在多进程环境中，每个进程中将有生命周期事件。

生命周期消息允许应用程序在正在运行的事件循环的上下文中初始化和关闭。这方面的一个示例是创建连接池，然后关闭连接池以释放连接。

```python
async def app(scope, receive, send):
    if scope['type'] == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                ... # Do some startup here!
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                ... # Do some shutdown here!
                await send({'type': 'lifespan.shutdown.complete'})
                return
    else:
        pass # Handle other types
```

#### Scope  ####

`type: will startswith lifespan.`