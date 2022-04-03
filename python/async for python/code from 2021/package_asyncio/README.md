# Coroutines

## 基本概念 ##

### 1、协程（coroutine）——本质就是一个函数 ###

所谓的“协程”就是一个函数，这个函数需要有两个基本的组成要素，第一，需要使用`@asyncio.coroutine`进行装饰；第二，函数体内一定要有`yield from` 返回的`generator`，或者是说使用`yield from` 返回另一个协程对象。

当然，这两个条件并不是硬性规定的，如果没有这两个条件，依然是函数，只不过是普通函数而已。

怎么判断一个函数是不是协程？通过`asyncio.iscoroutine(obj)`和`asyncio.iscoroutinefunction(func)`加以判断，返回true，则是。

那么协程函数有什么作用呢？

（1）result = yield from future

作用一：返回future的结果。什么是future？后面会讲到。当协程函数执行到这一句，协程会被悬挂起来，知道future的结果被返回。如果是future被中途取消，则会触发CancelledError异常。由于task是future的子类，后面也会介绍，关于future的所有应用，都同样适用于task

（2）result = yield from coroutine

等候另一个协程函数返回结果或者是触发异常 

（3）result= yield from task

返回一个task的结果

（4）return expression

作为一个函数，他本身也是可以返回某一个结果的

（5）raise exception 

### 2、事件循环 event_loop ###

协程函数，不是像普通函数那样直接调用运行的，必须添加到事件循环中，然后由事件循环去运行，单独运行协程函数是不会有结果的

```python
import time
import asyncio
async def say_after_time(delay,what):
        await asyncio.sleep(delay)
        print(what)
 
async def main():
        print(f"开始时间为： {time.time()}")
        await say_after_time(1,"hello")
        await say_after_time(2,"world")
        print(f"结束时间为： {time.time()}")
 
loop=asyncio.get_event_loop()    #创建事件循环对象
#loop=asyncio.new_event_loop()   #与上面等价，创建新的事件循环
loop.run_until_complete(main())  #通过事件循环对象运行协程函数
loop.close()
```

（1）获取事件循环对象的几种方式：

下面几种方式可以用来获取、设置、创建事件循环对象loop

`loop=asyncio.get_running_loop()` 返回（获取）在当前线程中正在运行的事件循环，如果没有正在运行的事件循环，则会显示错误；它是python3.7中新添加的

`loop=asyncio.get_event_loop()` 获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop；

`loop=asyncio.set_event_loop(loop)` 设置一个事件循环为当前线程的事件循环；

`loop=asyncio.new_event_loop()` 创建一个新的事件循环

（2）通过事件循环运行协程函数的两种方式：

（1）方式一：创建事件循环对象loop，即asyncio.get_event_loop()，通过事件循环运行协程函数

（2）方式二：直接通过asyncio.run(function_name)运行协程函数。但是需要注意的是，首先run函数是python3.7版本新添加的，前面的版本是没有的；其次，这个run函数总是会创建一个新的事件循环并在run结束之后关闭事件循环，所以，如果在同一个线程中已经有了一个事件循环，则不能再使用这个函数了，因为同一个线程不能有两个事件循环，而且这个run函数不能同时运行两次，因为他已经创建一个了。即同一个线程中是不允许有多个事件循环loop的。

asyncio.run（）是python3.7 新添加的内容，也是后面推荐的运行任务的方式，因为它是高层API，后面会讲到它与asyncio.run_until_complete()的差异性，run_until_complete()是相对较低层的API。

### 3、什么是awaitable对象 即可暂停等待的对象 ###

有三类对象是可等待的，即 coroutines, Tasks, and Futures.

coroutine：本质上就是一个函数，一前面的生成器yield和yield from为基础，不再赘述；

Tasks: 任务，顾名思义，就是要完成某件事情，其实就是对协程函数进一步的封装；

Future：它是一个“更底层”的概念，他代表一个一步操作的最终结果，因为一步操作一般用于耗时操作，结果不会立即得到，会在“将来”得到异步运行的结果，故而命名为Future。

三者的关系，coroutine可以自动封装成task，而Task是Future的子类。

### 4、什么是task任务 ###

如前所述，`Task`用来 **并发调度的**协程，即对协程函数的进一步包装？那为什么还需要包装呢？因为单纯的协程函数仅仅是一个函数而已，将其包装成任务，任务是可以包含各种状态的，异步编程最重要的就是对异步操作状态的把控了。

（1）创建任务（两种方法）：

方法一：`task = asyncio.create_task(coro())`  # 这是3.7版本新添加的

方法二：`task = asyncio.ensure_future(coro())`

（2）获取某一个任务的方法：

方法一：`task=asyncio.current_task(loop=None)`

返回在某一个指定的loop中，当前正在运行的任务，如果没有任务正在运行，则返回None；

如果loop为None，则默认为在当前的事件循环中获取，

方法二：`asyncio.all_tasks(loop=None)`

返回某一个loop中还没有结束的任务

### 5、什么是future？ ###

Future是一个较低层的可等待（awaitable）对象，他表示的是异步操作的最终结果，当一个Future对象被等待的时候，协程会一直等待，直到Future已经运算完毕。

Future是Task的父类，一般情况下，已不用去管它们两者的详细区别，也没有必要去用Future，用Task就可以了，

返回 future 对象的低级函数的一个很好的例子是

## 二、asyncio的基本架构 ##

asyncio分为高层API和低层API，

High-level APIs:

- [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Streams](https://docs.python.org/3/library/asyncio-stream.html)
- [Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html)
- [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html)
- [Queues](https://docs.python.org/3/library/asyncio-queue.html)
- [Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html)

Low-level APIs:

- [Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html)
- [Futures](https://docs.python.org/3/library/asyncio-future.html)
- [Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html)
- [Policies](https://docs.python.org/3/library/asyncio-policy.html)
- [Platform Support](https://docs.python.org/3/library/asyncio-platforms.html)

### 常见的High-level API方法 ###

1, 运行异步协程: `asyncio.run(coro, *, debug=False)`

2, 创建任务: `task=asyncio.create_task(coro)` `task = asyncio.ensure_future(coro()) `

3, 睡眠：

`await asyncio.sleep(delay, result=None, *, loop=None)`

这个函数表示的是：当前的那个任务（协程函数）睡眠多长时间，而允许其他任务执行。这是它与time.sleep()的区别，time.sleep()是当前线程休息，注意他们的区别哦。

另外如果提供了参数result，当当前任务（协程）结束的时候，它会返回；

4，并发运行多个任务

`await asyncio.gather(*coros_or_futures, loop=None, return_exceptions=False)`

`*coros_or_futures`是一个序列拆分操作，如果是以个协程函数，则会自动转换成Task。

当所有的任务都完成之后，返回的结果是一个列表的形式，列表中值的顺序和*coros_or_futures完成的顺序是一样的。

如果gather()本身被取消了，那么绑定在它里面的任务也就取消了。

6，设置 timeout 

`await asyncio.wait_for(aw, timeout, *, loop=None)`

如果aw是一个协程函数，会自动包装成一个任务task。

```python
import asyncio


async def func1():
    print('let\'s func1 start now...')
    await asyncio.sleep(3600)
    print('finally func1 execute down...')


async def main():
    try:
        print('wait you 3 seconds.....')
        await asyncio.wait_for(func1(), timeout=3)
    except asyncio.TimeoutError:
        print('timeout .....')


asyncio.run(main())
```

当异步操作需要执行的时间超过waitfor设置的timeout，就会触发异常，

7，多个协程函数时候的等待

`await asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)`
与上面的区别是，第一个参数aws是一个集合，要写成集合set的形式，

**注意：**该函数的返回值是两个Tasks/Futures的集合：

`(done, pending)`

其中done是一个集合，表示已经完成的任务tasks；pending也是一个集合，表示还没有完成的任务。
常见的使用方法为：`done, pending = await asyncio.wait(aws)`

*return_when* 参数的意思：

| Constant        | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| FIRST_COMPLETED | 当任何一个task或者是future完成或者是取消，wait函数就返回     |
| FIRST_EXCEPTION | 当任何一个task或者是future触发了某一个异常，就返回，.如果是所有的task和future都没有触发异常，则等价与下面的 `ALL_COMPLETED`. |
| ALL_COMPLETED   | 当所有的task或者是future都完成或者是都取消的时候，再返回。   |

```python
import asyncio
import time

a = time.time()


async def hello1():  # 大约2秒
    print("Hello world 01 begin")
    await asyncio.sleep(2)
    print("Hello again 01 end")


async def hello2():  # 大约3秒
    print("Hello world 02 begin")
    await asyncio.sleep(3)
    print("Hello again 02 end")


async def hello3():  # 大约4秒
    print("Hello world 03 begin")
    await asyncio.sleep(4)
    print("Hello again 03 end")


async def main():  # 入口函数
    done, pending = await asyncio.wait({hello1(), hello2(), hello3()}, return_when=asyncio.FIRST_COMPLETED)
    for i in done:
        print(i)
    for j in pending:
        print(j)


asyncio.run(main())  # 运行入口函数

b = time.time()
print('---------------------------------------')
print(b - a)
```

### 2、Task 类详解 ###

（1）他是作为一个python协程对象，和Future对象很像的这么一个对象，但不是线程安全的；他继承了Future所有的API，，除了`Future.set_result()`和`Future.set_Exception()`；

（2）使用高层API  `asyncio.ccreate_task()`创建任务，或者是使用低层API `loop.create_task()`或者是`loop.ensure_future()`创建任务对象；

（3）相比于协程函数，任务时有状态的，可以使用`Task.cancel()`进行取消，这会触发CancelledError异常，使用cancelled()检查是否取消.

Task中常见的一些函数

1，cancel

其实前面已经有所介绍，最好是使用他会出发CancelledError异常，所以需要取消的协程函数里面的代码最好在try-except语句块中进行，这样方便触发异常，打印相关信息，但是Task.cancel()没有办法保证任务一定会取消，而Future.cancel()是可以保证任务一定取消的。

```python
import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')
    try:
        await asyncio.sleep(3600)  # 模拟一个耗时任务
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    task = asyncio.create_task(cancel_me())
    await asyncio.sleep(1)
    print('main is sleep down')
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


if __name__ == '__main__':
    asyncio.run(main())
```

2，done()

当一个被包装の协程既没有触发异常、也没有被取消的时候，意味着它是done的，返回true。

3，result()

返回任务的执行结果，

当任务被正常执行完毕，则返回结果；

当任务被取消了，调用这个方法，会触发CancelledError异常；

当任务返回的结果是无用的时候，则调用这个方法会触发InvalidStateError；

当任务出发了一个异常而中断，调用这个方法还会再次触发这个使程序中断的异常。

4, exception()

返回任务的异常信息，触发了什么异常，就返回什么异常，如果任务是正常执行的无异常，则返回None；

当任务被取消了，调用这个方法会触发CancelledError异常；

当任务没有做完，调用这个方法会触发InvalidStateError异常。

### 3、异步函数的结果获取 ###

1, 通过 task.result() 获取

```python
import asyncio


async def hello(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


coroutine = hello(10, 5)
loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(coroutine)  # 第二步:将多个协程函数包装成任务列表
loop.run_until_complete(task)  # 第三步：通过事件循环运行
print('-------------------------------------')
print(task.result())
loop.close()
```

2, 通过回调函数获取

```python
import asyncio


async def hello(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


def callback(f):
    print(f.result())
    
    
loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(hello(10, 5))  # 第二步:将多个协程函数包装成任务
task.add_done_callback(callback)  # 并被任务绑定一个回调函数

loop.run_until_complete(task)  # 第三步：通过事件循环运行
loop.close()
```

所谓的回调函数，就是指协程函数coroutine执行结束时候会调用回调函数。并通过参数future获取协程执行的结果。我们创建的task和回调里的future对象，实际上是同一个对象，因为task是future的子类。

## 三、asyncio异步编程的基本模板 ##

### 1、python3.7之前的版本 ###

(1) 无参数 无返回值

```python

import asyncio
import time
 
a=time.time()
 
async def hello1():
    print("Hello world 01 begin")
    await asyncio.sleep(3)  #模拟耗时任务3秒
    print("Hello again 01 end")
 
async def hello2():
    print("Hello world 02 begin")
    await asyncio.sleep(2)   #模拟耗时任务2秒
    print("Hello again 02 end")
 
async def hello3():
    print("Hello world 03 begin")
    await asyncio.sleep(4)   #模拟耗时任务4秒
    print("Hello again 03 end")
 
loop = asyncio.get_event_loop()                #第一步：创建事件循环
tasks = [hello1(), hello2(),hello3()]          #第二步:将多个协程函数包装成任务列表
loop.run_until_complete(asyncio.wait(tasks))   #第三步：通过事件循环运行
loop.close()                                   #第四步：取消事件循环
```

(2) 有参数 有返回值

```python

import asyncio
import time
 
 
async def hello1(a,b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  #模拟耗时任务3秒
    print("Hello again 01 end")
    return a+b
 
async def hello2(a,b):
    print("Hello world 02 begin")
    await asyncio.sleep(2)   #模拟耗时任务2秒
    print("Hello again 02 end")
    return a-b
 
async def hello3(a,b):
    print("Hello world 03 begin")
    await asyncio.sleep(4)   #模拟耗时任务4秒
    print("Hello again 03 end")
    return a*b
 
loop = asyncio.get_event_loop()                #第一步：创建事件循环
task1=asyncio.ensure_future(hello1(10,5))
task2=asyncio.ensure_future(hello2(10,5))
task3=asyncio.ensure_future(hello3(10,5))
tasks = [task1,task2,task3]                    #第二步:将多个协程函数包装成任务列表
loop.run_until_complete(asyncio.wait(tasks))   #第三步:通过事件循环运行
print(task1.result())                               #并且在所有的任务完成之后，获取异步函数的返回值   
print(task2.result())
print(task3.result())
loop.close()                                   #第四步：关闭事件循环
```

(3) 总结：

1，构造事件循环， 参考上面的四个方法

2，将一个或者是多个协程函数包装成任务Task

```python

#高层API
task = asyncio.create_task(coro(参数列表))   # 这是3.7版本新添加的
task = asyncio.ensure_future(coro(参数列表)) 
 
#低层API
loop.create_future(coro)
loop.create_task(coro)
```

3，通过事件循环运行

```python
loop.run_until_complete(asyncio.wait(tasks))  #通过asyncio.wait()整合多个task
loop.run_until_complete(asyncio.gather(tasks))  #通过asyncio.gather()整合多个task
loop.run_until_complete(task_1)  #单个任务则不需要整合
loop.run_forever()  #但是这个方法在新版本已经取消，不再推荐使用，因为使用起来不简洁
 
'''
使用gather或者wait可以同时注册多个任务，实现并发,但他们的设计是完全不一样的，在前面的2.1.(4)中已经讨论过了，主要区别如下：
（1）参数形式不一样
gather的参数为 *coroutines_or_futures,即如这种形式
      tasks = asyncio.gather(*[task1,task2,task3])或者
      tasks = asyncio.gather(task1,task2,task3)
      loop.run_until_complete(tasks)
wait的参数为列表或者集合的形式，如下
      tasks = asyncio.wait([task1,task2,task3])
      loop.run_until_complete(tasks)
（2）返回的值不一样
gather的定义如下，gather返回的是每一个任务运行的结果，
      results = await asyncio.gather(*tasks) 
wait的定义如下,返回dones是已经完成的任务，pending是未完成的任务，都是集合类型
 done, pending = yield from asyncio.wait(fs)
'''
```

4, 关闭事件循环

```python

loop.close()
 
'''
以上示例都没有调用 loop.close，好像也没有什么问题。所以到底要不要调 loop.close 呢？
简单来说，loop 只要不关闭，就还可以再运行：
loop.run_until_complete(do_some_work(loop, 1))
loop.run_until_complete(do_some_work(loop, 3))
loop.close()
但是如果关闭了，就不能再运行了：
loop.run_until_complete(do_some_work(loop, 1))
loop.close()
loop.run_until_complete(do_some_work(loop, 3))  # 此处异常
建议调用 loop.close，以彻底清理 loop 对象防止误用
'''
```

### 2、python3.7版本 ###

(1) 无参数，无返回值

```python
import asyncio
import time
 
 
async def hello1():
    print("Hello world 01 begin")
    await asyncio.sleep(3)  #模拟耗时任务3秒
    print("Hello again 01 end")
 
async def hello2():
    print("Hello world 02 begin")
    await asyncio.sleep(2)   #模拟耗时任务2秒
    print("Hello again 02 end")
 
async def hello3():
    print("Hello world 03 begin")
    await asyncio.sleep(4)   #模拟耗时任务4秒
    print("Hello again 03 end")
 
async def main():
    results=await asyncio.gather(hello1(),hello2(),hello3())
    for result in results:
        print(result)     #因为没返回值，故而返回None
 
asyncio.run(main())
```

(2) 有参数，有返回值

```python
import asyncio
import time
 
 
async def hello1(a,b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  #模拟耗时任务3秒
    print("Hello again 01 end")
    return a+b
 
async def hello2(a,b):
    print("Hello world 02 begin")
    await asyncio.sleep(2)   #模拟耗时任务2秒
    print("Hello again 02 end")
    return a-b
 
async def hello3(a,b):
    print("Hello world 03 begin")
    await asyncio.sleep(4)   #模拟耗时任务4秒
    print("Hello again 03 end")
    return a*b
 
async def main():
    results=await asyncio.gather(hello1(10,5),hello2(10,5),hello3(10,5))
    for result in results:
        print(result)
 
asyncio.run(main())
```

(3) 总结：

构建入口函数 main 然后使用 asyncio.run 启动。

## 四、事件循环EventLoop ##

**1、事件循环的创建、获取、设置**

（1）asyncio.get_running_loop()。python3.7新添加的

（2）asyncio.get_event_loop()

（3）asyncio.set_event_loop(loop)

（4）asyncio.new_event_loop()

**2、运行和停止事件循环**

（1）loop.run_until_complete(future)。运行事件循环，直到future运行结束

（2）loop.run_forever()。在python3.7中已经取消了，表示事件循环会一直运行，直到遇到stop。

（3）loop.stop()。停止事件循环

（4）loop.is_running()。如果事件循环依然在运行，则返回True

（5）loop.is_closed()。如果事件循环已经close，则返回True

（6）loop.close()。关闭事件循环

**3、创建Future和Task**

（1）loop.create_future(coroutine) ，返回future对象

（2）loop.create_task(corootine) ，返回task对象

（3）loop.set_task_factory(factory)

（4）loop.get_task_factory()

**4、事件循环的时钟**

 loop.time()

```python
import asyncio


async def hello1(a, b):
    print('准备做加法运算')
    await asyncio.sleep(3)
    return a + b


loop = asyncio.get_event_loop()
t1 = loop.time()
print(t1)

loop.run_until_complete(hello1(3, 4))
t2 = loop.time()
print(t2)
print(t2 - t1)
```

**5、计划执行回调函数（CallBacks）**

（1）`loop.call_later(delay, callback, *args, context=None)`

首先简单的说一下它的含义，就是事件循环在delay多长时间之后才执行callback函数，它的返回值是asyncio.TimerHandle类的一个实例对象。

（2）`loop.call_at(when, callback, *args, context=None)`

即在某一个时刻进行调用计划的回调函数，第一个参数不再是delay而是when，表示一个绝对的时间点，结合前面的loop.time使用，它的使用方法和call_later()很类似。它的返回值是asyncio.TimerHandle类的一个实例对象。

（3）`loop.call_soon(callback, *args, context=None)`

在下一个迭代的时间循环中立刻调用回调函数，用法同上面。它的返回值是asyncio.Handle类的一个实例对象。

（4）`loop.call_soon_threadsafe(callback, *args, context=None)`

这是call_soon()函数的线程安全版本，计划回调函数必须在另一个线程中使用。

```python
import asyncio


def callback(n):
    print('我是回调函数，参数为： {0} '.format(n))


async def main(_loop):
    print('在异步函数中注册回调函数')
    _loop.call_later(2, callback, 1)
    _loop.call_later(1, callback, 2)
    _loop.call_soon(callback, 3)

    await asyncio.sleep(4)


loop = asyncio.get_event_loop()
print('进入事件循环')
loop.run_until_complete(main(loop))
print('关闭事件循环')
loop.close()
```

Notice:

（1）CallBack函数只能够定义为同步方法，不能够定义为async方法，及不能使用async和@asyncio.coroutine修饰；

（2）每一个CallBack方法只会调用一次，如果在同一个时刻有另个CallBack方法需要调用，则他们的执行顺序是不确定的；

对于一般的异步函数，我们需要将它放在时间循环里面，然后通过事件循环去循环调用它，而因为CallBack并不是异步函数，它是定义为普通的同步方法，所以不能够放在时间循环里面，但是如果我依然想要让事件循环去执行它怎么办呢？那就不放进事件循环，直接让事件循环“立即、稍后、在什么时候”去执行它不就行了嘛，call的含义就是“执行”。

## 五、底层API之Future ##

Future的本质是一个类。他表示的是异步操作的最终将要返回的结果，故而命名为Future，它不是线程安全的。

**asyncio中关于Future的几个方法**

（1）asyncio.isfuture(obj) 。判断一个对象是不是Future，注意python中一切皆对象哦，包括函数，当obj是下面几种情况时返回true：

- asyncio.Future的实例对象
- asyncio.Task的实例对象
- 一个具有 `_asyncio_future_blocking` 属性的对象

（2）`asyncio.ensure_future(obj, *, loop=None)` 将一个obj包装成Future

（3）`asyncio.wrap_future(future, *, loop=None)` 将[`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future)对象包装成一个 [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future) 对象。

**Future对象的常用方法**

1，result()

如果Future被执行完成，如果使用set_result()方法设置了一个结果，那个设置的value就会被返回；

如果Future被执行完成，如果使用set_exception()方法设置了一个异常，那么使用这个方法也会触发异常；

如果Future被取消了，那么使用这个方法会触发CancelledError异常；

如果Future的结果不可用或者是不可达，那么使用这个方法也会触发InvalidStateError异常；

2，set_result(result) 标记Future已经执行完毕，并且设置它的返回值。

3，set_exception(exception) 标记Future已经执行完毕，并且触发一个异常。

4，done() 如果Future1执行完毕，则返回 `True` 。

5，cancelled() 判断任务是否取消

6，add_done_callback(callback, *, context=None) 在Future完成之后，给它添加一个回调方法，这个方法就相当于是loop.call_soon()方法，

7, remove_done_callback(callback)

8, cancel()

9, exception()

10, get_loop()

**一些问题**

在有很多个异步方式的时候，一定要尽量避免这种异步函数的直接调用，这和同步是没什么区别的，一定要通过事件循环loop，“让事件循环在各个异步函数之间不停游走”，这样才不会造成阻塞。

协程的四种状态： pending running done cancelled

**使用 gather 同时注册多个任务，实现并发**

```python
import asyncio
import time
 
 
async def hello1(a,b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  #模拟耗时任务3秒
    print("Hello again 01 end")
    return a+b
 
async def hello2(a,b):
    print("Hello world 02 begin")
    await asyncio.sleep(2)   #模拟耗时任务2秒
    print("Hello again 02 end")
    return a-b
 
async def hello3(a,b):
    print("Hello world 03 begin")
    await asyncio.sleep(4)   #模拟耗时任务4秒
    print("Hello again 03 end")
    return a*b
 
async def main():  #封装多任务的入口函数
    task1=asyncio.ensure_future(hello1(10,5))
    task2=asyncio.ensure_future(hello2(10,5))
    task3=asyncio.ensure_future(hello3(10,5))
    results=await asyncio.gather(task1,task2,task3)   
    for result in results:    #通过迭代获取函数的结果，每一个元素就是相对应的任务的返回值，顺序都没变
        print(result)
 
 
loop = asyncio.get_event_loop()               
loop.run_until_complete(main())
loop.close()                                 
```

**使用wait可以同时注册多个任务，实现并发**

```python
async def main():  #封装多任务的入口函数
    task1=asyncio.ensure_future(hello1(10,5))
    task2=asyncio.ensure_future(hello2(10,5))
    task3=asyncio.ensure_future(hello3(10,5))
    done,pending=await asyncio.wait([task1,task2,task3])   
    for done_task in done:
        print(done_task.result())  #这里返回的是一个任务，不是直接的返回值，故而需要使用result函数进行获取
 
 
loop = asyncio.get_event_loop()               
loop.run_until_complete(main())
loop.close()
```

