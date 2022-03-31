# Scripting with Lua #

Redis保证了脚本的原子执行。在执行脚本时，所有服务器活动在整个运行时都被阻塞。这些语义意味着脚本的所有效果要么还没有发生，要么已经发生。

脚本提供了几个在许多情况下都很有价值的属性。这些包括:

- 通过执行数据所在的逻辑提供局部性。数据局部性减少了总体延迟并节省了网络资源。
- 阻塞语义，确保脚本的原子执行。
- 支持简单功能的组合，这些功能要么是Redis缺少的，要么是过于小众的一部分。

Lua允许你在Redis中运行你的部分应用逻辑。这样的脚本可以跨多个键执行有条件的更新，可能以原子方式组合几种不同的数据类型。

## Getting started ##

我们将使用EVAL命令开始编写Redis脚本。

```lua
> EVAL "return 'Hello, scripting!'" 0
"Hello, scripting!"
```

在这个例子中，EVAL有两个参数。第一个参数是由脚本的Lua源代码组成的字符串。这个脚本不需要包含任何Lua函数的定义。它只是一个运行在Redis引擎上下文中的Lua程序。

第二个参数是脚本主体后面的参数的数量，从第三个参数开始，表示Redis键名。在本例中，我们使用值0，因为我们没有为脚本提供任何参数，无论是否键名。

## 脚本参数化 ##

```lua
redis> EVAL "return ARGV[1]" 0 Hello
"Hello"
redis> EVAL "return ARGV[1]" 0 Parameterization!
"Parameterization!"
```

在这一点上，有必要理解Redis在输入参数之间的区别，这些参数是键名和那些不是。

为了确保脚本的正确执行，无论是在独立部署还是集群部署中，脚本访问的所有键名都必须显式地作为输入键参数提供。脚本应该只访问名称作为输入参数给出的键。脚本不应该使用程序生成的名称或基于数据库中存储的数据结构的内容访问键。

函数中任何非键名的输入都是常规输入参数。

下面试图演示脚本KEYS和ARGV运行时全局变量之间的输入参数分配:

```
redis> EVAL "return { KEYS[1], KEYS[2], ARGV[1], ARGV[2], ARGV[3] }" 2 key1 key2 arg1 arg2 arg3
1) "key1"
2) "key2"
3) "arg1"
4) "arg2"
5) "arg3"
```

## 通过脚本与Redis交互 ##

It is possible to call Redis commands from a Lua script either via [`redis.call()`](https://redis.io/topics/lua-api#redis.call) or [`redis.pcall()`](https://redis.io/topics/lua-api#redis.pcall).

但是，这两个函数之间的区别在于处理运行时错误(例如语法错误)的方式。调用`redis.call()`函数引发的错误将直接返回给执行它的客户端。相反，调用`redis.pcall()`函数时遇到的错误将被返回到脚本的执行上下文，以进行可能的处理。

```
> EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 foo bar
OK
```

## Script cache ##

每当调用EVAL时，我们也会在请求中包含脚本的源代码。重复调用EVAL来执行同一组参数化脚本，既浪费了网络带宽，也在Redis中有一些开销。当然，节省网络和计算资源是关键，因此Redid为脚本提供了一种缓存机制。

使用EVAL执行的每个脚本都存储在服务器保存的专用缓存中。缓存的内容是由脚本的SHA1摘要和组织的，所以脚本的SHA1摘要和在缓存中唯一标识它。您可以通过运行EVAL并在之后调用INFO来验证此行为。您将注意到`used_memory_scripts_eval`和`number_of_cached_scripts`指标随着每执行一个新脚本而增长。

A script is loaded to the server’s cache by calling the [`SCRIPT LOAD`](https://redis.io/commands/script-load) command and providing its source code. 

```
redis> SCRIPT LOAD "return 'Immabe a cached script'"
"c664a3bf70bd1d45c4284ffebb65a6f2299bfc9f"
redis> EVALSHA c664a3bf70bd1d45c4284ffebb65a6f2299bfc9f 0
"Immabe a cached script"
```

### Cache valatility ###

Redis脚本缓存总是不稳定的。它没有被认为是数据库的一部分，也没有被持久化。缓存可以在服务器重启时清除，也可以在副本担任主角色时进行故障转移时清除，也可以通过`SCRIPT FLUSH`显式地清除。这意味着缓存的脚本是短暂的，缓存的内容随时可能丢失。

Applications that use scripts should always call [`EVALSHA`](https://redis.io/commands/evalsha) to execute them. The server returns an error if the script’s SHA1 digest is not in the cache.

```
redis> EVALSHA ffffffffffffffffffffffffffffffffffffffff 0
(error) NOSCRIPT No matching script
```

### EVALSHA in the context of pipelining ###

应该特别注意在流水线请求的上下文中执行EVALSHA。流水线请求中的命令按照发送的顺序运行，但其他客户端的命令可能会在这些请求之间交叉执行。因此，`NOSCRIPT`错误可以从流水线请求中返回，但不能被处理。

因此，客户端库的实现应该恢复到在管道上下文中使用参数化的普通EVAL。

### 脚本缓存语义 ###

在正常操作期间，应用程序的脚本应该无限期地留在缓存中(也就是说，直到服务器重启或缓存被刷新)。其根本原因是，编写良好的应用程序的脚本缓存内容不太可能持续增长。即使是使用数百个缓存脚本的大型应用程序也不应该使用缓存内存。

清除脚本缓存的唯一方法是显式地调用`script flush`命令。运行该命令将完全刷新脚本缓存，删除到目前为止执行的所有脚本。通常，只有在云环境中为另一个客户或应用程序实例化时才需要这样做。

另外，正如前面提到的，重新启动一个Redis实例会刷新非持久化脚本缓存。然而，从Redis客户端的角度来看，只有两种方法可以确保Redis实例在两个不同的命令之间没有重启:

- 我们与服务器的连接是持久的，到目前为止从未关闭过。
- The client explicitly checks the `runid` field in the [`INFO`](https://redis.io/commands/info) command to ensure the server was not restarted and is still the same process.

## SCRIPT command ##

- `SCRIPT FLUSH` 这个命令是强制Redis刷新脚本缓存的唯一方法。
- `SCRIPT EXISTS` given one or more SHA1 digests as arguments, this command returns an array of *1*’s and *0*’s.
- `SCRIPT LOAD script` 
- `SCRIPT KILL` this command is the only way to interrupt a long-running script (a.k.a slow script), short of shutting down the server. 
- `SCRIPT DEBUG` 

