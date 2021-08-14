# Kotlin Started

## Basic syntax ##

### Package definition and imports ###

```kotlin
package my.demo

import kotlin.text.*

// ...
```

不需要匹配目录和包:源文件可以任意放置在文件系统中。

### Program entry point ###

```kotlin
fun main() {
    println("Hello world!")
}

fun main(args: Array<String>) {
    println(args.contentToString())
}
```

### Functions ###

```kotlin
fun sum(a: Int, b: Int): Int {
    return a + b
}

fun sum1(a: Int, b: Int) = a + b

fun printSum(a: Int, b: Int): Unit {
    println("sum of $a and $b is ${a + b}")
}
```

### Variables ###

只读局部变量使用关键字val定义，它们只能被赋值一次。

```kotlin
fun main() {
    val a: Int = 1  // immediate assignment
    val b = 2   // `Int` type is inferred
    val c: Int  // Type required when no initializer is provided
    c = 3       // deferred assignment
    println("a = $a, b = $b, c = $c")
}

fun main() {
    var x = 5 // `Int` type is inferred
    x += 1
    println("x = $x")
}
```

```kotlin
val PI = 3.14
var x = 0

fun incrementX() { 
    x += 1 
}

fun main() {
    println("x = $x; PI = $PI")
    incrementX()
    println("incrementX()")
    println("x = $x; PI = $PI")
}
```

### Creating classes and instances ###

```kotlin
open class Shape

class Rectangle(var height: Double, var length: Double) : Shape() {
    var perimeter = (height + length) * 2
}

fun main() {
    val rectangle = Rectangle(5.0, 2.0)
    println("The perimeter is ${rectangle.perimeter}")
}
```

Inheritance between classes is declared by a colon (`:`). Classes are final by default; to make a class inheritable, mark it as `open`.

### Comments ###

### Other syntax ###

```kotlin
fun main() {
    var a = 1
    // simple name in template:
    val s1 = "a is $a"

    a = 2
    // arbitrary expression in template:
    val s2 = "${s1.replace("is", "was")}, but now is $a"
    println(s2)
}

fun maxOf(a: Int, b: Int): Int {
    return if (a > b) {
        a
    } else {
        b
    }
}

fun maxOF(a: Int, b: Int) = if (a > b) a else b
```

### when expression ###

```kotlin
fun describe(obj: Any): String =
    when (obj) {
        1 -> "One"
        "Hello" -> "Greeting"
        is Long -> "Long"
        !is String -> "Not a string"
        else -> "Unknown"
    }

fun main() {
    println(describe(1))
    println(describe("Hello"))
    println(describe(1000L))
    println(describe(2))
    println(describe("other"))
}
```

### Ranges ###

```kotlin
fun main() {
    val x = 10
    val y = 9
    if (x in 1..y+1) {
        println("fits in range")
    }
}

fun main() {
    val list = listOf("a", "b", "c")

    if (-1 !in 0..list.lastIndex) {
        println("-1 is out of range")
    }
    if (list.size !in list.indices) {
        println("list size is out of valid list indices range, too")
    }
}
```

### Nullable values and null checks ###

当可能为空值时，引用必须显式标记为可空值。可空的类型名有?在最后。

```kotlin
fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}

fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

    // Using `x * y` yields error because they may hold nulls.
    if (x != null && y != null) {
        // x and y are automatically cast to non-nullable after null check
        println(x * y)
    } else {
        println("'$arg1' or '$arg2' is not a number")
    }
}

fun main() {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("a", "b")
}
```

### 类型检查和自动类型转换 ###

```kotlin
fun getStringLength(obj: Any): Int? {
    if (obj is String) {
        // `obj` is automatically cast to `String` in this branch
        return obj.length
    }

    // `obj` is still of type `Any` outside of the type-checked branch
    return null
}

fun main() {
    fun printLength(obj: Any) {
        println("Getting the length of '$obj'. Result: ${getStringLength(obj) ?: "Error: The object is not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength(1000)
    printLength(listOf(Any()))
}
```

## Idioms ##

### Create DTOs (POJOs/POCOs) ###

```kotlin
data class Customer(val name: String, val email: String)
```

- getters & setters
- equals
- hashCode
- toString
- copy
- `component1()`,  `component2()`

### 参数默认值 ###

```kotlin
fun foo(a: Int = 0, b: String = "") { ... }
```

### Filter a list ###

```kotlin
val positives = list.filter { x -> x > 0 }
val positives = list.filter { it > 0 }
```

### Instance checks ###

```kotlin
when (x) {
    is Foo -> ...
    is Bar -> ...
    else   -> ...
}
```

**字典遍历**

```kotlin
for ((k, v) in map) {
    println("$k -> $v")
}
```

**关于类的操作**

```kotlin
object Resource {
    val name = "Name"
}

abstract class MyAbstractClass {
    abstract fun doSomething()
    abstract fun sleep()
}

fun main() {
    val myObject = object : MyAbstractClass() {
        override fun doSomething() {
            // ...
        }

        override fun sleep() { // ...
        }
    }
    myObject.doSomething()
}
```

## Base Types ##

### Numbers ###

| Type  | Size (bits) | Min value                          | Max value                           |
| ----- | ----------- | ---------------------------------- | ----------------------------------- |
| Byte  | 8           | -128                               | 127                                 |
| Short | 16          | -32768                             | 32767                               |
| Int   | 32          | -2,147,483,648 (-2 31)             | 2,147,483,647 (2 31- 1)             |
| Long  | 64          | -9,223,372,036,854,775,808 (-2 63) | 9,223,372,036,854,775,807 (2 63- 1) |

#### JVM上的数字表示 ####

在JVM平台上，数字存储为基本类型:int、double等等。例外情况是当您创建一个可空的数字引用，如`Int?`或使用泛型。在这些情况下，数字被装入Java类Integer、Double等。

```kotlin
fun main() {
    val a: Int = 100
    val boxedA: Int? = a
    val anotherBoxedA: Int? = a

    val b: Int = 10000
    val boxedB: Int? = b
    val anotherBoxedB: Int? = b

    println(boxedA === anotherBoxedA) // true
    println(boxedB === anotherBoxedB) // false
}
```

## Packages and imports ##

A source file may start with a package declaration:

```kotlin
package org.example

fun printMessage() { /*...*/ }
class Message { /*...*/ }

// ...
```

### 默认导入 ###

- kotlin.*
- kotlin.annotation.*
- kotlin.collections.*
- kotlin.comparisons.*
- kotlin.io.*
- kotlin.ranges.*
- kotlin.sequences.*
- kotlin.text.*

JVM:

- java.lang.*
- kotlin.jvm.*
- kotlin.js.*

## Classes and objects ##

### classes ###

类声明由类名、类头(指定它的类型参数、主构造函数和其他东西)和用花括号括起来的类体组成。header和body都是可选的;如果类没有主体，则可以省略花括号。

#### 构造器 ####

在init块中的语句可以访问 class header中的变量。

如果class header中的变量有var val，则可以变成类的属性。

```kotlin
class Person(val firstName: String, val lastName: String, var isEmployed: Boolean = true) {
    fun changeEmploy(flag: Boolean) {
        isEmployed = flag
    }
}


class InitOrderDemo(name: String) {
    val firstProperty = "First property: $name".also(::println)

    init {
        println("First initializer block that prints $name")
    }

    val secondProperty = "Second property: ${name.length}".also(::println)

    init {
        println("Second initializer block that prints ${name.length}")
    }
}

fun main() {
    val person = Person("Tom", "Peter")
    println(person)
    InitOrderDemo("Peter")
}
```

Kotlin中的类可以有一个主构造函数和一个或多个次级构造函数。主构造函数是类头的一部分，它位于类名和可选类型参数之后。

主构造函数不能包含任何代码。初始化代码可以放在以init关键字为前缀的初始化块中。

在实例的初始化过程中，初始化器块的执行顺序与它们在类体中出现的顺序相同，并与属性初始化器穿插在一起:

```kotlin
class InitOrderDemo(name: String) {
    val firstProperty = "First property: $name".also(::println)

    init {
        println("First initializer block that prints $name")
    }

    val secondProperty = "Second property: ${name.length}".also(::println)

    init {
        println("Second initializer block that prints ${name.length}")
    }
}

class Customer(name: String) {
    val customerKey = name.uppercase()
}

class Pet {
    constructor(owner: Person) {
        owner.pets.add(this) // adds this pet to the list of its owner's pets
    }
}

fun main() {
    InitOrderDemo("hello")
}
```

#### 二级构造函数 ####

如果类有一个主构造函数，每个辅助构造函数都需要直接或间接地通过另一个辅助构造函数委托给主构造函数。对同一类的另一个构造函数的委托是使用this关键字完成的:

```kotlin
class Person(val name: String) {
    var children: MutableList<Person> = mutableListOf()
    constructor(name: String, parent: Person) : this(name) {
        parent.children.add(this)
    }
}
```

初始化块中的代码有效地成为了主构造函数的一部分。对主构造函数的委托发生在次级构造函数的第一条语句，因此所有初始化块和属性初始化器中的代码都是在次级构造函数体之前执行的。即使类没有主构造函数，委托仍然会隐式发生，初始化式块仍然会执行:

```kotlin
class Constructors {
    init {
        println("Init block")
    }

    constructor(i: Int) {
        println("Constructor $i")
    }
}

fun main() {
    Constructors(1)
}
```

### 继承 ###

Kotlin中的所有类都有一个通用的超类Any，它是没有声明超类型的类的默认超类。

默认情况下，Kotlin类是final类——它们不能被继承。要使一个类可继承，用open关键字标记它:

```kotlin
open class Base(p: Int)

class Derived(p: Int, q: Double = 0.0) : Base(p) {
    var sum = p * q
}
```

如果派生类有主构造函数，则基类可以(而且必须)根据其参数在主构造函数中初始化。

如果派生类没有主构造函数，则每个辅助构造函数都必须使用super关键字初始化基类，或者必须委托给另一个具有此功能的构造函数。

```kotlin
class MyView : View {
    constructor(ctx: Context) : super(ctx)
    constructor(ctx: Context, attrs: AttributeSet) : super(ctx, attrs)
}
```

#### 方法重载 ####

Kotlin要求可覆盖成员和覆盖的显式修饰符

```kotlin
open class Shape {
    open fun draw() { /*...*/ }
    fun fill() { /*...*/ }
}

class Circle() : Shape() {
    override fun draw() { /*...*/ }
}

open class Rectangle() : Shape() {
    // 终止重写
    final override fun draw() { /*...*/ }
}
```

#### 派生类初始化顺序 ####

在构造派生类的新实例期间，基类初始化是作为第一步完成的(在此之前只需要计算基类构造函数的参数)，这意味着它发生在派生类的初始化逻辑运行之前。

```kotlin
open class Base(val name: String) {

    init {
        println("Initializing a base class")
    }

    open val size: Int =
        name.length.also { println("Initializing size in the base class: $it") }
}

class Derived(
    name: String,
    val lastName: String,
) : Base(name.replaceFirstChar { it.uppercase() }.also { println("Argument for the base class: $it") }) {

    init {
        println("Initializing a derived class")
    }

    override val size: Int =
        (super.size + lastName.length).also { println("Initializing size in the derived class: $it") }
}

fun main() {
    println("Constructing the derived class(\"hello\", \"world\")")
    Derived("hello", "world")
}
```

这意味着在执行基类构造函数时，派生类中声明或重写的属性还没有初始化。在基类初始化逻辑中使用任何这些属性(直接或间接地通过另一个覆盖的开放成员实现)都可能导致错误行为或运行时失败。因此，在设计基类时，应该避免在构造函数、属性初始化器或init块中使用open成员。

#### 调用超类实现 ####

```kotlin
open class Rectangle {
    open fun draw() {
        println("Drawing a rectangle")
    }

    val borderColor: String get() = "black"
}

class FilledRectangle : Rectangle() {
    override fun draw() {
        super.draw()
        println("Filling the rectangle")
    }

    val fillColor: String get() = super.borderColor
}
```

### 属性 ###

属性的getter setter ：

```kotlin
var stringRepresentation: String
    get() = this.toString()
    set(value) {
        setDataFromString(value) // parses the string and assigns values to other properties
    }
```

### interfaces ###

Kotlin中的接口可以包含抽象方法的声明，以及方法实现。与抽象类不同的是，接口不能存储状态。它们可以具有属性，但这些属性需要是抽象的或提供访问器实现。

### Functional interfaces (SAM) ###

只有一个抽象方法的接口称为功能接口，或单一抽象方法(SAM)接口。函数接口可以有多个非抽象成员，但只能有一个抽象成员。

```kotlin
fun interface KRunnable {
   fun invoke()
}
```

### 访问修饰符 ###

类、对象、接口、构造函数、函数、属性和它们的setter都可以有可见性修饰符。getter总是具有与属性相同的可见性。

在Kotlin中有四种可见性修饰符:私有、受保护、内部和公共。默认可见性是公共的。

- private
- protected
- internal
- public (default)

### Data class ###

创建主要目的是保存数据的类并不少见。在这些类中，一些标准功能和一些实用函数通常可以从数据中机械地推导出来。在Kotlin中，这些被称为数据类，并用data标记:

```kotlin
data class User(val name: String, val age: Int)
```

### Sealed class ###

### inline class ###

To declare an inline class, use the `value` modifier before the name of the class:

```kotlin
value class Password(private val s: String)
```

## Functions ##

### Functions ###

### Lambdas ###

### inline functions ###

### 操作符重载 ###

```kotlin
data class Point(val x: Int, val y: Int)

operator fun Point.unaryMinus() = Point(-x, -y)

val point = Point(10, 20)

fun main() {
   println(-point)  // prints "Point(x=-10, y=-20)"
}
```

## Type-safe builders ##

## Null safety ##

### 可空类型和非空类型 ###

在Kotlin中，类型系统区分了可以保存空(可空引用)和不能保存空引用(非空引用)的引用。

```kotlin
fun main() {
    var a: String = "abc" // Regular initialization means non-null by default
    a = null // compilation error
}
fun main() {
    var b: String? = "abc" // can be set to null
    b = null // ok
    print(b)
}
```

现在，如果你调用一个方法或访问a的属性，它保证不会导致NPE

#### 检查条件是否为null ####

First, you can explicitly check whether `b` is `null`, and handle the two options separately:

```kotlin
val l = if (b != null) b.length else -1
```

#### Safe calls ####

访问可空变量的属性的第二种选择是使用安全调用操作符 `?.`

```kotlin
fun main() {
    val a = "Kotlin"
    val b: String? = null
    println(b?.length)
    println(a?.length) // Unnecessary safe call
}
```

Safe calls are useful in chains. 

