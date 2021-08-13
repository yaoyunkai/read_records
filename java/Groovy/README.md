# Groovy #

## Syntax ##

### 注释 ###

```groovy
// a standalone single line comment
println "hello" // a comment till the end of the line
```

```groovy
/* a standalone multiline comment
   spanning two lines */
println "hello" /* a multiline comment starting
                   at the end of a statement */
println 1 /* one */ + 2 /* two */
```

### Keywords ###

The following list represents all the keywords of the Groovy language:

```
as assert break case
catch class const continue
def default do else
enum extends false finally
for goto if implements
import in instanceof interface
new null package return
super swtich this throw
throws trait ture try
var while

// trait var
```

### 标识符 ###

引号标识符：

```groovy
def map = [:]
map."an identifier with a space and double quotes" = "ALLOWED"
map.'with-dash-signs-and-single-quotes' = "ALLOWED"
assert map."an identifier with a space and double quotes" == "ALLOWED"
assert map.'with-dash-signs-and-single-quotes' == "ALLOWED"

def firstname = "Homer"
map."Simpson-${firstname}" = "Homer Simpson"
assert map.'Simpson-Homer' == "Homer Simpson"
```

### Strings ###

GStrings: `groovy.lang.GString` 插值字符串。

`String#stripIndent()`

`String#stripMargin()`

```groovy
def name = 'Guillaume' // a plain string
def greeting = "Hello ${name}"
assert greeting.toString() == 'Hello Guillaume'

def sum = "The sum of 2 and 3 equals ${2 + 3}"
assert sum.toString() == 'The sum of 2 and 3 equals 5'
```

**Characters**

```groovy
char c1 = 'A' 
assert c1 instanceof Character

def c2 = 'B' as char 
assert c2 instanceof Character

def c3 = (char)'C' 
assert c3 instanceof Character
```

### Numbers ###

Groovy支持不同类型的整型和十进制字面值，由Java的常用Number类型支持。

- byte
- char
- short
- int
- long
- java.lang.BigInteger

```groovy
// primitive types
byte  b = 1
char  c = 2
short s = 3
int   i = 4
long  l = 5

// infinite precision
BigInteger bi =  6
```

如果您通过使用def关键字使用可选类型，整数值的类型将会变化:它将适应容纳该数值的类型的容量。

### Booleans ###

```groovy
def myBooleanVariable = true
boolean untypedBooleanVar = false
booleanField = true
```

此外，Groovy还有一些特殊的规则(通常称为Groovy Truth)，用于将非布尔对象强制转换为布尔值。

### Lists ###

Groovy使用逗号分隔的值列表，用方括号括起来，表示列表.

Groovy列表是纯JDK java.util.List

默认情况下，定义列表字面值时使用的具体列表实现是java.util.ArrayList，除非您决定另外指定，我们将在后面看到。

```groovy
def numbers = [1, "234", 4, 5]
println(numbers)
```

在as操作符中使用类型强制，或者为变量使用显式类型声明:

```groovy
def arrayList = [1, 2, 3]
def linkedList = [2, 3, 4] as LinkedList
LinkedList otherLinked = [3, 4, 5]
```

在Groovy中列表还支持：下标取值和 `<<` 操作符

```groovy
def letters = ['a', 'b', 'c', 'd']

assert letters[0] == 'a'
assert letters[1] == 'b'

assert letters[-1] == 'd'
assert letters[-2] == 'c'

letters[2] = 'C'
assert letters[2] == 'C'

letters << 'e'
assert letters[ 4] == 'e'
assert letters[-1] == 'e'

assert letters[1, 3] == ['b', 'd']
assert letters[2..4] == ['C', 'd', 'e']  
```

### Arrays ###

Groovy重用数组的列表表示法，但是要使这种字面量数组成为数组，您需要通过强制或类型声明显式地定义数组的类型。

```groovy
String[] arrStr = ['Ananas', 'Banana', 'Kiwi']

assert arrStr instanceof String[]
assert !(arrStr instanceof List)

def numArr = [1, 2, 3] as int[]

assert numArr instanceof int[]
assert numArr.size() == 3
```

```groovy
def primes = new int[]{1, 2, 3, 4}
println(primes.size())
println(primes.sum())
println(primes.class.name)

def pets = new String[]{'cat', 'dog'}
assert pets.size() == 2 && pets.sum() == 'catdog'
assert pets.class.name == '[Ljava.lang.String;'

// traditional Groovy alternative still supported
String[] groovyBooks = ['Groovy in Action', 'Making Java Groovy']
assert groovyBooks.every { it.contains('Groovy') }
```

### Maps ###

Groovy的特性是映射，在其他语言中有时被称为字典或关联数组。映射将键关联到值，用冒号分隔键和值，每个键/值对用逗号，整个键和值用方括号包围。

```groovy
def colors = [red: '#FF0000', green: '#00FF00', blue: '#0000FF']

assert colors['red'] == '#FF0000'
assert colors.green  == '#00FF00'

colors['pink'] = '#FF00FF'
colors.yellow  = '#FFFF00'

assert colors.pink == '#FF00FF'
assert colors['yellow'] == '#FFFF00'
```

## Operators ##

### Conditional operators ###

**Elvis operator**

这样做很方便的一个例子是，当表达式解析为假值时，返回一个“合理的默认值”

```groovy
def user = [:]
displayName = user.name ?: "Anonymous"
```

### Object operators ###

#### Safe navigation operator ####

The Safe Navigation operator is used to avoid a `NullPointerException`. 

```groovy
def person = Person.find { it.id == 123 }    
def name = person?.name                      
assert name == null   
```

#### Direct field access operator ####

```groovy
class User {
    public final String name
    User(String name) {
        this.name = name
    }
    String getName() {
        "Name: ${name}"
    }
}

def user = new User('Bob')
user.name == 'Name: Bob'
```

user.name调用会触发对同名属性的调用，也就是说，这里是对name的getter。如果你想要检索字段而不是调用getter，你可以使用直接字段访问操作符:

```groovy
assert user.@name == 'Bob'   
```

#### Method pointer operator ####

方法指针操作符(.&)可用于将方法的引用存储在变量中，以便以后调用:

```groovy
def str = 'example of method reference'
def fun = str.&toUpperCase
def upper = fun()
println(upper)
```

There are multiple advantages in using method pointers. First of all, the type of such a method pointer is a `groovy.lang.Closure`, so it can be used in any place a closure would be used. In particular, it is suitable to convert an existing method for the needs of the strategy pattern:

```groovy
def transform(List elements, Closure action) {
    def result = []
    elements.each {
        result << action(it)
    }
    result
}

class Person {
    public name
    public age
}

String describe(Person p) {
    "$p.name is $p.age"
}

def action = this.&describe
def list = [
        new Person(name: 'Bob', age: 42),
        new Person(name: 'Julia', age: 35)]
//assert transform(list, action) == ['Bob is 42', 'Julia is 35']

println(transform(list, action))
```

方法指针由接收方和方法名绑定。参数是在运行时解析的，这意味着如果你有多个同名的方法，语法没有什么不同，只有要调用的适当方法的解析会在运行时完成:

```groovy
def doSomething(String str) { str.toUpperCase() }    
def doSomething(Integer x) { 2*x }                   
def reference = this.&doSomething                    
assert reference('foo') == 'FOO'                     
assert reference(123)   == 246       
```

### 正则表达式 ###

```groovy
def p = ~/foo/
assert p instanceof Pattern
```

### Other operators ###

#### Spread operator ####

扩展点操作符(`*.`)，通常简称为扩展操作符，用于对聚合对象的所有项调用操作。这相当于在每个项目上调用动作，并将结果收集到一个列表中:

```groovy
class Car {
    String make
    String model
}
def cars = [
       new Car(make: 'Peugeot', model: '508'),
       new Car(make: 'Renault', model: 'Clio')]       
def makes = cars*.make                                
assert makes == ['Peugeot', 'Renault']   
```

The spread operator can be used on any class which implements the `Iterable` interface:

```groovy
class Component {
    Long id
    String name
}
class CompositeObject implements Iterable<Component> {
    def components = [
        new Component(id: 1, name: 'Foo'),
        new Component(id: 2, name: 'Bar')]

    @Override
    Iterator<Component> iterator() {
        components.iterator()
    }
}
def composite = new CompositeObject()
assert composite*.id == [1,2]
assert composite*.name == ['Foo','Bar']
```

#### Range operator ####

Groovy支持范围的概念，并提供了一个符号(`..`)来创建对象的范围:

```groovy
def range = 0..5                                    
assert (0..5).collect() == [0, 1, 2, 3, 4, 5]       
assert (0..<5).collect() == [0, 1, 2, 3, 4]         
assert (0..5) instanceof List                       
assert (0..5).size() == 6  
```

