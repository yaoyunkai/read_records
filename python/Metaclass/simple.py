"""
The code created by Liberty on 2021/5/25

"""


class BaseClass(type):
    def __init__(cls, name, bases, attrs):
        print('BaseClass __init__: ', end=' ')
        print(cls, end=' ')
        print(name, end=' ')
        print(bases, end=' ')
        print(attrs)
        # cls: Class
        # name: Class.__name__
        # bases: Class Parent class
        # class_dict: attrs
        super().__init__(name, bases, attrs)

    def __new__(mcs, name, bases, attrs):
        print('BaseClass __new__:', end=' ')
        print(mcs, end=' ')
        print(name, end=' ')
        print(bases, end=' ')
        print(attrs)
        super_new = super().__new__
        new_class = super_new(mcs, name, bases, attrs)
        return new_class

    def __call__(cls, *args, **kwargs):
        print('BaseClass __call__: ', end=' ')
        print(args, end=' ')
        print(kwargs)
        super().__call__(*args, **kwargs)


class Foo(object, metaclass=BaseClass):

    def __new__(cls, *args, **kwargs):
        print('Foo __new__: ', end='')
        print(args, end=' ')
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    f = Foo(1, 3, a=12, b=34)
