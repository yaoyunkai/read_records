# Descriptor #

### 定义与介绍 ###

一般而言，描述器是一个包含了描述器协议中的方法的属性值。 这些方法有 `__get__()`, `__set__()` 和 `__delete__()`。 如果为某个属性定义了这些方法中的任意一个，它就可以被称为 descriptor。

属性访问的默认行为是从一个对象的字典中获取、设置或删除属性。对于实例来说，`a.x` 的查找顺序会从 `a.__dict__['x']` 开始，然后是 `type(a).__dict__['x']`，接下来依次查找 `type(a)` 的方法解析顺序（MRO）。 如果找到的值是定义了某个描述器方法的对象，则 Python 可能会重写默认行为并转而发起调用描述器方法。这具体发生在优先级链的哪个环节则要根据所定义的描述器方法及其被调用的方式来决定。

描述器是一个强大而通用的协议。 它们是属性、方法、静态方法、类方法和 super() 背后的实现机制。 它们在 Python 内部被广泛使用。 描述器简化了底层的 C 代码并为 Python 的日常程序提供了一组灵活的新工具。

### 描述器协议 ###

```python
descr.__get__(self, obj, type=None) -> value
descr.__set__(self, obj, value) -> None
descr.__delete__(self, obj) -> None
```

如果一个对象定义了 `__set__()` 或` __delete__()`，则它会被视为数据描述器。 仅定义了` __get__()` 的描述器称为非数据描述器（它们经常被用于方法，但也可以有其他用途）。

数据和非数据描述器的不同之处在于，如何计算实例字典中条目的替代值。如果实例的字典具有与数据描述器同名的条目，则数据描述器优先。如果实例的字典具有与非数据描述器同名的条目，则该字典条目优先。

### 描述器调用概述 ###

描述器可以通过 `d.__get__(obj)` 或 `desc.__get__(None, cls)` 直接调用。

但更常见的是通过属性访问自动调用描述器。

表达式 obj.x 在命名空间的链中查找``obj`` 的属性 x。如果搜索在实例 `__dict__` 之外找到描述器，则根据下面列出的优先级规则调用其 `__get__()` 方法。

调用的细节取决于 obj 是对象、类还是超类的实例。

#### 通过实例调用 ####

实例查找通过命名空间链进行扫描，数据描述器的优先级最高，其次是实例变量、非数据描述器、类变量，最后是 `__getattr__()` （如果存在的话）。

如果 `a.x` 找到了一个描述器，那么将通过 `desc.__get__(a, type(a))` 调用它。

点运算符的查找逻辑在 [`object.__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) 中。这里是一个等价的纯 Python 实现：

```python
def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = getattr(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__') or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)
```

有趣的是，属性查找不会直接调用 `object.__getattribute__()` ，点运算符和 getattr() 函数均通过辅助函数执行属性查找：

```python
def getattr_hook(obj, name):
    "Emulate slot_tp_getattr_hook() in Objects/typeobject.c"
    try:
        return obj.__getattribute__(name)
    except AttributeError:
        if not hasattr(type(obj), '__getattr__'):
            raise
    return type(obj).__getattr__(obj, name)             # __getattr__
```

因此，如果 [`__getattr__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattr__) 存在，则只要 [`__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) 引发 [`AttributeError`](https://docs.python.org/zh-cn/3.9/library/exceptions.html#AttributeError) （直接引发异常或在描述符调用中引发都一样），就会调用它。

同时，如果用户直接调用 [`object.__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) ，则 [`__getattr__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattr__) 的钩子将被绕开。

#### 通过类调用 ####

像 A.x 这样的点操作符查找的逻辑在 `type.__getattribute__()` 中。步骤与 `object.__getattribute__()` 相似，但是实例字典查找改为搜索类的 method resolution order。

如果找到了一个描述器，那么将通过 `desc.__get__(None, A)` 调用它。

完整的 C 实现可在 [Objects/typeobject.c](https://github.com/python/cpython/tree/3.9/Objects/typeobject.c) 中的 `type_getattro()` 和 `_PyType_Lookup()` 找到。

#### 通过super调用 ####

super 的点操作符查找的逻辑在 super() 返回的对象的 `__getattribute__()` 方法中。

类似 super(A, obj).m 形式的点分查找将在 `obj.__class__.__mro__` 中搜索紧接在 A 之后的基类 B，然后返回 `B.__dict__['m'].__get__(obj, A)`。如果 m 不是描述器，则直接返回其值。

完整的 C 实现可以在 [Objects/typeobject.c](https://github.com/python/cpython/tree/3.9/Objects/typeobject.c) 的 `super_getattro()` 中找到。纯 Python 等价实现可以在 [Guido's Tutorial](https://www.python.org/download/releases/2.2.3/descrintro/#cooperation) 中找到。

#### 调用逻辑总结 ####

描述器的机制嵌入在 object，type 和 super() 的 `__getattribute__()` 方法中。

- 描述器由 [`__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) 方法调用。
- 类从 [`object`](https://docs.python.org/zh-cn/3.9/library/functions.html#object)，[`type`](https://docs.python.org/zh-cn/3.9/library/functions.html#type) 或 [`super()`](https://docs.python.org/zh-cn/3.9/library/functions.html#super) 继承此机制。
- 由于描述器的逻辑在 [`__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) 中，因而重写该方法会阻止描述器的自动调用。
- [`object.__getattribute__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__getattribute__) 和 `type.__getattribute__()` 会用不同的方式调用 [`__get__()`](https://docs.python.org/zh-cn/3.9/reference/datamodel.html#object.__get__)。前一个会传入实例，也可以包括类。后一个传入的实例为 `None` ，并且总是包括类。
- 数据描述器始终会覆盖实例字典。
- 非数据描述器会被实例字典覆盖。

### Python等价实现 ###

#### property ####

该文档显示了定义托管属性 `x` 的典型用法：

```python
class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")
```

下面展示了纯python的等价实现:

```python
class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```

#### 函数和方法 ####

Python 的面向对象功能是在基于函数的环境构建的。通过使用非数据描述器，这两方面完成了无缝融合。

在调用时，存储在类词典中的函数将被转换为方法。方法与常规函数的不同之处仅在于对象实例被置于其他参数之前。方法与常规函数的不同之处仅在于第一个参数是为对象实例保留的。按照惯例，实例引用称为 *self* ，但也可以称为 *this* 或任何其他变量名称。

为了支持自动创建方法，函数包含 `__get__()` 方法以便在属性访问时绑定其为方法。这意味着函数其是非数据描述器，它在通过实例进行点查找时返回绑定方法，其运作方式如下：

```python
class Function:
    def __get__(self, obj, objtype=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return MethodType(self, obj)

class D:
    def f(self, x):
        return x

D.f.__qualname__  # D.f
D.__dict__['f']   # 通过类字典访问函数不会调用 __get__()。相反，它只返回基础函数对象
D.f               # 来自类的点运算符访问会调用 __get__()，直接返回底层的函数。

d = D()
d.f               # 有趣的行为发生在从实例进行点访问期间。点运算符查找调用 __get__()，返回绑定的方法对象
```

#### 静态方法 ####

静态方法返回底层函数，不做任何更改。调用 `c.f` 或 `C.f` 等效于通过 `object.__getattribute__(c, "f")` 或 `object.__getattribute__(C, "f")` 查找。这样该函数就可以从对象或类中进行相同的访问。

```python
class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f
```

#### 类方法 ####

与静态方法不同，类方法在调用函数之前将类引用放在参数列表的最前。无论调用方是对象还是类，此格式相同 当方法仅需要具有类引用并且确实依赖于存储在特定实例中的数据时，此行为就很有用。类方法的一种用途是创建备用类构造函数。

```python
class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        if hasattr(type(self.f), '__get__'):
            return self.f.__get__(cls)
        return MethodType(self.f, cls)
```

#### 实例对象和 `__slot__` ####

1. Provides immediate detection of bugs due to misspelled attribute assignments. Only attribute names specified in `__slots__` are allowed

2. Helps create immutable objects where descriptors manage access to private attributes stored in `__slots__`

   ```python
   class Immutable:
   
       __slots__ = ('_dept', '_name')          # Replace the instance dictionary
   
       def __init__(self, dept, name):
           self._dept = dept                   # Store to private attribute
           self._name = name                   # Store to private attribute
   
       @property                               # Read-only descriptor
       def dept(self):
           return self._dept
   
       @property
       def name(self):                         # Read-only descriptor
           return self._name
   >>> mark = Immutable('Botany', 'Mark Watney')
   >>> mark.dept
   'Botany'
   >>> mark.dept = 'Space Pirate'
   Traceback (most recent call last):
       ...
   AttributeError: can't set attribute
   >>> mark.location = 'Mars'
   Traceback (most recent call last):
       ...
   AttributeError: 'Immutable' object has no attribute 'location'
   ```

3. save memory.

要创建一个一模一样的纯 Python 版的 `__slots__` 是不可能的，因为它需要直接访问 C 结构体并控制对象内存分配。 但是，我们可以构建一个非常相似的模拟版，其中作为 slot 的实际 C 结构体由一个私有的 `_slotvalues` 列表来模拟。 对该私有结构体的读写操作将由成员描述器来管理：

```python
null = object()

class Member:

    def __init__(self, name, clsname, offset):
        'Emulate PyMemberDef in Include/structmember.h'
        # Also see descr_new() in Objects/descrobject.c
        self.name = name
        self.clsname = clsname
        self.offset = offset

    def __get__(self, obj, objtype=None):
        'Emulate member_get() in Objects/descrobject.c'
        # Also see PyMember_GetOne() in Python/structmember.c
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        return value

    def __set__(self, obj, value):
        'Emulate member_set() in Objects/descrobject.c'
        obj._slotvalues[self.offset] = value

    def __delete__(self, obj):
        'Emulate member_delete() in Objects/descrobject.c'
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        obj._slotvalues[self.offset] = null

    def __repr__(self):
        'Emulate member_repr() in Objects/descrobject.c'
        return f'<Member {self.name!r} of {self.clsname!r}>'

# type.__new__() 方法负责将成员对象添加到类变量：
class Type(type):
    'Simulate how the type metaclass adds member objects for slots'

    def __new__(mcls, clsname, bases, mapping):
        'Emuluate type_new() in Objects/typeobject.c'
        # type_new() calls PyTypeReady() which calls add_methods()
        slot_names = mapping.get('slot_names', [])
        for offset, name in enumerate(slot_names):
            mapping[name] = Member(name, clsname, offset)
        return type.__new__(mcls, clsname, bases, mapping)

# object.__new__() 方法负责创建具有 slot 而非实例字典的实例。 以下是一个纯 Python 的粗略模拟版：
class Object:
    'Simulate how object.__new__() allocates memory for __slots__'

    def __new__(cls, *args):
        'Emulate object_new() in Objects/typeobject.c'
        inst = super().__new__(cls)
        if hasattr(cls, 'slot_names'):
            empty_slots = [null] * len(cls.slot_names)
            object.__setattr__(inst, '_slotvalues', empty_slots)
        return inst

    def __setattr__(self, name, value):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{type(self).__name__!r} object has no attribute {name!r}'
            )
        super().__setattr__(name, value)

    def __delattr__(self, name):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{type(self).__name__!r} object has no attribute {name!r}'
            )
        super().__delattr__(name)
```

