# Use Celery #

<img src=".assets/celery_512.png" alt="Logo" style="zoom:33%;" />

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

celery必须在使用前实例化，这个实例称为应用程序(或简称app)。

该应用程序是线程安全的，因此具有不同配置、组件和任务的多个Celery应用程序可以在同一个进程空间中共存。

#### Main Name ####

其中只有一个是重要的，那就是主模块名。让我们看看为什么会这样。

在Celery中发送任务消息时，该消息不会包含任何源代码，而只包含要执行的任务的名称。这类似于主机名在互联网上的工作方式:每个工作者维护一个任务名到其实际功能的映射，称为任务注册表。

```python
In [2]: from celery import Celery

In [3]: app = Celery()

In [4]: app
Out[4]: <Celery __main__ at 0x7f7a77ddc1f0>

In [5]: @app.task
   ...: def add(x, y):
   ...:     return x + y
   ...: 

In [6]: add
Out[6]: <@task: __main__.add of __main__ at 0x7f7a77ddc1f0>
```

当你定义一个任务时，这个任务也会被添加到本地注册表中:

```python
In [9]: app.tasks
Out[9]: 
{'__main__.add': <@task: __main__.add of __main__ at 0x7f7a77ddc1f0>,
 'celery.chain': <@task: celery.chain of __main__ at 0x7f7a77ddc1f0>,
 'celery.backend_cleanup': <@task: celery.backend_cleanup of __main__ at 0x7f7a77ddc1f0>,
 'celery.starmap': <@task: celery.starmap of __main__ at 0x7f7a77ddc1f0>,
 'celery.chord': <@task: celery.chord of __main__ at 0x7f7a77ddc1f0>,
 'celery.accumulate': <@task: celery.accumulate of __main__ at 0x7f7a77ddc1f0>,
 'celery.chunks': <@task: celery.chunks of __main__ at 0x7f7a77ddc1f0>,
 'celery.chord_unlock': <@task: celery.chord_unlock of __main__ at 0x7f7a77ddc1f0>,
 'celery.group': <@task: celery.group of __main__ at 0x7f7a77ddc1f0>,
 'celery.map': <@task: celery.map of __main__ at 0x7f7a77ddc1f0>}

In [10]: type(app.tasks)
Out[10]: celery.app.registry.TaskRegistry

In [11]: type(add)
Out[11]: celery.local.PromiseProxy

In [12]: app.tasks['__main__.add']
Out[12]: <@task: __main__.add of __main__ at 0x7f7a77ddc1f0>

```

每当celery不能检测到函数属于哪个模块时，它就使用main module来生成任务名的开头。

1. If the module that the task is defined in is run as a program.
1. If the application is created in the Python shell (REPL).

#### Configuration ####

```python
In [14]: type(app.conf)
Out[14]: celery.app.utils.Settings

```

两种方式来更新app的配置：

```python
>>> app.conf.enable_utc = True

>>> app.conf.update(
...     enable_utc=True,
...     timezone='Europe/London',
...)
```

配置对象由多个字典组成，这些字典按顺序被查询:

1. changes made at run-time
2. The configuration module (if any)
3. The default configuration ([`celery.app.defaults`](https://docs.celeryproject.org/en/latest/reference/celery.app.defaults.html#module-celery.app.defaults)).

你甚至可以使用app.add_defaults()方法添加新的默认源。

**config_from_object**

The [`app.config_from_object()`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.config_from_object) method loads configuration from a configuration object.

这可以是一个配置模块，或者任何具有配置属性的对象。

请注意，在调用config_from_object()时，之前设置的任何配置都将被重置。如果您想要设置额外的配置，您应该在这之后这样做。

list the examples below:

```python
# 1. The app.config_from_object() method can take the fully qualified name of a Python module, or even the name of a Python attribute, for example: "celeryconfig", "myproj.config.celery", or "myproj.config:CeleryConfig":
from celery import Celery
app = Celery()
app.config_from_object('celeryconfig')

# 2. pass an already imported module object
import celeryconfig
from celery import Celery
app = Celery()
app.config_from_object(celeryconfig)

# 3. Using a configuration class/object
from celery import Celery
app = Celery()
class Config:
    enable_utc = True
    timezone = 'Europe/London'
app.config_from_object(Config)

# 4. from env variables
import os
from celery import Celery
os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')
app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')
```

**Censored configuration**

如果您希望打印配置，作为调试信息或类似信息，您可能还希望过滤掉密码和API密钥等敏感信息。

以字符的形式输出：`app.conf.humanize(with_defaults=False, censored=True)`

以字典的形式输出：`app.conf.table(with_defaults=False, censored=True)`

#### Laziness ####

应用程序实例是惰性的，这意味着它在实际需要时才会被执行。

Creating a [`Celery`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery) instance will only do the following:

- Create a logical clock instance, used for events.
- Create the task registry.
- Set itself as the current app (but not if the `set_as_current` argument was disabled)
- Call the [`app.on_init()`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.on_init) callback (does nothing by default).

The [`app.task()`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.task) decorators don’t create the tasks at the point when the task is defined, instead it’ll defer the creation of the task to happen either when the task is used, or after the application has been *finalized*,

```python
In [1]: from celery import Celery

In [2]: app = Celery()

In [3]: @app.task
   ...: def add(x, y):
   ...:     return x + y
   ...: 

In [4]: type(add)
Out[4]: celery.local.PromiseProxy

In [5]: add.__evaluated__()
Out[5]: True

```

*Finalization* of the app happens either explicitly by calling [`app.finalize()`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.finalize)  or implicitly by accessing the `app.tasks` attribute.

Finalizing the object will:

- Copy tasks that must be shared between apps
- Evaluate all pending task decorators.
- Make sure all tasks are bound to the current app.

#### Breaking the chain ####

虽然它可能依赖于当前正在设置的应用程序，但最佳实践是始终将应用程序实例传递给任何需要它的东西。

我称之为“应用程序链”，因为它根据被传递的应用程序创建了一个实例链。

```python
# The following example is considered bad practice:
from celery import current_app

class Scheduler:

    def run(self):
        app = current_app
        
# Instead it should take the app as an argument:
class Scheduler:

    def __init__(self, app):
        self.app = app
```

Internally Celery uses the [`celery.app.app_or_default()`](https://docs.celeryproject.org/en/latest/reference/celery.app.html#celery.app.app_or_default) function so that everything also works in the module-based compatibility API

```python
from celery.app import app_or_default

class Scheduler:
    def __init__(self, app=None):
        self.app = app_or_default(app)
```

#### Abstract Tasks ####

All tasks created using the [`task()`](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.task) decorator will inherit from the application’s base [`Task`](https://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task) class.

You can specify a different base class using the `base` argument:

```python
@app.task(base=OtherTask):
def add(x, y):
    return x + y
```

To create a custom task class you should inherit from the neutral base class: `celery.Task`

```python
from celery import Task

class DebugTask(Task):

    def __call__(self, *args, **kwargs):
        print('TASK STARTING: {0.name}[{0.request.id}]'.format(self))
        return self.run(*args, **kwargs)
```

It’s even possible to change the default base class for an application by changing its [`app.Task()`](https://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task) attribute:

```python
>>> from celery import Celery, Task

>>> app = Celery()

>>> class MyBaseTask(Task):
...    queue = 'hipri'

>>> app.Task = MyBaseTask
>>> app.Task
<unbound MyBaseTask>

>>> @app.task
... def add(x, y):
...     return x + y

>>> add
<@task: __main__.add>

>>> add.__class__.mro()
[<class add of <Celery __main__:0x1012b4410>>,
 <unbound MyBaseTask>,
 <unbound Task>,
 <type 'object'>]
```

### Tasks ###

