# JavaScript 高级编程v4 #

## 1. what is javascript ##

### 1.1 简短的历史回顾 ###

1995 年，网景公司一位名叫 Brendan Eich 的工程师，开始为即将发布的 Netscape Navigator 2 开发一个叫 Mocha（后来改名为 LiveScript）的脚本语言。当时的计划是在客户端和服务器端都使用它，它在服务器端叫 LiveWire。

为了赶上发布时间，网景与 Sun 公司结为开发联盟，共同完成 LiveScript 的开发。就在 Netscape Navigator 2正式发布前，网景把 LiveScript改名为 JavaScript，以便搭上媒体当时热烈炒作 Java的顺风车。

微软的 JavaScript 实现意味着出现了两个版本的 JavaScript：Netscape Navigator 中的 JavaScript，以及 IE 中的 JScript。

### 1.2 JavaScript实现 ###

虽然JavaScript和ECMAScript基本上是同义词，但JavaScript远远不限于ECMA-262所定义的那样。
没错，完整的 JavaScript 实现包含以下几个部分：

- 核心 ECMAScript
- 文档对象模型DOM
- 浏览器对象模型BOM

![image-20210707211253673](.assets/image-20210707211253673.png)

## 2 HTML中的JavaScript ##

### 2.1 `<script>` 元素 ###

该元素有以下的属性：

- async 可选。表示应该立即开始下载脚本，但不能阻止其他页面动作，比如下载资源或等待其他脚本加载。只对外部脚本文件有效。
- charset 可选。使用 src 属性指定的代码字符集。这个属性很少使用，因为大多数浏览器不在乎它的值。
- crossorigin 可选。配置相关请求的CORS（跨源资源共享）设置。默认不使用CORS。
- defer 可选。表示脚本可以延迟到文档完全被解析和显示之后再执行。只对外部脚本文件有效。
- integrity 可选。允许比对接收到的资源和指定的加密签名以验证子资源完整性（SRI，Subresource Integrity）。
- language 废弃。最初用于表示代码块中的脚本语言
- src 可选。表示包含要执行的代码的外部文件。
- type 可选。代替 language ，表示代码块中脚本语言的内容类型（也称 MIME 类型）。按照惯
  例，这个值始终都是 "text/javascript" 。

两种使用方式：通过它直接在网页中嵌入 JavaScript 代码，以及通过它在网页中包含外部 JavaScript 文件。

不管包含的是什么代码，浏览器都会按照 <script> 在页面中出现的顺序依次解释它们，前提是它们没有使用 defer 和 async 属性。第二个 <script> 元素的代码必须在第一个 <script> 元素的代码解释完毕才能开始解释，第三个则必须等第二个解释完，以此类推。

#### 2.1.1 标签位置 ####

现代 Web 应用程序通常将所有 JavaScript 引用放在 <body> 元素中的页面内容后面，如下面的例子所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<!-- 这里是页面内容 -->
<script src="example1.js"></script>
<script src="example2.js"></script>
</body>
</html>
```

#### 2.1.2 推迟执行脚本 ####

defer: 脚本会被延迟到整个页面都解析完毕后再运行,相当于告诉浏览器立即下载，但延迟执行。

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Example HTML Page</title>
		<script defer src="example1.js"></script>
		<script defer src="example2.js"></script>
	</head>
	<body>
	<!-- 这里是页面内容 -->
	</body>
</html>
```

HTML5 规范要求脚本应该按照它们出现的顺序执行，因此第一个推迟的脚本会在第二个推迟的脚本之前执行，而且两者都会在 DOMContentLoaded 事件之前执行

#### 2.1.3 异步执行脚本 ####

async: 告诉浏览器，不必等脚本下载和执行完后再加载页面，同样也不必等到该异步脚本下载和执行后再加载其他脚本。正因为如此，异步脚本不应该在加载期间修改 DOM。

异步脚本保证会在页面的 load 事件前执行，但可能会在 DOMContentLoaded （参见第 17 章）之前或之后。

## 3 语法基础 ##

### 3.1 语法 ###

#### 3.1.1 区分大小写 ####

#### 3.1.2 标识符 ####

所谓标识符，就是变量、函数、属性或函数参数的名称。标识符可以由一或多个下列字符组成：

- 第一个字符必须是一个字母、下划线（ _ ）或美元符号（ $ ）；
- 剩下的其他字符可以是字母、下划线、美元符号或数字。

标识符中的字母可以是扩展 ASCII（Extended ASCII）中的字母，也可以是 Unicode 的字母字符，

ECMAScript 标识符使用驼峰大小写形式，

#### 3.1.4 严格模式 ####

`"use strict"`

#### 3.1.5 语句 ####

ECMAScript 中的语句以分号结尾。省略分号意味着由解析器确定语句在哪里结尾，

### 3.2 关键字和保留字 ###

ECMA-262 描述了一组保留的关键字，这些关键字有特殊用途，比如表示控制语句的开始和结束，
或者执行特定的操作。按照规定，保留的关键字不能用作标识符或属性名。

![image-20210707214033086](.assets/image-20210707214033086.png)

### 3.3 变量 ###

ECMAScript 变量是松散类型的，意思是变量可以用于保存任何类型的数据。每个变量只不过是一个用于保存任意值的命名占位符。有 3 个关键字可以声明变量： var 、 const 和 let 。其中， var 在ECMAScript 的所有版本中都可以使用，而 const 和 let 只能在 ECMAScript 6及更晚的版本中使用。

#### 3.3.1 var ####

```javascript
// 不初始化的情况下，变量会保存一个特殊值 undefined
var message;
var message = "hi";
```

**1. var声明作用域**

使用 var 操作符定义的变量会成为包含它的函数的局部变量。

```javascript
function test() {
    var s2 = "hello";
}
test();
console.log(s2); // meet error
```

不过，在函数内定义变量时省略 var 操作符，可以创建一个全局变量：

```javascript
function test2() {
    s3 = "nihao";
}
test2();
console.log(s3);
```

**2. var声明提升**

使用这个关键字声明的变量会自动提升到函数作用域顶部：

```javascript
function foo() {
    console.log(age);
    var age = 23;
}

foo();
```

之所以不会报错，是因为 ECMAScript 运行时把它看成等价于如下代码：

```javascript
function foo1() {
    var age1;
    console.log(age1);
    age1 = 23;
}

foo1();
```

这就是所谓的“提升”（hoist），也就是把所有变量声明都拉到函数作用域的顶部。此外，反复多次使用 var 声明同一个变量也没有问题.

#### 3.3.2 let ####

let 跟 var 的作用差不多，但有着非常重要的区别。最明显的区别是， let 声明的范围是块作用域，而 var 声明的范围是函数作用域。

```js
if (true) {
    var name = 'Tom';
    console.log(name);
}
console.log(name);

if (true) {
    let age = 23;
    console.log(age);
}
console.log(age); // meet error
```

let 也不允许同一个块作用域中出现冗余声明。这样会导致报错.

对声明冗余报错不会因混用 let 和 var 而受影响。这两个关键字声明的并不是不同类型的变量，它们只是指出变量在相关作用域如何存在。

```js
var name;
let name; // SyntaxError
let age;
var age; // SyntaxError
```

**1. 暂时性死区**

```js
// name 会被提升
console.log(name); // undefined
var name = 'Matt';

// age 不会被提升
console.log(age); // ReferenceError：age 没有定义
let age = 26;
```

**2. 全局声明**

与 var 关键字不同，使用 let 在全局作用域中声明的变量不会成为 window 对象的属性（ var 声明的变量则会）。

```js
var name = 'Matt';
console.log(window.name); // 'Matt'

let age = 26;
console.log(window.age); // undefined
```

**3. 条件声明**

在使用 var 声明变量时，由于声明会被提升，JavaScript 引擎会自动将多余的声明在作用域顶部合并为一个声明。

因为 let 的作用域是块，所以不可能检查前面是否已经使用 let 声明过同名变量，同时也就不可能在没有声明的情况下声明它。

```html
<script>
var name = 'Nicholas';
let age = 26;
</script>

<script>
// 假设脚本不确定页面中是否已经声明了同名变量
// 那它可以假设还没有声明过
var name = 'Matt';
// 这里没问题，因为可以被作为一个提升声明来处理
// 不需要检查之前是否声明过同名变量
let age = 36;
// 如果 age 之前声明过，这里会报错
</script>
```

使用 try / catch 语句或 typeof 操作符也不能解决，因为条件块中 let 声明的作用域仅限于该块。

```js
// script1
let name = 'Nicholas';
let age = 36;

// script2
if (typeof name === 'undefined') {
    let name;
}

name = 'Matt';

try {
    console.log(age);
} catch (error) {
    let age;
}

age = 26;

```

**4. for 循环中的let声明**

在 let 出现之前， for 循环定义的迭代变量会渗透到循环体外部：

```js
for (var i = 0; i < 5; ++i) {
	// 循环逻辑
}
console.log(i); // 5
```

改成使用 let 之后，这个问题就消失了，因为迭代变量的作用域仅限于 for 循环块内部：

```js
for (let i = 0; i < 5; ++i) {
	// 循环逻辑
}
console.log(i); // ReferenceError: i 没有定义
```

在使用 var 的时候，最常见的问题就是对迭代变量的奇特声明和修改：

```js
for (var i = 0; i < 5; ++i) {
	setTimeout(() => console.log(i), 0)
}
// 你可能以为会输出 0、1、2、3、4
// 实际上会输出 5、5、5、5、5
```

#### 3.3.3 const ####

const 的行为与 let 基本相同，唯一一个重要的区别是用它声明变量时必须同时初始化变量，且尝试修改 const 声明的变量会导致运行时错误。

```js
const age = 23;
age = 36 // TypeError: 给常量赋值

// const 也不允许重复声明
const name = 'Matt';
const name = 'Nicholas'; // SyntaxError

// const 声明的作用域也是块
const name = 'Matt';
if (true) {
	const name = 'Nicholas';
}
console.log(name); // Matt
```

const 声明的限制只适用于它指向的变量的引用。换句话说，如果 const 变量引用的是一个对象，那么修改这个对象内部的属性并不违反 const 的限制。

```js
const person = {};
person.name = 'Matt'; // ok
```

### 3.4 数据类型 ###

ECMAScript 有 6 种简单数据类型（也称为原始类型）： Undefined 、 Null 、 Boolean 、 Number 、String 和 Symbol 。 Symbol （符号）是 ECMAScript 6 新增的。还有一种复杂数据类型叫 Object （对象）。

#### 3.4.1 typeof 操作符 ####

对一个值使用 typeof 操作符会返回下列字符串之一：

- undefined 值未定义
- boolean
- string
- number
- object
- function
- symbol 表示值为符号。

#### 3.4.2 undefined 类型 ####

Undefined 类型只有一个值，就是特殊值 undefined 。当使用 var 或 let 声明了变量但没有初始化时，就相当于给变量赋予了 undefined 值：

```js
let msg1;
console.log(msg1 == undefined);
```

包含 undefined 值的变量跟未定义变量是有区别的。请看下面的例子：

```js
let message; // 这个变量被声明了，只是值为 undefined
// 确保没有声明过这个变量
// let age
console.log(message); // "undefined"
console.log(age); // 报错
```

在对未初始化的变量调用 typeof 时，返回的结果是 "undefined" ，但对未声明的变量调用它时，返回的结果还是 "undefined" ，

#### 3.4.3 Null类型 ####

Null 类型同样只有一个值，即特殊值 null 。逻辑上讲， null 值表示一个空对象指针，这也是给typeof 传一个 null 会返回 "object" 的原因：

```js
let car = null;
console.log(typeof car); // "object"
```

#### 3.4.4 Boolean类型 ####

Boolean （布尔值）类型是 ECMAScript 中使用最频繁的类型之一，有两个字面值： true 和 false 。这两个布尔值不同于数值，因此 true 不等于 1， false 不等于 0。

虽然布尔值只有两个，但所有其他 ECMAScript 类型的值都有相应布尔值的等价形式。要将一个其他类型的值转换为布尔值，可以调用特定的 Boolean() 转型函数：

```js
let message = "Hello world!";
let messageAsBoolean = Boolean(message);
```

| 数据类型  | 转换为true的值 | 转换为false的值 |
| --------- | -------------- | --------------- |
| Boolean   | true           | false           |
| String    | 非空字符串     | ""              |
| Number    | 非零数值       | 0 NaN           |
| Object    | 任意对象       | null            |
| Undefined | N/A            | undefined       |

理解以上转换非常重要，因为像 if 等流控制语句会自动执行其他类型值到布尔值的转换。

#### 3.4.5 Number类型 ####

 Number 类型使用 IEEE 754格式表示整数和浮点值

**2. 值的范围**

ECMAScript 可以表示的最小数值保存在 Number.MIN_VALUE 中。

可以表示的最大数值保存在Number.MAX_VALUE 中。

任何无法表示的负数以 -Infinity （负无穷大）表示，任何无法表示的正数以 Infinity （正无穷大）表示。

要确定一个值是不是有限大（即介于 JavaScript 能表示的最小值和最大值之间），可以使用 isFinite() 函数，

**3. NaN**

有一个特殊的数值叫 NaN ，意思是“不是数值”（Not a Number），用于表示本来要返回数值的操作失败了（而不是抛出错误）。比如，用 0 除任意数值在其他语言中通常都会导致错误，从而中止代码执行。

```js
console.log(0/0); // NaN
console.log(-0/+0); // NaN

console.log(5/0); // Infinity
console.log(5/-0); // -Infinity
```

首先，任何涉及 NaN 的操作始终返回 NaN （如 NaN/10 ），在连续多步计算时这可能是个问题。其次， NaN 不等于包括 NaN 在内的任何值。

为此，ECMAScript 提供了 isNaN() 函数。该函数接收一个参数，可以是任意数据类型，然后判断这个参数是否“不是数值”。

```js
console.log(isNaN(NaN)); // true
console.log(isNaN(10)); // false，10 是数值
console.log(isNaN("10")); // false，可以转换为数值 10
console.log(isNaN("blue")); // true，不可以转换为数值
console.log(isNaN(true)); // false，可以转换为数值 1
```

**4. 数值转换**

有 3 个函数可以将非数值转换为数值： Number() 、 parseInt() 和 parseFloat() 。 Number() 是转型函数，可用于任何数据类型。后两个函数主要用于将字符串转换为数值。

`Number()` 函数的转换规则：

- 布尔值， true 转换为 1， false 转换为 0。
- 数值，直接返回
- null ，返回 0。
- undefined ，返回 NaN 。
- 字符串：
  - 如果字符串包含数值字符，包括数值字符前面带加、减号的情况，则转换为一个十进制数值。
  - 如果字符串包含有效的浮点值格式如 "1.1" ，则会转换为相应的浮点值（同样，忽略前面的零）。
  - 如果字符串包含有效的十六进制格式如 "0xf" ，则会转换为与该十六进制值对应的十进制整数值。
  - 如果是空字符串（不包含字符），则返回 0。
  - 如果字符串包含除上述情况之外的其他字符，则返回 NaN 。
- 对象，调用 valueOf() 方法，并按照上述规则转换返回的值。

#### 3.4.6 String类型 ####

String （字符串）数据类型表示零或多个 16 位 Unicode 字符序列。字符串可以使用双引号（"）、单引号（'）或反引号（`）标示。

**3. 转换为字符串**

有两种方式把一个值转换为字符串。首先是使用几乎所有值都有的 toString() 方法。这个方法唯一的用途就是返回当前值的字符串等价物。

**4. 模板字面量**

反引号。

**5. 字符串插值**

模板字面量最常用的一个特性是支持字符串插值，也就是可以在一个连续定义中插入一个或多个值。技术上讲，模板字面量不是字符串，而是一种特殊的 JavaScript 句法表达式，只不过求值后得到的是字符串。模板字面量在定义时立即求值并转换为字符串实例，任何插入的变量也会从它们最接近的作用域中取值。

字符串插值通过在 `${}` 中使用一个 JavaScript 表达式实现。

```js
let value = 5;
let exponent = 'second';
let interpolatedString = `${value} to the ${exponent} power is ${value * value}`;
console.log(interpolatedString);
```

**6. 模板字面量标签函数**

模板字面量也支持定义标签函数（tag function），而通过标签函数可以自定义插值行为。标签函数会接收被插值记号分隔后的模板和对每个表达式求值的结果。

标签函数本身是一个常规函数，通过前缀到模板字面量来应用自定义行为，如下例所示。标签函数接收到的参数依次是原始字符串数组和对每个表达式求值的结果。这个函数的返回值是对模板字面量求值得到的字符串。

```js
function simpleTag(strings, aValExpression, bValExpression, sumExpression) {
    console.log(strings);
    console.log(aValExpression);
    console.log(bValExpression);
    console.log(sumExpression);

    return "foobar";
}
let untaggedResult = `${ a } + ${ b } = ${ a + b }`;
let taggedResult = simpleTag`${ a } + ${ b } = ${ a + b }`;

function simpleTag1(strings, ...expressions) {
    console.log(strings);
    for (const expression of expressions) {
        console.log(expression);
    }
    return 'foobar';
}
```

#### 3.4.7 Symbol类型 ####

符号是原始值，且符号实例是唯一、不可变的。符号的用途是确保对象属性使用唯一标识符，不会发生属性冲突的危险。

**1. 符号的基本用法**

符号需要使用 Symbol() 函数初始化。因为符号本身是原始类型，所以 typeof 操作符对符号返回symbol 。

```js
let sym = Symbol();
console.log(typeof sym);
```

调用 Symbol() 函数时，也可以传入一个字符串参数作为对符号的描述（description），将来可以通过这个字符串来调试代码。但是，这个字符串参数与符号定义或标识完全无关：

```js
let genericSymbol = Symbol();
let otherGenericSymbol = Symbol();

let fooSymbol = Symbol('foo');
let otherFooSymbol = Symbol('foo');
console.log(genericSymbol == otherGenericSymbol);
console.log(fooSymbol == otherFooSymbol);
```

 Symbol() 函数不能与 new 关键字一起作为构造函数使用。这样做是为了避免创建符号包装对象。

```js
let myBool = new Boolean();
console.log(typeof myBool);

let myStr = new String();
console.log(typeof myStr);

let myNum = new Number();
console.log(typeof myNum);

// let mySymbol = new Symbol(); // Uncaught TypeError: Symbol is not a constructor

// 如果你确实想使用符号包装对象，可以借用 Object() 函数：
let mySymbol = Symbol();
let myWrappedSymbol = Object(mySymbol);
console.log(typeof myWrappedSymbol); // "object"

```

**2. 使用全局符号注册表**

`Symbol.for()` 对每个字符串键都执行幂等操作。第一次使用某个字符串调用时，它会检查全局运行时注册表，发现不存在对应的符号，于是就会生成一个新符号实例并添加到注册表中。后续使用相同字符串的调用同样会检查注册表，发现存在与该字符串对应的符号，然后就会返回该符号实例。

```js
let fooGlobalSymbol = Symbol.for('foo'); // 创建新符号
let otherFooGlobalSymbol = Symbol.for('foo'); // 重用已有符号
console.log(fooGlobalSymbol === otherFooGlobalSymbol); // true
```

即使采用相同的符号描述，在全局注册表中定义的符号跟使用 Symbol() 定义的符号也并不等同：

```js
let localSym = Symbol('foo')
let globalSym = Symbol.for('foo')
localSym === globalSym // false

Symbol.keyFor(globalSym) // foo
```

**3. 使用符号作为属性**

凡是可以使用字符串或数值作为属性的地方，都可以使用符号。这就包括了对象字面量属性和`Object.defineProperty()` / `Object.defineProperties()` 定义的属性。对象字面量只能在计算属性语法中使用符号作为属性。

```js
let s1 = Symbol('foo'),
    s2 = Symbol('bar'),
    s3 = Symbol('baz'),
    s4 = Symbol('qux');

let o = {
    [s1]: 'foo val'
}
console.log(o);

Object.defineProperty(o, s2, {value: 'bar val'});
console.log(o);

Object.defineProperties(o, {
    [s3]: {value: 'baz val'},
    [s4]: {value: 'qux val'}
});
console.log(o);
```

类似于 `Object.getOwnPropertyNames()` 返回对象实例的常规属性数组， `Object.getOwnPropertySymbols()`返回对象实例的符号属性数组。这两个方法的返回值彼此互斥。 `Object.getOwnPropertyDescriptors()` 会返回同时包含常规和符号属性描述符的对象。 `Reflect.ownKeys()` 会返回两种类型的键。

```js
let s1 = Symbol('foo');
let s2 = Symbol('bar');

let o = {
[s1]: 'foo val',
[s2]: 'bar val',
baz: 'baz val',
qux: 'qux val'
};
console.log(o);

console.log(Object.getOwnPropertySymbols(o));
console.log(Object.getOwnPropertyNames(o));
console.log(Object.getOwnPropertyDescriptors(o));
console.log(Reflect.ownKeys(o));
```

因为符号属性是对内存中符号的一个引用，所以直接创建并用作属性的符号不会丢失。但是，如果没有显式地保存对这些属性的引用，那么必须遍历对象的所有符号属性才能找到相应的属性键：

```js
let o = {
[Symbol('foo')]: 'foo val',
[Symbol('bar')]: 'bar val'
}
console.log(o);

let barSymbol = Object.getOwnPropertySymbols(o).find((symbol) => symbol.toString().match(/bar/));
console.log(barSymbol);
```

**4. 常用内置符号**

#### 3.4.8 Object类型 ####

ECMAScript 中的对象其实就是一组数据和功能的集合。对象通过 new 操作符后跟对象类型的名称来创建。开发者可以通过创建 Object 类型的实例来创建自己的对象，然后再给对象添加属性和方法：

```js
let o = new Object()
```

这个语法类似 Java，但 ECMAScript 只要求在给构造函数提供参数时使用括号。如果没有参数，如上面的例子所示，那么完全可以省略括号（不推荐）：

```js
let o = new Object; // 合法，但不推荐
```

ECMAScript中的 Object 也是派生其他对象的基类。 Object 类型的所有属性和方法在派生的对象上同样存在。

每个 Object 实例都有如下属性和方法:

- constructor
- hasOwnProperty(propertyName) 用于判断当前对象实例（不是原型）上是否存在给定的属性。
- isPrototypeOf(object) ：用于判断当前对象是否为另一个对象的原型。
- propertyIsEnumerable(propertyName) ：用于判断给定的属性是否可以使用（本章稍后讨论的） for-in 语句枚举。
- toLocaleString() ：返回对象的字符串表示，该字符串反映对象所在的本地化执行环境
- toString() ：返回对象的字符串表示。
- valueOf() ：返回对象对应的字符串、数值或布尔值表示。

### 3.5 操作符 ###

#### 3.5.2 位操作符 ####

接下来要介绍的操作符用于数值的底层操作，也就是操作内存中表示数据的比特（位）。ECMAScript中的所有数值都以 IEEE 754 64 位格式存储，但位操作并不直接应用到 64 位表示，而是先把值转换为32 位整数，再进行位操作，之后再把结果转换为 64 位。

**1. 按位非**

```js
let num1 = 25; // 二进制 00000000000000000000000000011001
let num2 = ~num1; // 二进制 11111111111111111111111111100110
console.log(num2); // -26
```

**2. 按位与**

```js
let result = 25 & 3;
console.log(result); // 1
```

**3. 按位或**

```js
let result = 25 | 3;
console.log(result); // 27
```

**4. 按位异或**

```js
let result = 25 ^ 3;
console.log(result); // 26
```

左移：`<<`

有符号右移： `>>`

无符号右移: `>>>`

#### 3.5.3 布尔操作符 ####

#### 3.5.7 关系操作符 ####

关系操作符执行比较两个值的操作，包括小于（ < ）、大于（ > ）、小于等于（ <= ）和大于等于（ >= ），用法跟数学课上学的一样。这几个操作符都返回布尔值。

与 ECMAScript中的其他操作符一样，在将它们应用到不同数据类型时也会发生类型转换和其他行为。

- 如果操作数都是数值，则执行数值比较。
- 如果操作数都是字符串，则逐个比较字符串中对应字符的编码。
- 如果有任一操作数是数值，则将另一个操作数转换为数值，执行数值比较。
- 如果有任一操作数是对象，则调用其 valueOf() 方法，取得结果后再根据前面的规则执行比较
- 如果没有 valueOf() 操作符，则调用 toString() 方法，取得结果后再根据前面的规则执行比较。
- 如果有任一操作数是布尔值，则将其转换为数值再执行比较。

#### 3.5.8 相等操作符 ####

提供了两组操作符。第一组是等于和不等于，它们在比较之前执行转换。第二组是全等和不全等，它们在比较之前不执行转换。

**1. 等于和不等于**

ECMAScript 中的等于操作符用两个等于号（ == ）表示，如果操作数相等，则会返回 true 。不等于操作符用叹号和等于号（ != ）表示，如果两个操作数不相等，则会返回 true 。这两个操作符都会先进行类型转换（通常称为强制类型转换）再确定操作数是否相等。

- 如果任一操作数是布尔值，则将其转换为数值再比较是否相等。 false 转换为 0， true 转换为 1。
-  如果一个操作数是字符串，另一个操作数是数值，则尝试将字符串转换为数值，再比较是否相等。
- 如果一个操作数是对象，另一个操作数不是，则调用对象的 valueOf() 方法取得其原始值，再根据前面的规则进行比较。

在进行比较时，这两个操作符会遵循如下规则。

- null 和 undefined 相等。
- null 和 undefined 不能转换为其他类型的值再进行比较。
- 如果有任一操作数是 NaN ，则相等操作符返回 false ，不相等操作符返回 true 。
- 如果两个操作数都是对象，则比较它们是不是同一个对象。如果两个操作数都指向同一个对象，则相等操作符返回 true 。

**2. 全等和不全等**

全等和不全等操作符与相等和不相等操作符类似，只不过它们在比较相等时不转换操作数。全等操作符由 3 个等于号（ === ）表示，只有两个操作数在不转换的前提下相等才返回 true 

不全等操作符用一个叹号和两个等于号（ !== ）表示，只有两个操作数在不转换的前提下不相等才返回 true 。

### 3.6 语句 ###

## 4. 变量 作用域和内存 ##

### 4.1 原始值和引用值 ###

在把一个值赋给变量时，JavaScript 引擎必须确定这个值是原始值还是引用值。上一章讨论了 6 种原始值： Undefined 、 Null 、 Boolean 、 Number 、 String 和 Symbol 。保存原始值的变量是按值（by value）访问的，因为我们操作的就是存储在变量中的实际值。

#### 4.1.1 动态属性 ####

原始类型的初始化可以只使用原始字面量形式。如果使用的是 new 关键字，则 JavaScript 会创建一个 Object 类型的实例，但其行为类似原始值。

```js
let name1 = "Tom";
let name2 = new String("Bob");
name1.age = 27;
name2.age = 26;

console.log(name1.age); // undefined
console.log(name2.age); // 26
console.log(typeof name1); // string
console.log(typeof name2); // object
```

#### 4.1.2 复制值 ####

#### 4.1.3 传递参数 ####

按值传递的方式

#### 4.1.4 确定类型 ####

 typeof 操作符最适合用来判断一个变量是否为原始类型。它是判断一个变量是否为字符串、数值、布尔值或 undefined 的最好方式。

```js
let s = "Nicholas";
let b = true;
let i = 22;
let u;
let n = null;
let o = new Object();

console.log(typeof s); // string
console.log(typeof i); // number
console.log(typeof b); // boolean
console.log(typeof u); // undefined
console.log(typeof n); // object
console.log(typeof o); // object
```

### 4.2 执行上下文与作用域 ###

每个上下文都有一个关联的变量对象（variable object），而这个上下文中定义的所有变量和函数都存在于这个对象上。虽然无法通过代码访问变量对象，但后台处理数据会用到它。

全局上下文是最外层的上下文。根据 ECMAScript实现的宿主环境，表示全局上下文的对象可能不一样。在浏览器中，全局上下文就是我们常说的 window 对象。

因此所有通过 var 定义的全局变量和函数都会成为 window 对象的属性和方法。

上下文中的代码在执行的时候，会创建变量对象的一个作用域链（scope chain）。这个作用域链决定了各级上下文中的代码在访问变量和函数时的顺序。代码正在执行的上下文的变量对象始终位于作用域链的最前端。如果上下文是函数，则其活动对象（activation object）用作变量对象。

```js
var color = "blue";

function changeColor() {
    if (color === 'blue') {
        color = 'red';  // 相当于一个全局变量
    } else {
        color = 'blue';
    }
}

changeColor();
console.log(color);  // red
```

```js
var color = 'blue';

function changeColor() {
    let anotherColor = 'red';
    function swapColors() {
        let tmpColor = anotherColor;
        anotherColor = color;  // 全局 但是应该会被 let 抑制
        color = tmpColor;  // 全局
        demo = '123'
    }
    swapColors();
}
changeColor();
console.log(color);
// console.log(anotherColor);
console.log(demo);
```

 `swapColors()`局部上下文的作用域链中有 3 个对象： swapColors() 的变量对象、 changeColor() 的变量对象和全局变量对象。

#### 4.2.1 作用域链增强 ####

#### 4.2.2 变量声明 ####

**1. 使用var的函数作用域声明**

**2. 使用let的块级作用域声明**

### 4.3 垃圾回收 ###

## 5 基本引用类型 ##

### 5.2 RegExp ###

`let expression = /pattern/flags;`

- g ：全局模式，表示查找字符串的全部内容，而不是找到第一个匹配的内容就结束。
- i ：不区分大小写，表示在查找匹配时忽略 pattern 和字符串的大小写。
- m ：多行模式，表示查找到一行文本末尾时会继续查找。
- y ：粘附模式，表示只查找从 lastIndex 开始及之后的字符串。
- u ：Unicode 模式，启用 Unicode 匹配。
- s ： dotAll 模式，表示元字符 . 匹配任何字符（包括 \n 或 \r ）。

#### 5.2.1 RegExp 实例属性 ####

```js
let pattern1 = /[bc]at/i;
console.log(pattern1.global); // false
console.log(pattern1.ignoreCase); // true
console.log(pattern1.multiline); // false
console.log(pattern1.lastIndex); // 0
console.log(pattern1.source); // "\[bc\]at"
console.log(pattern1.flags); // "i"
```

### 5.4 单例内置对象 ###

#### 5.4.1 Global ####

在全局作用域中定义的变量和函数都会变成 Global 对象的属性 。

虽然 ECMA-262 没有规定直接访问 Global 对象的方式，但浏览器将 window 对象实现为 Global对象的代理。因此，所有全局作用域中声明的变量和函数都变成了 window 的属性。

#### 5.4.2 Math ####

## 6 集合引用类型 ##

### 6.1 Object ###

显式地创建 Object 的实例有两种方式。

```js
let person = new Object();
person.name = "Nicholas";
person.age = 29;

let person = {
	name: "Nicholas",
	age: 29
};
```

### 6.2 Array ###

### 6.3 typed array ###

## 7 迭代器和生成器 ##

## 8 面向对象 ##

### 8.1 理解对象 ###

```js
let person = new Object();
person.name = "Nicholas";
person.age = 29;
person.job = "Software Engineer";

// console.log(this) // 表示全局的window对象

person.sayName = function () {
    console.log(this.name);
};

let person1 = {
    name: "Nicholas",
    age: 29,
    job: "Software Engineer",
    sayName() {
        console.log(this.name);
    }
};
```

#### 8.1.1 属性的类型 ####

