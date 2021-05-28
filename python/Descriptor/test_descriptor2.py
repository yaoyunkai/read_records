"""
The code created by Liberty on 2021/5/24

覆盖类属性描述符
非覆盖类属性描述符 通过是否有 __set__ 区分

advice：
a, 只读描述符必须有 __set__ 方法
只读属性的 __set__ 方法只需抛出 AttributeError 异常，并提供合适的错误消息

b, 用于验证的描述符可以只有 __set__ 方法
如果有效，使用描述符实例的名称为键，直接在实例的__dict__ 属性中设置。
这样，从实例中读取同名属性的速度很快，因为不用经过 __get__ 方法处理

c, 仅有 __get__ 方法的描述符可以实现高效缓存
如果只编写了 __get__ 方法，那么创建的是非覆盖型描述符.
这种描述符可用于执行某些耗费资源的计算，然后为实例设置同名属性，缓存结果。
同名实例属性会遮盖描述符，因此后续访问会直接从实例的 __dict__ 属性中获取值，而不会再触发描述符的 __get__ 方法。

参考链接：
https://docs.python.org/zh-cn/3.9/howto/descriptor.html


"""
import collections


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(_obj):
    cls = type(_obj)
    if cls is type:
        return '<class {}>'.format(_obj.__name__)
    elif cls in [type(None), int]:
        return repr(_obj)
    else:
        return '<{} object>'.format(cls_name(_obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


# =============================== 方法是非覆盖属性描述符 ===============================


class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]


if __name__ == '__main__':
    obj = Managed()

    """
    
    obj.over
    Managed.over
    obj.over = 7
    obj.over
    obj.__dict__['over'] = 8
    print(vars(obj))
    obj.over
    """

    """
    # 描述符没有 __get__ 因此实例直接从类中获取属性, 那么就是描述符本身
    print(obj.over_no_get)
    print(Managed.over_no_get)
    obj.over_no_get = 7
    print(obj.over_no_get)
    obj.__dict__['over_no_get'] = 9
    obj.over_no_get = 7
    print(obj.over_no_get)
    """

    """
    obj.non_over
    obj.non_over = 7
    print(obj.non_over)

    Managed.non_over
    del obj.non_over
    obj.non_over
    """

    word = Text('forward')  # Text 实例的 repr 方法返回一个类似 Text 构造方法调用的字符串，可用于创建相同的实例。
    print(word.reverse())
    Text.reverse(Text('backward'))  # 在类上调用方法相当于调用函数。
    print(type(Text.reverse), type(word.reverse))  # 注意类型是不同的，一个是 function，一个是 method。

    # Text.reverse 相当于函数，甚至可以处理 Text 实例之外的其他对象。
    print(list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])))

    # 函数都是非覆盖型描述符。在函数上调用 __get__ 方法时传入实
    # 例，得到的是绑定到那个实例上的方法。
    print(Text.reverse.__get__(word))

    # 调用函数的 __get__ 方法时，如果 instance 参数的值是 None，那
    # 么得到的是函数本身。
    print(Text.reverse.__get__(None, Text))

    # word.reverse 表达式其实会调用
    # Text.reverse.__get__(word)，返回对应的绑定方法。
    print(word.reverse)

    # 绑定方法对象有个 __self__ 属性，其值是调用这个方法的实例引用。
    print(word.reverse.__self__)

    # 绑定方法的 __func__ 属性是依附在托管类上那个原始函数的引用。
    print(word.reverse.__func__ is Text.reverse)
