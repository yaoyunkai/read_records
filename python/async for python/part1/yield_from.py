"""
RESULT = yield from EXPR


"""

"""
_i = iter(EXPR)  # EXPR 可以是任何可迭代的对象
try:
    _y = next(_i)  # 预激子生成器；结果保存在 _y 中，作为产出的第一个值。
except StopIteration as _e:
    _r = _e.value  # 如果抛出 StopIteration 异常，获取异常对象的 value 属性，赋值给 _r
else:
    while True:  # 运行这个循环时，委派生成器会阻塞，只作为调用方和子生成器之间的通道。
        _s = yield _y  # 产出子生成器当前产出的元素；等待调用方发送 _s 中保存的值。
        try:
            _y = _i.send(_s)  # 尝试让子生成器向前执行，转发调用方发送的 _s。
        except StopIteration as _e:
            _r = _e.value  # 如果子生成器抛出 StopIteration 异常，获取 value 属性的值，赋值给 _r，然后退出循环，让委派生成器恢复运行。
            break
RESULT = _r  # 返回的结果（RESULT）是 _r，即整个 yield from 表达式的值。
"""

"""
_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while True:
        try:
            _s = yield _y
        except GeneratorExit as _e:  # 这一部分用于关闭委派生成器和子生成器。因为子生成器可以是任何可迭代的对象，所以可能没有 close 方法。
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
        except BaseException as _e:  # 这一部分处理调用方通过 .throw(...) 方法传入的异常。
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r
"""


#
#   Here is a binary tree that produces an inorder traversal
#   of its items when iterated over. (Courtesy of Scott Dial)
#

class BinaryTree:
    def __init__(self, left=None, us=None, right=None):
        self.left = left
        self.us = us
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        if self.us:
            yield self.us
        if self.right:
            yield from self.right


#
#   For comparison, here is the same thing using for-loops
#   instead of yield-from.
#

class BinaryTreeForLoop:
    def __init__(self, left=None, us=None, right=None):
        self.left = left
        self.us = us
        self.right = right

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        if self.us:
            yield self.us
        if self.right:
            for node in self.right:
                yield node
