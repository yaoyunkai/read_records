# Lua Reference Manual #

作为一种扩展语言，Lua没有“主”程序的概念:它嵌入在主机客户机中工作，称为嵌入程序或简单地称为主机。(通常，这个主机是独立的lua程序。)宿主程序可以调用函数来执行一段Lua代码，可以编写和读取Lua变量，可以注册C函数来被Lua代码调用。通过C函数的使用，Lua可以被扩充以处理广泛的不同领域，从而创建共享语法框架的定制编程语言。

## 1 - Introduction ##

## 2 - The language ##

### 2.1 - Lexical Conventions ###

Lua中的名称(也称为标识符)可以是由字母、数字和下划线组成的任意字符串，而不是以数字开头。这与大多数语言中名称的定义一致。(字母的定义取决于当前区域设置:任何被当前区域设置认为是字母的字符都可以在标识符中使用。)标识符用于命名变量和表字段。

keywords:

```
     and       break     do        else      elseif
     end       false     for       function  if
     in        local     nil       not       or
     repeat    return    then      true      until     while
```

按照约定，以下划线开头，后跟大写字母的名称(如_VERSION)保留给Lua使用的内部全局变量。

下面的字符串表示其他符号:

```
     +     -     *     /     %     ^     #
     ==    ~=    <=    >=    <     >     =
     (     )     {     }     [     ]
     ;     :     ,     .     ..    ...
```

字面值字符串可以由匹配的单引号或双引号分隔，并且可以包含以下类似c的转义序列

### 2.2 - Values and Types ###

Lua是一种动态类型语言。这意味着变量没有类型;只值。该语言中没有类型定义。所有值都有自己的类型。

There are eight basic types in Lua: *nil*, *boolean*, *number*, *string*, *function*, *userdata*, *thread*, and *table*.

Tables, functions, threads, and (full) userdata values are *objects*: 变量实际上并不包含这些值，只是对它们的引用。赋值、参数传递和函数返回总是操作对这些值的引用;这些操作并不意味着任何类型的复制。

### 2.3 - Variables ###

变量是存储值的地方。Lua中有三种变量:全局变量、局部变量和表字段。

单个名称可以表示全局变量或局部变量(或函数的形参，它是一种特定的局部变量):

```
var ::= Name
```

任何变量都被假定为全局变量，除非显式地声明为局部变量.局部变量具有词法作用域:局部变量可以由定义在其作用域内的函数自由访问

