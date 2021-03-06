# Redis In Action #

## 1. hello redis ##

### 1.3 对文章进行投票 ###

## 3. Redis命令 ##

### 3.1 字符串 string ###

字符串可以存储的3种类型：

- 字节串 byte string
- 整数
- 浮点数

redis字符串自增和自减命令:

| 命令                        | 描述                                                 |
| --------------------------- | ---------------------------------------------------- |
| INCR key-name               | 对无法被解释为整数或者浮点型的字符串执行操作时会报错 |
| DECR key-name               | 可以自减为负数                                       |
| INCRBY key-name amount      |                                                      |
| DECRBY key-name amount      |                                                      |
| INCRBYFLOAT key-name amount | 在redis2.6及以上版本可用                             |

let's list the demo:

```console
conn = redis.Redis(db=1)
conn.get('key')
conn.incr('key')
Out[5]: 1
conn.incr('key', 34)
Out[6]: 35
conn.incr('key', -34)
Out[7]: 1
conn.incr('key', -34)
Out[8]: -33
conn.incr('key', -34)
Out[9]: -67
conn.set('key', 'abc')
Out[10]: True
conn.incr('key')
Traceback (most recent call last):
  File "D:\Projects\Python\simple\venv\lib\site-packages\IPython\core\interactiveshell.py", line 3361, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-11-b86f1ac8de83>", line 1, in <cell line: 1>
    conn.incr('key')
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\commands\core.py", line 1351, in incrby
    return self.execute_command("INCRBY", name, amount)
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\client.py", line 1176, in execute_command
    return conn.retry.call_with_retry(
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\retry.py", line 45, in call_with_retry
    return do()
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\client.py", line 1177, in <lambda>
    lambda: self._send_command_parse_response(
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\client.py", line 1153, in _send_command_parse_response
    return self.parse_response(conn, command_name, **options)
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\client.py", line 1192, in parse_response
    response = connection.read_response()
  File "D:\Projects\Python\simple\venv\lib\site-packages\redis\connection.py", line 829, in read_response
    raise response
redis.exceptions.ResponseError: value is not an integer or out of range
```

redis对字符串的其中一部分内容进行读取或者写入的操作：

| 命令     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| APPEND   | APPEND key-name value, 将value追加到当前存储的值的末尾, 执行命令之后会返回字符串当前长度 |
| GETRANGE | GETRANGE key-name start end, 获取一个由偏移量范围内的字符串子串，包括start & end. |
| SETRANGE | SETRANGE key offset value, offset下标从0开始，貌似offset为任何值都不会报错 |
| GETBIT   | GETBIT key offset                                            |
| SETBIT   | SETBIT key offset value, 将偏移量为offset的二进制位的值设置为 value |
| BITCOUNT | `BITCOUNT key [start end]` 统计二进制位串值为1的二进制位的数量。这里的start end 是以字节为单位的 |
| BITOP    | `BITOP operation dest-key key-name [key-name ...]` 对一个或者多个二进制位串执行 AND OR XOR NOT 任意一种按位运算操作，并将结果保存在 dest-key 中。 |
| STRLEN   | `STRLEN key-name` Get the length of the value stored in a key |

```console
conn.set('demo1', 'abc')
Out[12]: True
conn.append('demo1', 'def')
Out[13]: 6
conn.append('demo1', 'ghijkl')
Out[14]: 12
conn.getrange('demo1', 0, 3)
Out[15]: b'abcd'
conn.getrange('demo1', 0, -1)
Out[16]: b'abcdefghijkl'
conn.getrange('demo1', 0, -2)
Out[17]: b'abcdefghijk'
conn.getrange('demo1', 0, 5)
Out[18]: b'abcdef'
conn.setrange('demo1', 0, 'A')
Out[19]: 12
conn.get('demo1')
Out[20]: b'Abcdefghijkl'
conn.setrange('demo1', 0, 'ABC')
Out[21]: 12
conn.get('demo1')
Out[22]: b'ABCdefghijkl'
conn.setrange('demo1', 12, 'KKK')
Out[23]: 15
conn.get('demo1')
Out[24]: b'ABCdefghijklKKK'
conn.setrange('demo1', 14, 'DDDD')
Out[25]: 18
conn.get('demo1')
Out[26]: b'ABCdefghijklKKDDDD'
conn.setrange('demo1', 19, 'DDDD')
Out[27]: 23
conn.get('demo1')
Out[28]: b'ABCdefghijklKKDDDD\x00DDDD'

conn.set('demo1', 'ab')
Out[4]: True
conn.getbit('demo1', 1)
Out[5]: 1
conn.getbit('demo1', 2)
Out[6]: 1
conn.getbit('demo1', 3)
Out[7]: 0
conn.setbit('demo1', 7, 0)
Out[8]: 1
conn.setbit('demo1', 6, 1)
Out[9]: 0
conn.get('demo1')
Out[10]: b'bb'
```

### 3.2 列表 list ###

列表常用的命令：

| 命令   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| RPUSH  | `RPUSH key-name value [value ...]` 一个或者多个推入列表右端, 返回插入后列表的长度 |
| LPUSH  |                                                              |
| RPOP   | `RPOP key-name` 移除并返回列表最右端的元素                   |
| LPOP   |                                                              |
| LINDEX | `LINDEX key-name offset` 返回列表中偏移量为offset的元素      |
| LRANGE | `LRANGE key-name start end` 从start到end偏移量范围内的所有元素。 |
| LTIRM  | `LTRIM key-name start end` 保留从start到end偏移量内的元素，包括start和end。 |

```shell
127.0.0.1:6379[1]> flushall
OK
127.0.0.1:6379[1]> rpush l1 "abc" "ghj" "bnm" "123"
(integer) 4
127.0.0.1:6379[1]> lindex l1 0
"abc"
127.0.0.1:6379[1]> lindex l1 5
(nil)
127.0.0.1:6379[1]> lindex l1 3
"123"
127.0.0.1:6379[1]> lrange l1 0 1
1) "abc"
2) "ghj"
127.0.0.1:6379[1]> lrange l1 2 3
1) "bnm"
2) "123"
127.0.0.1:6379[1]> ltrim l1 2 3
OK
127.0.0.1:6379[1]> lrange l1 0 -1
1) "bnm"
2) "123"
127.0.0.1:6379[1]> rpush l1 "tom" "345" "asdf"
(integer) 5
127.0.0.1:6379[1]> lpush l1 "zxc"
(integer) 6
127.0.0.1:6379[1]> lpop l1
"zxc"
127.0.0.1:6379[1]>
```

阻塞式的列表命令：

| 命令       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| BLPOP      | `BLPOP key-name [key-name ...] timeout` 从第一个非空列表中弹出位于最左端的元素. 如果timeout=0,那么不会超时 |
| BRPOP      | 从第一个非空列表中弹出位于最右端的元素. 如果timeout=0,那么不会超时 |
| RPOPLPUSH  | `RPOPLPUSH source-key dest-key` 从source-key队列弹出最右端的元素，然后将这个元素推入dest-key列表的最左端，向用户返回。 |
| BRPOPLPUSH | 同上，为阻塞方法。                                           |
| LINSERT    | `LINSERT  key-name before|after element value` 在某个元素的前或者后面插入一个元素，成功返回列表的长度，失败返回-1 |
| LLEN       | Integer reply: the length of the list at key.                |
| LPUSHX     | Inserts specified values at the head of the list stored at key, only if key already exists and holds a list. |
| LSET       | simple string reply. An error is returned for out of range indexes. |

```console
127.0.0.1:6379[1]> rpush l1 "abc"
(integer) 1
127.0.0.1:6379[1]> lpush l1 "123" "234" "345"
(integer) 4
127.0.0.1:6379[1]> linsert l1 before "abc" "tt"
(integer) 5
127.0.0.1:6379[1]> linsert l1 before "abcd" "tt"
(integer) -1
127.0.0.1:6379[1]> llen l1
(integer) 5
127.0.0.1:6379[1]> lpushx l1 "gg"
(integer) 6
127.0.0.1:6379[1]> lpushx l2 "gg"
(integer) 0

127.0.0.1:6379[1]> lset l1 0 "ff"
OK
127.0.0.1:6379[1]> lset l1 -1 "ll"
OK
127.0.0.1:6379[1]> lset l1 45 "llgg"
(error) ERR index out of range
```

### 3.3 集合 set ###

集合以无序的方式来存储各不相同的元素，下面列出了一些常见的命令：

| 命令        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| SADD        | `SADD key-name item [item ...]` 将一个或者多个元素添加到集合，返回添加成功的数量 |
| SCARD       | Integer reply: the cardinality (number of elements) of the set, or 0 if key does not exist. |
| SDIFF       | `SDIFF key-name [key-name ...]` 返回由第一个集合与所有后续集合之差产生的集合的成员。(列表中包含结果集的成员。) |
| SDIFFSTORE  | 返回由第一个集合与所有后续集合之差产生的集合的成员列表，并将结果存储在指定的key |
| SINTER      | 返回由所有给定集合的交集生成的集合的成员。(Array reply: list with members of the resulting set.) |
| SINTERSTORE | 返回由所有给定集合的交集生成的集合的成员, 并将结果存储在指定的key |
| SISMEMBER   | 检查member是否存在于集合中，返回1表示存在，0表示不存在。     |
| SMEMBERS    | 返回存储在key处的集合值的所有成员。(Array reply: all elements of the set.) |
| SMOVE       | `SMOVE source-key dest-key item` Move a member from one set to another |
| SPOP        | 从集合中随机弹出一个元素                                     |
| SRANDMEMBER | `srandmember key [count]`  从集合里面随机地返回一个或者多个元素 |
| SSCAN       | `SSCAN key cursor [MATCH pattern] [COUNT count]` 增量的扫描set中的元素，cursor默认开始扫描时设为0，pattern为要匹配的元素的模式，count为一次扫描的数量，返回两部分数据，第一部分返回下一次扫描的cursor，第二部分为扫描得到的结果，直到最终cursor返回0. |

```console
127.0.0.1:6379[1]> sadd s1 "a" "b" "C" "d"
(integer) 4
127.0.0.1:6379[1]> sadd s1 "a" "b" "C" "d"
(integer) 0
127.0.0.1:6379[1]> sadd s1 "5"
(integer) 1
127.0.0.1:6379[1]> scard s1
(integer) 5
127.0.0.1:6379[1]> sadd s2 "a" "b"
(integer) 2
127.0.0.1:6379[1]> sdiff s1 s2
1) "C"
2) "5"
3) "d"
127.0.0.1:6379[1]> sdiffstore s3 s1 s2
(integer) 3
127.0.0.1:6379[1]>

127.0.0.1:6379[1]> sinter s1 s2
1) "b"
2) "a"
127.0.0.1:6379[1]> SISMEMBER s1 "a"
(integer) 1
127.0.0.1:6379[1]> SISMEMBER s1 "aaa"
(integer) 0
127.0.0.1:6379[1]> SMEMBERS s1
1) "C"
2) "a"
3) "d"
4) "5"
5) "b"
127.0.0.1:6379[1]>
```

### 3.4 散列 hash ###

与python对应的类型 dict

用于添加和删除键值对的散列操作：

| 命令    | 描述                                            |
| ------- | ----------------------------------------------- |
| HSET    | `HSET key field value`                          |
| HMSET   | `HMSET key field value [field value ...]`       |
| HDEL    | `HDEL key field [field ...]`                    |
| HEXISTS | `hexists key feild`                             |
| HGET    | `HGET key field`                                |
| HGETALL | `HGETALL key`                                   |
| HMGET   | `HMGET key field [feild ...]`                   |
| HKEYS   | `HKEYS key` 获取给定key的所有 field的集合。     |
| HLEN    | `HLEN field` Get the number of fields in a hash |

### 3.5 有序集合 zset / sort_set ###

分值以IEEE754双精度浮点数的格式存储

| 命令             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| ZADD             | `ZADD key [NX|XX] [CH] [INCR] score member [score member ...] ` 向有序集合中添加元素<br />NX: 只添加新元素。不要更新已经存在的元素。<br />XX: 只更新已经存在的元素。不要添加新元素。<br />CH: 更改返回值的表示方式，默认返回新添加的元素的数量，CH表示只返回score值更新的元素的数量 |
| ZCARD            | 获取已排序集合中的成员数                                     |
| ZRANK            | `zrank key-name member`  返回成员member在有序集合中的排序。member不存在返回 `nil` |
| ZREVRANK         | 反向排序                                                     |
| ZCOUNT           | `ZCOUNT key min max` 返回分值介于min和max之间的成员数量。<br />min和max可以取值为 `-inf` `+inf` `(` 前两个表示最小值和最大值， `(` 表示不包括或者叫开区间 |
| ZLEXCOUNT        | `ZLEXCOUNT key min max` 返回元素的字母排序介于 min和max之间的成员数量。<br />min和max的可取值为 `-` `+` `[` `(` |
| ZRANGE           | `zrange key start stop [WITHSCORES]` 返回有序集合中排名介于 start stop之间的成员 <br />start stop 可取值类似于 zount的min max |
| ZRANGEBYLEX      | 使用元素的字符编码排序来返回成员。                           |
| ZRANGEBYSCORE    | 使用分值的排序来返回成员                                     |
| ZREVRANGE        | 同上，只不过使用反向排序。                                   |
| ZREVRANGEBYLEX   |                                                              |
| ZREVRANGEBYSCORE |                                                              |
| ZSCAN            | 同`SSCAN` `SCAN`                                             |
| ZSCORE           | 返回成员member的分值                                         |
| ZINTERSTORE      | `ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight] [AGGREGATE SUM` 对给定的集合执行交集运算。<br />weights: 分值的个数和key的个数必须匹配，聚合运算之前先对score进行weight。<br />返回值是存储到dest-key中的元素个数。 |
| ZUNIONSTORE      |                                                              |
| ZREM             | `ZREM key member [member ...]` 移除给定的成员。              |
| ZREMRANGEBYLEX   |                                                              |
| ZREMRANGEBYRANK  |                                                              |
| ZREMRANGEBYSCORE |                                                              |
| ZINCRBY          | `ZINCRBY key increment member`                               |

### 3.6 glob-style pattern ###

Supported glob-style patterns:

- `h?llo` matches `hello`, `hallo` and `hxllo`
- `h*llo` matches `hllo` and `heeeello`
- `h[ae]llo` matches `hello` and `hallo,` but not `hillo`
- `h[^e]llo` matches `hallo`, `hbllo`, ... but not `hello`
- `h[a-b]llo` matches `hallo` and `hbllo`

### 3.7 SORT命令 ###

### 3.8 基本的redis事务 ###

有五个相关的命令：

`WATCH` `MULTI` `EXEC` `UNWATCH` `DISCARD`

- 事务中的所有命令都被序列化并按顺序执行。在Redis事务执行的过程中，一个由其他客户端发出的请求是不可能被服务的。这保证了这些命令是作为单个隔离操作执行的。
- 要么所有的命令都被处理，要么不处理，所以Redis事务也是原子的。

使用`MULTI`命令输入Redis事务。该命令总是以OK回答。此时，用户可以发出多个命令。而不是执行这些命令，Redis将它们排队。调用`EXEC`后，将执行所有命令。

而调用`DISCARD`将清空事务队列并退出事务。

```
> MULTI
OK
> INCR foo
QUEUED
> INCR bar
QUEUED
> EXEC
1) (integer) 1
2) (integer) 1
```

从上面的会话中可以看到，EXEC返回一个应答数组，其中每个元素都是事务中单个命令的应答，顺序与发出命令的顺序相同。

在事务处理过程中，可能会遇到两种命令错误:

- 命令可能无法进入队列，因此在调用EXEC之前可能会出现错误。
- 调用EXEC后，命令可能会失败，例如，因为我们对值错误的键执行了操作(比如对字符串值调用列表操作)。

客户端习惯于通过检查队列命令的返回值来感知第一种错误，即在EXEC调用之前发生的错误:如果命令响应queued，那么它就被正确地排队了，否则Redis将返回一个错误。如果在命令队列中出现错误，大多数客户端将放弃事务并丢弃它。

但是从Redis 2.6.5开始，服务器会记住在积累命令的过程中有一个错误，并且会拒绝执行事务，在EXEC过程中也会返回一个错误，并自动丢弃该事务。

----

在EXEC之后发生的错误不会以特殊的方式处理:即使在事务执行过程中某些命令失败，也会执行所有其他命令。

在对应的python客户端中 使用 **pipeline** .

### 3.9 键的过期时间 ###

| 命令      | 描述                                             |
| --------- | ------------------------------------------------ |
| PERSIST   | 移除键的过期时间                                 |
| TTL       | 查看键距离过期还有多少秒                         |
| EXPIRE    | 给键指定过期时间(秒)                             |
| EXPIREAT  | 将给定键的过期时间设置为给定unix时间戳           |
| PTTL      | 距离过期时间还有多少毫秒                         |
| PEXPIRE   | 给键指定过期的毫秒数                             |
| PEXPIREAT | 将一个毫秒精度的unix时间戳设置为给定键的过期时间 |

## 4. 数据安全与性能保障 ##

### 4.1 持久化选项 ###

### 4.4 Redis 事务 ###

一次性发送多个命令，然后等待所有回复出现的做法称为流水线(pipelining)

WATCH用于为Redis事务提供检查和设置(CAS)行为。

监视键是为了检测针对它们的变化。如果在执行EXEC命令之前至少修改了一个被监视的键，整个事务就会中止，并且EXEC返回一个Null回复来通知事务失败。

```
WATCH mykey
val = GET mykey
val = val + 1
MULTI
SET mykey $val
EXEC
```

使用上述代码，如果存在竞争条件，并且在调用WATCH和调用EXEC之间的时间内，另一个客户端修改了val的结果，则事务将失败。

那么WATCH到底是什么呢?这是一个命令，将使EXEC有条件:我们要求Redis执行事务，只有当没有被修改的键。这包括客户端所做的修改，如写命令，以及Redis本身所做的修改，如过期或逐出。如果在监视key和接收到EXEC之间修改了密钥，则整个事务将被中止。

在使用watch命令对键进行监视之后，直到用户执行exec命令的这段时间里面，如果有其他客户端抢先对任何被监视的key进行了替换，更新，删除操作，那么当用户尝试执行exec时，事务将失败并返回一个错误。

### 4.5 非事务型流水线 ###

`pipe = conn.pipeline(False)`

## 5. 使用redis构建支持程序 ##

### 5.1 使用redis来记录日志 ###

