"""
The code created by Liberty on 2021/5/24

descriptor 就是任何一个定义了 __get__()，__set__() 或 __delete__() 的对象。

可选地，描述器可以具有 __set_name__() 方法。这仅在描述器需要知道创建它的类或分配给它的类变量名称时使用。
（即使该类不是描述器，只要此方法存在就会调用。）

在属性查找期间，描述器由点运算符调用。
如果使用 vars(some_class)[descriptor_name] 间接访问描述器，则返回描述器实例而不调用它。

描述器仅在用作类变量时起作用。放入实例时，它们将失效。

描述器的主要目的是提供一个挂钩，允许存储在类变量中的对象控制在属性查找期间发生的情况。


"""
import logging
import os

logging.basicConfig(level=logging.INFO)


# 动态查找
class DirectorySize:
    def __get__(self, obj, obj_type=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname


class LoggedAgeAccess:
    def __get__(self, instance, owner):
        value = instance._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, instance, value):
        logging.info('Updating %r to %r', 'age', value)
        instance._age = value


class LoggedAccess:
    def __set_name__(self, owner, name):
        logging.info('set_name: %r --> %r', owner, name)
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        value = getattr(instance, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)


class Person:
    name = LoggedAccess()  # First descriptor instance
    age = LoggedAccess()

    def __init__(self, name, age):
        self.name = name  # Regular instance attribute
        self.age = age  # Calls __set__()

    def birthday(self):
        self.age += 1  # Calls both __get__() and __set__()


if __name__ == '__main__':
    print(Person.name)
