# Use Celery #

![Logo](.assets/celery_512.png)

> rabbitmq 架构

![img](.assets/20190802194242348.png)

![img](.assets/20190802175911116.png)

## First Steps with Celery ##

- Choosing and installing a message transport (broker).
- Installing Celery and creating your first task.
- Starting the worker and calling tasks.
- Keeping track of tasks as they transition through different states, and inspecting return values.

### Choose a Broker ###

- RabbitMQ
- Redis
- Other brokers

### Application ###

```python
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
```

第一个参数：name of the current module.

第二个参数 broker: 指定要使用的消息代理的URL

**how to run celery**

```console
$ celery -A tasks worker --loglevel=INFO
```

**how to get help**

```console
$ celery worker --help
$ celery --help
```

### Calling the task ###

To call our task you can use the [`delay()`](https://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task.delay) method.

This is a handy shortcut to the [`apply_async()`](https://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task.apply_async) method that gives greater control of the task execution (see [Calling Tasks](https://docs.celeryproject.org/en/latest/userguide/calling.html#guide-calling)):

```python
>>> from tasks import add
>>> 
>>> add.delay(4,4)
<AsyncResult: 5ebd82d3-25df-47c1-8ef8-e5483e7fdbb2>
>>> 
```

调用一个任务将返回一个 [`AsyncResult`](https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult) 实例。这可以用来检查任务的状态，等待任务完成，或者获取它的返回值(或者如果任务失败，获取异常和回溯)。

### Keeping Results ###

choose a backend like: Django ORM, MongoDB, Memcached, Redis, RPC(RabbitMQ/AMQP)

```python
app = Celery('tasks', backend='rpc://', broker='pyamqp://')
```

```python
>>> from tasks import add
>>> 
>>> result = add.delay(4,5)
>>> result.ready()
True
>>> result.get(timeout=1)
9
```

The [`ready()`](https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult.ready) method returns whether the task has finished processing or not.

In case the task raised an exception, [`get()`](https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult.get) will re-raise the exception, but you can override this by specifying the `propagate` argument.

### Configuration ###

As an example you can configure the default serializer used for serializing task payloads by changing the [`task_serializer`](https://docs.celeryproject.org/en/latest/userguide/configuration.html#std-setting-task_serializer) setting:

```python
app.conf.task_serializer = 'json'
```

Also, we can use this way to define a app:

```python
app.config_from_object('celeryconfig')
```

For a complete reference of configuration options, see [Configuration and defaults](https://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration).

为了演示配置文件的威力，下面是你如何将一个行为不正常的任务路由到一个专用队列:

```python
# celeryconfig.py

task_routes = {
    'tasks.add': 'low-priority',
}

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}
```

If you’re using RabbitMQ or Redis as the broker then you can also direct the workers to set a new rate limit for the task at runtime:

```python
$ celery -A tasks control rate_limit tasks.add 10/m
worker@example.com: OK
    new rate limit set successfully
```

## Next Steps ##

### Should use modularization  ###

Project layout:

```console
proj/__init__.py
    /celery.py
    /tasks.py
```

```python
# celery.py

from celery import Celery

app = Celery('proj',
             broker='amqp://',
             backend='rpc://',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
```

When the worker starts you should see a banner and some messages:

```console
celery -A part2 worker --loglevel=INFO
(venv) liberty@local1:~/PycharmProjects/start_celery/code$ celery -A part2 worker --loglevel=INFO
 
 -------------- celery@local1 v5.1.2 (sun-harmonics)
--- ***** ----- 
-- ******* ---- Linux-5.8.0-53-generic-x86_64-with-glibc2.29 2021-06-29 22:13:33
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         part2:0x7f8a9fc277c0
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     redis://localhost/
- *** --- * --- .> concurrency: 6 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . part2.tasks.add
  . part2.tasks.mul
  . part2.tasks.xsum


```

- Event: 一个选项，使Celery发送监视消息(事件)，以监视工作者中发生的操作。
- Queues: worker将从中使用任务的队列列表。可以告诉工作者同时从多个队列中消费，这用于将消息路由到特定的工作者，作为服务质量、关注点分离和优先级划分的手段，所有这些都在Routing Guide中描述了。

### Background ###

In production you’ll want to run the worker in the background, described in detail in the [daemonization tutorial](https://docs.celeryproject.org/en/latest/userguide/daemonizing.html#daemonizing).

The daemonization scripts uses the **celery multi** command to start one or more workers in the background:

```console
$ celery multi start w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Starting nodes...
    > w1.halcyon.local: OK

$ celery  multi restart w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64024
> Waiting for 1 node.....
    > w1.halcyon.local: OK
> Restarting node w1.halcyon.local: OK
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64052

$ celery multi stop w1 -A proj -l INFO
```

默认情况下，它将在当前目录中创建pid和日志文件。为了防止多个worker在一个之上启动，你应该把它们放在一个专用目录中:

```python
$ mkdir -p /var/run/celery
$ mkdir -p /var/log/celery
$ celery multi start w1 -A proj -l INFO --pidfile=/var/run/celery/%n.pid \
                                        --logfile=/var/log/celery/%n%I.log
```

### celery命令的参数-A (--app) ###

定义使用的Celery app: `module.path:attribute`

或者使用这种形式：`--app=proj`

1. an attribute named `proj.app`, or
2. an attribute named `proj.celery`, or
3. any attribute in the module `proj` where the value is a Celery application, or

If none of these are found it’ll try a submodule named `proj.celery`:

1. an attribute named `proj.celery.app`, or
2. an attribute named `proj.celery.celery`, or
3. Any attribute in the module `proj.celery` where the value is a Celery application.

### calling tasks ###

可以使用delay():

```python
>>> from proj.tasks import add

>>> add.delay(2, 2)
```

这个方法实际上是另一个名为apply_async()的方法的星型参数快捷方式:

`>>> add.apply_async((2, 2))`

后者允许您指定执行选项，如运行时间(倒计时)，它应该发送到的队列，等等:

```python
>>> add.apply_async((2, 2), queue='lopri', countdown=10)
```

在上面的示例中，任务将被发送到一个名为lopri的队列，并且任务最早将在消息发送10秒后执行。

直接应用该任务将执行当前进程中的任务，因此不会发送任何消息:

```python
>>> add(2, 2)
4
```

These three methods - `delay()`, `apply_async()`, and applying (`__call__`), make up the Celery calling API, which is also used for signatures.

A more detailed overview of the Calling API can be found in the [Calling User Guide](https://docs.celeryproject.org/en/latest/userguide/calling.html#guide-calling).

每个任务调用都将得到一个惟一的标识符(UUID)——这就是任务id。

```python
>>> res = add.delay(2, 2)
>>> res.get(timeout=1)
4

>>> res.id
d6b3aea2-fb9b-4ebc-8da4-848818db9114
```

那么它如何知道任务是否失败了呢?它可以通过查看任务状态来发现:

```python
>>> res.state
'FAILURE'
```

### Canvas: Designing workflow ###

You just learned how to call a task using the tasks `delay` method, and this is often all you need. But sometimes you may want to pass the signature of a task invocation to another process or as an argument to another function, for which Celery uses something called *signatures*.

A signature wraps the arguments and execution options of a single task invocation in such a way that it can be passed to functions or even serialized and sent across the wire.

```python
>>> from part2.tasks import add
>>> 
>>> add.signature((2,5), countdown=10)
part2.tasks.add(2, 5)
>>> add.s(2,2)
part2.tasks.add(2, 2)
>>> s = add.s(2,4)
>>> res = s.delay()
>>> res.get()
6
```

**signature 可以使用 Primitives**

group
chain
chord
map
starmap
chunks

#### Group ####

A [`group`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.group) calls a list of tasks in parallel, and it returns a special result instance that lets you inspect the results as a group, and retrieve the return values in order.

```python
>>> from part2.tasks import add
>>> from celery import group
>>> 
>>> group(add.s(i, i) for i in range(10))().get()
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```

#### Chains ####

Tasks can be linked together so that after one task returns the other is called:

```python
>>> from celery import chain
>>> from part2.tasks import add, mul
>>> chain(add.s(4, 4) | mul.s(8))().get()
64

```

### Routing ###

支持AMQP提供的所有路由工具，但它也支持简单路由，将消息发送到指定队列。

The [`task_routes`](https://docs.celeryproject.org/en/latest/userguide/configuration.html#std-setting-task_routes) setting enables you to route tasks by name and keep everything centralized in one location:

```python
app.conf.update(
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)
```

### Remote Control ###

- celery inspect
- celery control
- celery status

## User Guide ##

### Application ###

### Tasks ###

