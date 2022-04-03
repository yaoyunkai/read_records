### Yield From 的使用方法 ###

1 - yield from 可用于简化 for 循环中的 yield 表达式。

2 - 用作委托生成器使用，用于调用方和子生成器的管道。

#### 1. 用法1的demo ####

```python
def chain(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))

def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

list(gen())
```

#### 2. 用法2的demo ####

```python
# BEGIN YIELD_FROM_AVERAGER
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # <1>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # <4>


# the delegating generator
def grouper(results, key):  # <5>
    while True:  # <6>
        results[key] = yield from averager()  # <7>


# the client code, a.k.a. the caller
def main(data):  # <8>
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # <9>
        next(group)  # <10>
        for value in values:
            group.send(value)  # <11>
        group.send(None)  # important! <12>

    print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


if __name__ == '__main__':
    data123 = {
        'girls;kg':
            [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m':
            [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg':
            [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m':
            [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
    }
    main(data123)
```

#### yield from的意义 ####

- 子生成器产出的值直接传给委派生成器的调用方。
- 使用 `send()` 发给委派生成器的值都直接传给子生成器。如果发送的值是 None，那么会调用子生成器的 `__next__()` 方法。如果发送的值不是 None，那么会调用子生成器的 send() 方法。如果调用的方法抛出 StopIteration 异常，那么委派生成器恢复运行。任何其他异常都会向上冒泡，传给委派生成器。
- 生成器退出时，生成器（或子生成器）中的 return expr 表达式会触发 StopIteration(expr) 异常抛出。
- yield from 表达式的值是子生成器终止时传给 StopIteration 异常的第一个参数。

简化的 yield from的运行原理： `RESULT = yield from EXPR`

```python
_i = iter(EXPR)  # <1>
try:
	_y = next(_i)  # <2>
except StopIteration as _e:
	_r = _e.value  # <3>
else:
    while 1:  # <4>
    	_s = yield _y  # <5>
    	try:
    		_y = _i.send(_s)  # <6>
    	except StopIteration as _e:  # <7>
    		_r = _e.value
    		break
RESULT = _r  # <8>
```

- 1: XPR 可以是任何可迭代的对象，因为获取迭代器 _i（这是子生成器）使用的是 iter() 函数。
- 2: 预激子生成器；结果保存在 _y 中，作为产出的第一个值。
- 3: 如果抛出 StopIteration 异常，获取异常对象的 value 属性，赋值给 _r——这是最简单情况下的返回值（RESULT）。
- 4: 运行这个循环时，委派生成器会阻塞，只作为调用方和子生成器之间的通道。
- 5: 产出子生成器当前产出的元素；等待调用方发送 _s 中保存的值。注意，这个代码清单中只有这一个 yield 表达式。
- 6: 尝试让子生成器向前执行，转发调用方发送的 _s。
- 7: 如果子生成器抛出 StopIteration 异常，获取 value 属性的值，赋值给 _r，然后退出循环，让委派生成器恢复运行。
- 8: 返回的结果（RESULT）是 _r，即整个 yield from 表达式的值。

伪代码使用的变量:

_i（迭代器）
　　子生成器

_y（产出的值）
　　子生成器产出的值

_r（结果）
　　最终的结果（即子生成器运行结束后 yield from 表达式的值）

_s（发送的值）
　　调用方发给委派生成器的值，这个值会转发给子生成器

_e（异常）
　　异常对象（在这段简化的伪代码中始终是 StopIteration 实例）

