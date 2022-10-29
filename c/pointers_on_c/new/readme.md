# Pointers On C #

## 2. 基本概念 ##

### 2.1 环境 ###

**编译和链接**

`cc`命令的使用

### 2.2 词法规则 ###

#### 2.2.1 字符 ####

三字母词 trigrph 

```c
printf("Delete file (are you really sure??): ");
```

字符转义：

- `\?` 在多个问号时使用，防止被解释为三字母词
- `\"` 用于表示一个字符串常量内部的双引号
- `\a` 警告字符
- `\b` 退格符
- `\f` 进纸字符
- `\ddd` 表示1-3个八进制数字
- `\xddd` 表示16进制数

#### 2.2.2 注释 ####

#### 2.2.4 标识符 ####

由大小写字母，数字和下划线组成，但不能以数字开头。

## 3. 数据 ##

变量的三个属性 —— 作用域，链接属性和存储类型。

### 3.1 基本数据类型 ###

4种基本数据类型——整型，浮点型，指针和聚合类型(数组和结构)

#### 3.1.1 整型家族 ####

包括字符，短整型，整型和长整型，分为有符号和无符号两种版本。

长整型至少应该和整型一样长，整型至少应该和短整型一样长。

| 类型               | 最小范围                |
| ------------------ | ----------------------- |
| char               | 0到127                  |
| signed char        | -127 到 127             |
| unsigned char      | 0到255                  |
| short int          | -32767到32767           |
| unsigned short int | 0到65535                |
| int                | -32767到32767           |
| unsigned int       | 0到65535                |
| long int           | -2147483647到2147483647 |
| unsigned long int  | 0到4294967295           |

short int 至少16位，long int 至少32位。至于缺省的int的位数由编译器设计者决定。

头文件 `limits.h` 说明了各种不同的整型类型的特点。

分别说明了有符号和无符号整型的范围：

`{type}_MIN` `{type}_MAX` `U{type}_MAX`

char的目的是存放字符型值，但本质上是小整数。缺省的char可能有符号的也有可能是无符号的。所以这里就涉及到可移植性的问题，最佳妥协方案就是把存储于char型变量的值限制在有符号和无符号的交集内。

**一、整型字面值**

字面量 literal 。

当一个程序内出现整型字面值时，它属于整型家族中哪一种类型？取决于字面值是如何书写的。

- 可以通过字面值后面加 `L` `U` 改变解释的类型
- 十进制表示法
- 八进制表示法 ：以0开头
- 十六进制表示法 ：以0x开头
- 字符常量，他们的类型总是int：用一个单引号包围起来的单个字符。

**二、枚举类型**

枚举类型：它的值为符号常量而不是字面值的类型。

```c
    // 枚举类型
    enum Jar_type {
        CUP, PINT, QUART, GALLON
    };
```

这条语句声明了一个类型，称为Jar_Type

```c
    // 枚举类型
    enum Jar_type {
        CUP, PINT, QUART, GALLON
    };

    enum Jar_type jar1, jar2;

    enum {
        CAT, DOG, PIG
    } animal1, animal2;
```

感觉enum的定义方式有点像struct。

这种类型的变量实际上以整型的方式存储，这些符号名的实际值都是整型值。

#### 3.1.2 浮点类型 ####

通常以一个小数以及一个以某个假定数为基数的指数组成。

浮点数家族包括float，double，long double类型。

头文件float.h 定义了名字 FLT_MAX, DBL_MAX, LDBL_MAX来表示浮点类型能存储的最大值。

浮点数字面值在缺省情况下都是double类型的，除非它的后面跟一个L或者l表示它是一个long double类型，用f或者F来表示float类型。

#### 3.1.3 指针 ####

**一、指针常量 pointer constant**

**二、字符串常量 string literal**

他是一串以NUL字节结尾的零个或多个字符。字符串通常存储在字符数组中。NUL字节是用于终结字符串的，所以在字符串内部不能有NUL字节。

在程序中使用字符串常量会生成一个"指向字符的常量指针"。当一个字符串常量出现于一个表达式中时，表达式所使用的值就是这些字符所存储的地址，而不是这些字符本身。

你可以把字符串常量赋值给一个“指向字符的指针”，后者指向这些字符所存储的地址。

但是，你不能把字符串常量赋值给一个字符数组，因为字符串常量的直接值是一个指针，而不是这些字符本身。

### 3.2 基本声明 ###

#### 3.2.1 初始化 ####

在声明时对变量进行初始化

#### 3.2.2 声明简单数组 ####

#### 3.2.3 声明指针 ####

```c
int *a; // *a 产生的结果是int.
```

`*` 操作符执行的是间接访问操作，所以 a肯定是一个指向int的指针。

在声明指针变量时，可以为它指定初始值。

```c
char *msg = "hello world";
// 这里是把字符串常量第一个字符的地址赋值给了msg指针变量。
```

#### 3.2.4 隐式声明 ####

函数如果不显式地声明返回值类型，他就默认返回整型。

### 3.3 typedef ###

`typedef char *ptr_to_char`

为数据类型定义新的名字。

typedef在结构中特别有用。

应该使用typedef而不是#define来创建新的类型名。

### 3.4 常量 ###

使用 `const` 关键字来声明常量

```c
int const a;
const int a;
```

两种初始化方式：

- 在声明时进行初始化
- 在函数中声明为const的形参在函数被调用时会得到实参的值。

const关键字与指针的互动：

`int const *pci` 指向整型常量的指针。可以修改指针的值，但是不能修改它所指向的值。

```c
int i = 10;
int i2 = 20;

int const *pci = &i;

pci = &i2;
*pci = 40; // error

int *p1;
*p1 = 20;

printf("the pci point value is %d\n", *pci);
```

`int *const cpi`指向整型的常量指针，此时指针是常量，指针的值无法修改，可以修改它所指向的整型的值。

```c
int a = 10;
int b = 20;

int *p1;
int *const cpi = &a;

// cpi = &b;
*cpi = b;
```

`int const * const cpci`; 指针本身还是所指向的值都是常量。

**定义常量的另一种机制:** `#define MAX_LEN 50`

### 3.5 作用域 ###

scope, 变量只有在特定的区域才能被访问，只要分属不同的作用域，就可以给不同的变量起同一个名字。

四种不同类型的作用域：

- 文件作用域
- 函数作用域
- 代码块作用域
- 原型作用域

#### 3.5.1 代码块作用域 block scope ####

任何在代码块的开始位置声明的标识符都具有代码块作用域 block scope,

函数定义的形参在函数体内部也具有代码块作用域

#### 3.5.2 文件作用域 file scope ####

任何在所有代码块之外声明的标识符都具有文件作用域。

在头文件中编写并通过 #include指令包含到其他文件中的声明就好像直接写在那些文件中一样。所以它们的作用域并不局限于头文件的文件尾。

#### 3.5.3 原型作用域 prototype scope ####

#### 3.5.4 函数作用域 function scope ####

只适用于语句标签，用于goto语句。

一个函数中的所有语句标签必须唯一。

### 3.6 链接属性 ###

标识符的链接属性`linkage`决定如何处理在不同文件中出现的标识符。标识符的作用域与它的链接属性有关，但这两个属性并不相同。

处理不同文件中出现的相同标识符。

链接属性三种：

- external：任何地方表示同一个实体
- internal：在同一个源文件内的所有声明都指同一个实体，不同的源文件的多个声明则分属不同的实体
- none：该标识符的多个声明被当作独立不同的实体。

默认情况下，函数的链接属性为external；文件作用域变量的链接属性为 external。代码块作用域变量的链接属性为none；

关键字 extern 和 static 用于在声明中修改标识符的链接属性，如果某个声明默认具有external的链接属性，在它前面加上 static 关键字可以使其链接属性变为 internal 。

static只对缺省链接属性为external的声明才有改变链接属性的效果。

**extern**

```c
//demo1.c
int x = 10;                                       #include <stdio.h>
void print(void)                                  int main(void)
{                                                 {
    printf("Hello World!\n");                         extern int x;
}                                                     printf("%d ");
                                                      print();
                                                      return 0;
                                                  }       //demo2.c
```

**static**

```c
//demo4.c
static int x = 10;                                #include <stdio.h>
static void print(void)                           int main(void)
{                                                 {
    printf("Hello World!\n");                         extern int x;
}                                                     printf("%d ");
                                                      print();
                                                      return 0;
                                                  }       //demo5.c
```

这两个关键字只有在声明中才是必须的。

### 3.7 存储类型 ###

指存储变量值的内存类型。

- 普通内存
- 运行时堆栈
- 硬件寄存器

变量的默认存储类型取决于它的声明位置。

代码块之外的声明总是存储于静态内存。

在代码块内部声明的变量缺省类型是自动的，存储于堆栈中，自动变量。在程序执行到声明自动变量的代码块时，自动变量才被创建，当程序的执行流离开该代码块时，这些自动变量便自行销毁。

对于在代码块内部声明的变量，如果给它加上关键字static，可以使存储类型变为静态类型。

函数的形参不能声明为静态。

register关键字可以用于自动变量的声明。

**初始化**

自动变量和静态变量初始化的差异。

自动变量没有默认的初始值。

具有external链接属性的实体总是具有静态存储类型。

### 3.8 static关键字 ###

用于函数定义和代码块之外的变量声明时，static用于修改标识符的链接属性。

用于代码块内部的变量声明时，static用于修改存储类型。

## 4. 语句 ##

## 5. 操作符和表达式 ##

### 5.1 操作符 ###

#### 5.1.1 算术运算符 ####

```c
+ - / * %

% ---- 取模操作符
```

#### 5.1.2 移位操作符 ####

左移位操作符为 `<<`

右移位操作符为 `>>`

注意：有符号数的右移位，分为逻辑右移(填0)和算术右移(根据符号位决定)

#### 5.1.3 位操作符 ####

位操作符有：

```c
& | ^ ~
```

#### 5.1.4 赋值 ####

用一个等号表示。

#### 5.1.5 单目操作符 ####

- `!` 逻辑反操作
- `~` 对整形数进行求补操作
- `&` 产生它的操作数的地址。
- `*` 间接访问操作符，它与指针一起使用，用于访问指针所指向的值。
- sizeof: 判断操作数的类型长度，以字节为单位。可以是表达式也可以是两边加上括号的类型名。当sizeof操作数组名时，它返回该数组的长度，以字节为单位。
- `(type)` 强制类型转换。

#### 5.1.6 关系操作符 ####

```c
> >= < <= != ==
```

这些操作符产生的结果是一个整数值。

#### 5.1.7 逻辑操作符 ####

```c
&& ||
```

#### 5.1.8 条件操作符 ####

#### 5.1.9 逗号操作符 ####

#### 5.1.10 下标引用，函数调用和结构成员 ####

```
array[point]
*(array + (point))
```

### 5.2 布尔值 ###

零是假，任何非零值皆为真

### 5.3 左值和右值 ###

左值就是能够出现在赋值符号左边的东西，右值就是那些可以出现在赋值符号右边的东西。

标识了一个可以存储结果值的地点。

指定了一个值。

### 5.4 表达式求值 ###

#### 5.4.1 隐式类型转换 ####

#### 5.4.2 算术转换 ####

#### 5.4.3 操作符的属性 ####

## 6. 指针 ##

### 6.1 内存和地址 ###

1. 内存中的每一个位置由独一无二的地址标识
1. 内存中的每个位置都包含一个值

### 6.2 值和类型 ###

### 6.3 指针变量的内容 ###

```c
int a = 112, b = -1;
float c = 3.14;
int *d = &a;
float *e = &c;
```

### 6.4 间接访问操作符 ###

### 6.5 未初始化和非法指针 ###

```c
int main() {
    int *a;
    *a = 10;
    return 0;
}
```

在对指针进行间接访问之前，必须确保指针已被初始化。

### 6.6 NULL指针 ###

一个特殊的指针变量，表示不指向任何东西。

要使一个指针变量为NULL，你可以给它赋一个0值。

### 6.7 指针，间接访问和左值 ###

指针变量可以作为左值，并不是因为他们是指针，而是因为他们是变量。对指针变量进行间接访问表示我们应该访问指着所指向的位置。间接访问指定了一个特定的内存位置，所以我们可以把 间接访问表达式的结果作为左值使用。

```c
*d = 10 - *d;
d = 10 - *d; // error, 把一个整型存储一个指针变量中。
```

### 6.8 指针，间接访问和变量 ###

```c
*&a=25;
```

产生a的地址，并对该地址进行间接访问，为该指针指向的地址赋值一个新的值。

### 6.9 指针常量 ###

```c
* (int *) 100 = 25;
```

### 6.10 指针的指针 ###

```c
int a = 12;
int *b = &a;
int **c = &b;
```

*操作符具有从右至左的结合性，所以表达式相当于 `*(*c)` 

*c 访问变量c所指向的位置，第二个间接访问操作符这个位置所指向的地址。

### 6.11 指针表达式 ###

首先给出定义：

```c
char ch = 'a';
char *cp = &ch;
```

| 表达式    | 右值                                                         | 左值                                 |
| --------- | ------------------------------------------------------------ | ------------------------------------ |
| ch        | 'a'                                                          | 变量ch的内存地址                     |
| &ch       | 变量ch的内存地址                                             | 非法                                 |
| cp        | cp位置存放的值，就是ch的内存地址                             | 变量cp所处的内存位置                 |
| &cp       | 变量cp所处的内存位置，产生的是指针，指向字符的指针的指针     | 非法                                 |
| *cp       | 访问cp的值指向的内存的值                                     | 访问cp的值指向的内存(ch的内存地址)   |
| *cp+1     | *的优先级高于+，先间接访问得到ch的值a，将'a' + 1 得到 'b'    | 最终结果的存储位置并未清晰定义，非法 |
| *(cp + 1) | cp+1得到一个新的地址(a向后一个位置)，再间接访问a后面的一个位置的值 | a后面一个位置的内存地址              |
| ++cp      | 增值后的指针的一份拷贝。                                     | 非法                                 |
| cp++      | 先返回cp的值的一份拷贝，再增加cp的值。                       | 非法                                 |
| *++cp     | 间接访问操作符作用于增值后的指针的拷贝上，右值是ch后面的内存的值 | 左值是就是a后面的那个位置            |
| *cp++     | 右值和左值都是ch<br />++产生一个cp的拷贝，而 `*` 操作的是cp的拷贝，同时 `++` 操作作用于cp的拷贝来增值cp。<br />通常在数组中出现 | 右值和左值都是ch                     |
| ++*cp     | 操作符的结核性都是从右至左，*cp的结果类型是char，然后char类型的值再加一。 | 非法                                 |
| &(cp+1)   | cp+1是一个临时变量，临时变量不能取地址。                     |                                      |

### 6.12 实例 ###

```c
#include <stdio.h>
#include <stdlib.h>


size_t string_len(char *string) {
    // 这里会有可能出现NULL的问题，那么解引用会报错
    int len = 0;
    while (*string++ != '\0') {
        len += 1;
    }

    return len;
}

int main(void) {
    char str1[] = "abcdef";
    int len = string_len(str1);
    printf("length is %d\n", len);
    return 0;
}
```

```c
#include <stdio.h>


#define TRUE 1
#define FALSE 0

int find_char(char **strings, char value) {
    char *string;
    while ((string = *strings++) != NULL) {
        while (*string != '\0') {
            if (*string++ == value) {
                return TRUE;
            }
        }
    }
    return FALSE;
}
```

### 6.13 指针运算 ###

指针加一个整数的结果是另一个指针。

当一个指针和一个整数量执行算术运算时，整数在执行加法运算前会根据 指针所指向类型的大小进行调整。

#### 6.13.1 算术运算 ####

```
指针 +- 整数
```

标准定义这种形式只能用于指向数组中某个元素的指针 。

让指针指向最后一个元素的后面位置是合法的，但是不能解引用。

```
指针 - 指针
```

当两个指针都指向同一个数组中的元素时，才可以进行相减，结果的类型是ptrdiff_t, 它是一种有符号整数类型。

结果是两个指针在内存中距离(以数组元素的长度为单位，而不是以字节为单位)

#### 6.13.2 关系运算 ####

还可以对两个指针值进行比较。

前提是它们都指向同一个数组中的元素。

## 7. 函数 ##

所有的函数应该都有原型。

### 7.3 函数的参数 ###

均以传值调用的方式进行。

传递给函数的数组参数在行为上就像是它们是通过传址调用的那样。

## 8. 数组 ##

### 8.1 一维数组 ###

```c
int a;
int b[10];
```

在几乎所有使用数组名的表达式中，数组名的值是一个指针常量，也就是数组第一个元素的地址，他的类型取决于数组元素的类型。

数组和指针的区别：

数组具有确定数量的元素，指针是一个标量值。编译器用数组名来记住这些属性。

只有当数组名在表达式中使用时，编译器才会为它产生一个指针常量。

在两种场合下，数组名并不用指针常量来表示：sizeof返回整个数组的长度，取一个数组名的地址所产生的是一个指向数组的指针，而不是一个指向某个指针常量值的指针。

```c
int a[10];
int b[10];
int *c;

c = &a[0];
```

c = &a[0];是一个指向数组第一个元素的指针，这个语句等同于 `c=a;`

#### 8.1.2 下标引用 ####

```c
*(b + 3);
```

b的值是一个指向整型的指针，所以b+3产生另一个指向整型的指针，然后间接访问操作访问这个新位置。

```
array[index]
*(array + index)
```

下面来个demo：

```c
int a[10] = {2, 5, 3, 5, 6, 9};
int *ap = a+2;
```

| 表达式  | 解释                                |
| ------- | ----------------------------------- |
| ap      | a+2 或者 &a[2]                      |
| *ap     | a[2] *(a+2)                         |
| ap[0]   | *(ap+(0)) ==> a[2]                  |
| ap+6    | a+8 或者 &a[8]                      |
| *ap+6   | 先解引用得到3，然后得到3+6为9       |
| *(ap+6) | a+8或者 &a[8] , 然后解引用得到 a[8] |
| ap[6]   | 同上一个表达式                      |
| &ap     | 取变量ap的地址                      |
| ap[-1]  | 下标引用就是间接访问，a[1]          |

#### 8.1.3 指针与下标 ####

下标绝不会比指针更有效率，但指针有时会比下标更有效率。

#### 8.1.5 数组和指针 ####

```c
int a[5];
int *b;
```

声明一个数组时，会有保留给数组的内存空间，然后再创建数组名，它的值是一个常量，指向这段空间的起始位置。

声明一个指针时，编译器只为指针本身保留内存空间。而且指针不会被初始化。

#### 8.1.6 作为函数参数的数组名 ####

此时传递给函数的是一份该指针的拷贝。

函数如果执行了下标引用，实际上是对这个指针执行间接访问操作。

#### 8.1.7 声明数组参数 ####

```c
int strlen(char *string);
int strlen(char string[]);
```

使用指针会更好。

#### 8.1.8 初始化 ####

```c
int vector[5] = {1,2,3,4,5};
```

**静态和自动初始化**

取决于存储类型：

静态只初始化一次，数组元素的默认值是0

对于自动变量，在默认情况下是未初始化的，如果自动变量给出了初始值，每当执行流进入自动变量声明所在的作用域时，变量就被隐式的赋值语句初始化。

#### 8.1.9 不完整的初始化 ####

#### 8.1.11 字符数组的初始化 ####

```c
char msg[] = {'a', 'c', 'd', 'd', 'e'};
char msg[] = "hello world";
```

看上去像字符串常量，实际上不是。

### 8.2 多维数组 ###

```c
int a;
int b[10];
int c[6][10];
int d[3][6][10];
```

#### 8.2.1 存储顺序 ####

在c中，多维数组的元素存储顺序按照最右边的下标率先变化的原则，称为行主序 row major order

```c
int matrix[6][10];
int *mp;

mp = &matrix[3][8];

printf("first value is %d\n",*mp);
printf("second value is %d\n",*++mp);
printf("third value is %d\n",*++mp);
```

#### 8.2.2 数组名 ####

matrix是一个指向一个包含10个整型元素的数组的指针

#### 8.2.3 下标 ####

有如下的声明：

```c
int matrix[3][10];
```

`matrix[1][5]` 访问第二行第六个元素

matrix 表达式的类型是 指向包含10个整型元素数组的指针。

matrix+1 ：指向第二行数组的指针。

`*(matrix+1)` ：标识了一个包含10个整型元素的子数组。它的类型是指向整型的指针。

`*(matrix+1) + 5`  : 对比前一个表达式，它的类型是指向整型的指针，比原来的位置偏移了5个int型元素。

`*(*(matrix+1) + 5)` : 现在就是访问指针指向的位置，那个整型元素。

`*(matrix[1] + 5)` 这个表达式和上一个表达式效果是一样的。 *(matrix+1) 等同于 matrix[1]

#### 8.2.4 指向数组的指针 ####

```c
int vector[10], *vp = vector;
int matrix[3][10], *mp = matrix;
```

第二个声明是非法的，mp的初始化不正确，matrix并不是一个指向整型的指针，而是一个指向整型数组的指针。

```c
int (*p)[10];
```

p是一个拥有10个整型元素的数组的指针。当你把p与一个整数相加时，该整数值首先根据10个整型值的长度进行调整，然后再执行加法。这样就是一行一行在matrix中移动。

```c
int *pi = &matrix[0][0];
int *pi = matrix[0];
```

这样一个指针就可以逐个访问整型元素。

#### 8.2.5 作为函数参数的多维数组 ####

多维数组的每个元素本身是另一个数组，编译器需要知道它的维数。

```c
void func2(int (*mat)[10]);
void func2(int mat[][10]);
```

关键在于编译器必须知道第二个及以后各维的长度才能对各下标进行求值，因此在原型中必须声明这些维的长度。

```c
void func2(int **mat);
```

这个声明是一个指向整型指针的指针，它和指向整型数组的指针并不是一回事。

#### 8.2.6 初始化 & 数组长度自动计算 ####

### 8.3 指针数组 ###

```c
int *api[10];
```

下标引用的优先级高于间接访问，首先执行下标引用，api是某种类型的数组。在取得一个数组元素之后，随即执行的是间接访问。

api的元素类型是指向整型的指针。

## 9. 字符串, 字符和字节 ##

### 9.1 字符串基础 ###

字符串是一串零个或者多个字符，并且以一个 NUL 字节结尾。

TODO: 字符常量和字符数组的区别？？？

### 9.2 字符串长度 ###

无符号数不要使用相减来比较，因为结果永远是非负数。

strlen 返回 结果是 size_t (size_t 在stddef.h中定义)

### 9.3 不受限制的字符串函数 ###

它们只是通过寻找NUL字节来判断它的长度，这些函数一般都指定一块内存用于存放结果字符串，我们必须保证结果字符串不会溢出这块内存。

#### 9.3.1 复制字符串 ####

```c
char *strcpy(char *dst, char const *src); // const 防止修改指针指向的内容
```

dst 参数必须是一个字符数组或者是一个指向动态分配内存的数组的指针。

目标参数以前的内容将被覆盖并丢失。

#### 9.3.2 连接字符串 ####

```c
char *strcat(char *dst, char const *src);
```

目标字符数组剩余的空间足以保存整个源字符串。

#### 9.3.3 函数的返回值 ####

strcpy和strcat都返回它们第一个参数的一份拷贝，就是一个指向目标字符数组的指针。

#### 9.3.4 字符串比较 ####

```c
int strcmp(char const *s1, char const *s2);
```

### 9.4 长度受限的字符串函数 ###

显式接受一个长度参数。

```c
char *strncpy(char *dst, char const *src, size_t len);
char *strncat(char *dst, char const *src, size_t len);
int strncmp(char const *s1, char const *s2, size_t len);
```

### 9.5 字符串查找基础 ###

```c
char *strchr(char const *str, int ch);
char *strrchr(char const *str, int ch);

char *strpbrk(char const *str, char const *group); // 查找一组字符第一次在字符串中出现的位置

char *strstr(char const *s1, char const *s2); // 查找子串
```

### 9.7 错误信息 ###

```c
char *strerror(int error_number);
```

### 9.8 字符操作 ###

操作单独的字符，位于`ctype.h`

两种是字符测试和字符转换

| 函数    | 功能         |
| ------- | ------------ |
| iscntrl | 是否控制字符 |
| isspace | 空白字符     |
| isdigit | 十进制数     |
| ...     |              |
| tolower |              |
| toupper |              |

### 9.9 内存操作 ###

这些函数能够处理任何字节序列

```c
void *memcopy(void *dst, void const *src, size_t length);
void *memmove(void *dst, void const *src, size_t length);
void *memcmp(void *dst, void const *src, size_t length);
void *memchr(void *dst, void const *src, size_t length);
void *memset(void *dst, void const *src, size_t length);
```

## 10. 结构和联合 ##

### 10.1 结构基础知识 ###

结构变量在表达式中使用时，它并不被替换成一个指针。

#### 10.1.1 结构声明 ####

```c
struct tag {member-list} variable-list;
```

所有可选部分不能全部省略，至少要出现两个。

```c
struct {
    int a;
    char b;
    float c;
} x;

struct {
    int a;
    char b;
    float c;
} y[20], *z;
```

这两个声明被编译器当作不同的类型。

```c
struct SIMPLE {
    int a;
    char b;
    float c;
};
struct SIMPLE a, b[20], *c;
```

标签字段允许为成员列表提供一个名字，这样就可以在后续的声明中使用。

标签标识了一种模式，用于声明未来的变量。

还有另一种技巧是用typedef创建一种新的类型：

```c
typedef struct {
    int a;
    char b;
    float c;
} SIMPLE;

SIMPLE e, r[20], *t;
```

现在这个SIMPLE是个类型名，所有声明方式也有不同。

#### 10.1.2 结构成员 ####

```c
struct SIMPLE {
    int a;
    char b;
    float c;
};

struct COMPLEX {
    float f;
    int a[20];
    long *lp;
    struct SIMPLE s;
    struct SIMPLE sa[10];
    struct SIMPLE *sp;
};
```

#### 10.1.3 结构成员的直接访问 ####

```c
struct COMPLEX comp;
```

点操作符的结合性是从左向右。

```c
comp.s.a ==> (comp.s).a
```

下标引用和点操作符具有相同的优先级，它们的结合性都是从左向右。

```c
((comp.sa)[4]).c ==> comp.sa[4].c
```

#### 10.1.4 结构成员的间接访问 ####

如果拥有一个指向结构的指针，该如何访问这个结构的成员？

```c
void func(struct COMPLEX *cp);

(*cp).f 
```

先执行间接访问，然后执行点操作符。

`->` 左操作数必须是一个指向结构的指针，箭头操作符对左操作数执行间接访问取得指针所指向的结构，然后和点操作符一样，根据右操作数选择一个指定的结构成员。

```c
cp->f
cp->a
```

#### 10.1.5 结构的自引用 ####

```c
struct SELF_REF1 {
    int a;
    struct SELF_REF1 b;
    int c;
};
```

在遇到内部成员b时，编译器还不知道SELF_REF1的完整结构，所以这个表达式时非法的。

```c
struct SELF_REF1 {
    int a;
    struct SELF_REF1 *b;
    int c;
};
```

而这个声明是合法的，因为编译器有确定的指针长度。

```c
typedef struct SELF_REF2_TAG {
    int a;
    struct SELF_REF2_TAG *b;
    int c;
} SELF_REF2;
```

#### 10.1.6 不完整的声明 ####

使用不完整声明

```c
struct B;

struct A {
    struct B *p;
};

struct B {
    struct A *p;
};
```

#### 10.1.7 结构的初始化 ####

### 10.2 结构,指针和成员 ###

```c
typedef struct {
    int a;
    short b[2];
} Ex2;

typedef struct EX {
    int a;
    char b[3];
    Ex2 c;
    struct EX *d;
} Ex;
```

```c
Ex x = {
    10,
    "Hi",
    {5, {-1, 25}},
    0
};
Ex *px = &x;
```

#### 10.2.1 访问指针 ####

```
px: 一个指针变量，右值是其内容，左值可以赋值一个新的结构地址
px+1: 下一个地址

*px: 可以结合点操作符访问结构成员，右值是指针指向的结构本身。
*px + 1
*(px + 1): 获取下一个结构。结果是未定义的
```

#### 10.2.3 访问结构成员 ####

```
px->a ：访问结构的成员a
```

`*px` 和 `px->a` 的区别：

实际上内存中这两个变量的内容都是一样的，结构和a的地址是一样。

但是变量的类型是不一样的。

```
&px->a: -> 操作符的优先级高于&操作符的优先级
px->b : 一个指针常量。 如果我们对这个表达式执行间接访问操作，它将访问数组的第一个元素。
```

#### 10.2.4 访问嵌套的结构 ####

```
px->c.a : 访问c的特定成员。

*px->c.b : 首先执行箭头操作符，结果是c，.b 访问结构c的成员b，结果是一个int * 的常量指针，最后间接访问，结果是数组的第一个元素。
```

#### 10.2.5 访问指针成员 ####

```
px->d : 它的右值是0，它的左值是他本身的内存位置。

*px->d : 获取d所指的结构。


```

### 10.3 结构的存储分配 ###

只有当存储成员时需要满足正确的边界对齐要求时，成员之间才可能出现用于填充的额外内存空间。

```c
struct ALIGN {
	char a;
    int b;
    char c;
}

demo: |a 3blank|b|c 3blank|
```

可以在声明中对结构成员列表重新排列：

```c
struct ALIGN2 {
    int a;
    char b;
    char c;
}
```

sizeof 能够得出一个结构的整体长度，包括因边界对齐 而跳过的那些字节。

确定结构某个成员的实际位置，应该考虑边界对齐因素，可以使用 offsetof 宏 (定义于 stddef.h)

```
offsetof(type, member)
```

### 10.4 作为函数参数的结构 ###

传递指针效率会更好一些。

付出的代价是必须在函数中使用间接访问来访问结构的成员。

使用 const 关键字来防止修改指针指向的内容。

```c
void print_receipt(register Transaction const *trans);
```

### 10.5 位段 ###

### 10.6 联合 ###

## 11. 动态内存分配 ##

### 11.2 malloc 和 free ###

```
// defined in stdlib.h
void *malloc (size_t size);
void free(void *pointer);
```

需要分配的内存字节数，如果内存池中的可用内存可以满足这个需求，malloc就返回一个指向被分配的内存块起始位置的指针。

free的参数必须要么是NULL，要么是一个先前从malloc calloc realloc 返回的值。向free传递一个NULL参数不会产生任何效果。

### 11.3 calloc 和 realloc ###

```c
void *calloc(size_t num_elements, size_t element_size);
void realloc(void *ptr, size_t new_size);
```

calloc 在返回指向内存的指针之前把它初始化位0。

realloc 函数用于修改一个原先已经分配的内存块的大小。如果原先的内存块无法改变大小，realloc将分配另一个正确的大小的内存，并把原先那块内存的内容复制到新的块上。应该使用realloc 返回的新指针。

### 11.5 常见的动态内存错误 ###

忘记检查所请求的内存是否成功分配。

### 11.6 内存分配实例 ###

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare_integers(void const *a, void const *b) {
    register int const *pa = a;
    register int const *pb = b;

    return *pa > *pb ? 1 : *pa < *pb ? -1 : 0;
}

int main() {
    int *array;
    int n_values;
    int i;

    printf("How many values are there?");
    if (scanf("%d", &n_values) != 1 || n_values <= 0) {
        printf("illegal number of values.\n");
        exit(EXIT_FAILURE);
    }

    array = malloc(n_values * sizeof(int));
    if (array == NULL) {
        printf("can\'t get memory for that many values.\n");
        exit(EXIT_FAILURE);
    }

    for (i = 0; i < n_values; i += 1) {
        printf("? ");
        if (scanf("%d", array + i) != 1) {
            printf("Error reading value #%d\n", i);
            free(array);
            exit(EXIT_FAILURE);
        }
    }

    qsort(array, n_values, sizeof(int), compare_integers);
    for (i = 0; i < n_values; i += 1) {
        printf("%d\n", array[i]);
    }

    free(array);
    return EXIT_SUCCESS;
}


char *strdup1(char const *string) {
    char *new_string;
    new_string = malloc(strlen(string) + 1);
    if (new_string != NULL) {
        strcpy(new_string, string);
    }
    return new_string;
}
```

```c
typedef struct {
    int cost;
    int supplier;
} Partinfo;

typedef struct {
    int n_parts;
    struct SUBASSYPART {
        char partno[10];
        short quan;
    } *part;

} Subassyinfo;

typedef struct {
    char partno[10];
    int quan;
    enum {
        PART, SUBASSY
    } type;
    union {
        Partinfo *part;
        Subassyinfo *subassy;
    } info;

} Invrec;

#include <stdlib.h>
#include <stdio.h>
#include "inventor.h"


Invrec *create_subassy_record(int n_parts) {
    Invrec *new_rec;

    new_rec = malloc(sizeof(Invrec));
    if (new_rec != NULL) {
        new_rec->info.subassy = malloc(sizeof(Subassyinfo));
        if (new_rec->info.subassy != NULL) {
            new_rec->info.subassy->part = malloc(n_parts * sizeof(struct SUBASSYPART));
            if (new_rec->info.subassy->part != NULL) {
                new_rec->type = SUBASSY;
                new_rec->info.subassy->n_parts = n_parts;
                return new_rec;
            }
            free(new_rec->info.subassy);
        }
        free(new_rec);
    }
    return NULL;
}

```

## 12. 使用结构和指针 ##

### 12.1 链表 ###

### 12.2 单链表 ###

```c
typedef struct NODE {
    struct NODE *link;
    int value;
} Node;

#define FALSE 0;
#define TRUE 1;

```

```c
int sll_insert(Node *current, int new_value) {
    Node *previous;
    Node *new;

    while (current->value < new_value) {
        previous = current;
        current = current->link;
    }

    new = (Node *) malloc(sizeof(Node));
    if (new == NULL) {
        return FALSE;
    }

    new->value = new_value;
    new->link = current;
    previous->link = new;
    return TRUE;
}
```

1，这个函数没有对current的值测试，NULL

2，这个函数没办法访问root指针。

```c
int sll_insert2(Node **rootp, int new_value) {
    Node *current;
    Node *previous;
    Node *new;

    current = *rootp;
    previous = NULL;

    while (current != NULL && current->value < new_value) {
        previous = current;
        current = current->link;
    }

    new = (Node *) malloc(sizeof(Node));
    if (new == NULL) {
        return FALSE;
    }
    new->value = new_value;
    
    new->link = current;
    if (previous == NULL) {
        *rootp = new;
    } else {
        previous->link = new;
    }

    return TRUE;
}
```

链表中的每个节点都有一个指向它的指针，对于第一个节点，这个指针是根指针，对于其他节点，这个指针是前一个节点的link字段。重点是每个节点都一个指针指向它。

两个变量：一个指向当前节点的指针，一个指向当前节点的link字段的指针。

```c
int sll_insert3(register Node **linkp, int new_value) {
    register Node *current;
    register Node *new;
    
    // current = *linkp;
    // while (current != NULL && current->value < new_value) {
    //     linkp = &current->link;
    //     current = *linkp;
    // }
    while ((current = *linkp) != NULL && current->value < new_value) {
        linkp = &current->link;
    }

    new = (Node *) malloc(sizeof(Node));
    if (new == NULL) {
        return FALSE;
    }
    new->value = new_value;
    new->link = current;
    *linkp = new;
    return TRUE;
}

void print_linked_list(Node **rootp) {
    Node *current;
    while ((current = *rootp) != NULL) {
        printf("node value: %d\n", current->value);
        rootp = &current->link;
    }

}
```

### 12.3 双链表 ###

## 13. 高级指针话题 ##

### 13.1 指向指针的指针 ###

```c
int i;
int *pi;
int **ppi;
```

ppi: 自动变量。

&ppi: 存储ppi的地址

*ppi = 5 : 对ppi不应该执行间接访问操作，因为他尚未被初始化。

### 13.2 高级声明 ###

```c
int f;
int *f;

int *f(); // 首先执行的是和函数调用操作，它的优先级高于间接访问操作
int (*f)(); // 使得间接访问在函数调用之前进行，使f成为一个函数指针，它所指向的函数返回一个整型值

int *(*f)(); // f是一个函数指针，函数的返回值是一个整型指针
int f[];
int *f[]; // 指针数组
int f()[];  // f是一个函数，返回值是数组，非法
int f[]();  // f是一个数组，它的元素类型是返回值为整型的函数

int (*f[])();  // *f[] 先进行求值，f是一个元素为某种类型的指针的数组，数组元素的类型是函数指针，它所指向的函数的返回值是一个整型值。
int *(*f[])();

int *(*g[])(int, float);
```

### 13.3 函数指针 ###

```c
#include <stdio.h>

int f(int a) {
    return a;
}

int main() {
    int (*pf) (int) = &f;
    printf("pf is %p\n", pf);
    
    f(25);
    (*pf)(25);
    pf(23);
    
    return 0;
}

```

第一个语句，使用名字调用函数f，函数f首先被转换为一个函数指针，该指针指定函数在内存中的位置，函数调用操作符调用该函数。

#### 13.3.1 回调函数 ####

```c
Node * search_list(Node * node, void const * value, int (*compare) (void const *, void const *));
```

#### 13.3.2 转移表 ####

```c
double add(double, double);
double suB(double, double);
double mul(double, double);
double div(double, double);

double (*oper_func[]) (double, double) = {
    add, sub, mul, div, 
}

```

### 13.4 命令行参数 ###

```c
int main(int argc, char **argv);
```

### 13.5 字符串常量 ###

当一个字符串常量出现于表达式中，它的值是个指针常量。

## 14. 预处理器 ##

### 14.1 预定义符号 ###

| 符号           | 含义     | demo     |
| -------------- | -------- | -------- |
| `__FILE__`     | 源文件名 | "name.c" |
| `__LINE__`     |          |          |
| `__DATE__`     |          |          |
| `__TIME__`     |          |          |
| `__STDC__`     |          |          |
| `__FUNCTION__` |          |          |

### 14.2 #define ###

```c
#define name stuff

#define reg register
#define do_forever for(;;)
#define CASE break;case
```

不应该在宏定义的尾部加上分号。

#### 14.2.1 宏 ####

#define 机制包括了一个规定，允许把参数替换到文本中，这种实现通常称为宏 Marco 

```c
#define name(parameter-list) stuff
```

```c
#include <stdio.h>

#define SQUARE(x) x*x
#define DOUBLE(x) (x) + (x)

int main() {
    int a = 5;
    printf("%d\n", SQUARE(a + 1));  // 5 + 1 * 5 + 1
    printf("%d\n", 10 * DOUBLE(a)); // 10 * (5) + (5)
    return 0;
}
```

所有用于对数值表达式进行求值的宏定义都应该用这种方式加上括号。

#### 14.2.2 #define替换 ####

- 在调用宏时，首先对参数进行检查，看看是否包含了任何由#define定义的符号，如果是它们首先被替换。
- 替换文本随后被插入到程序中原本文本位置。对于宏，参数名被它们的值替换
- 最后，再次对结果文本进行扫描，看看它是否包含了任何由#define定义的符号。如果是，就重复上述处理过程。

宏不可以出现递归。

当预处理器搜索#define时，字符串常量的内容并不进行检查。

1，邻近字符串自动连接的特性：

```c
#define PRINT(FORMAT, VALUE) printf("The value is" FORMAT "\n", VALUE)


int main() {
    int a = 5;
    PRINT("%d", a);
    return 0;
}
```

2，使用预处理器把一个宏参数转换为一个字符串。

`#argument` 被翻译为 "argument"

```
#define PRINT(FORMAT, VALUE) printf("The value of " #VALUE " is " FORMAT "\n", VALUE)


int main() {
    int a = 5;
    PRINT("%d", a + 8);
    return 0;
}
```

`##` 把位于它两边的符号连接成一个符号。

```c
#define ADD_TO_SUM(SUM_NUMBER, VALUE) sum ##SUM_NUMBER += VALUE


int main() {
    int a = 5;
    int sum5 = 0;

    ADD_TO_SUM(5, 25);
    PRINT("%d", sum5);
    return 0;
}
```

#### 14.2.3 宏与函数 ####

用于执行简单的计算。

宏与类型无关

```c
#define MALLOC(n, type) ((type *) malloc((n) * sizeof(type)))
```

#### 14.2.4 代副作用的宏参数 ####

当宏参数在宏定义中出现的次数超过一次时，如果这个参数具有副作用。

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))


int main() {
    // int a = 5;
    // int sum5 = 0;
    // ADD_TO_SUM(5, 25);
    // PRINT("%d", sum5);

    int x = 5;
    int y = 8;

    int z = MAX(x++, y++);
    PRINT("%d", z);
    PRINT("%d", x);
    PRINT("%d", y);
    return 0;
}
```

#### 14.2.5 命令约定 ####

#### 14.2.6 #undef ####

移除宏定义

```c
#undef name
```

如果一个现有的名字需要被重新定义，旧的定义必须要先移除

#### 14.2.7 命令行定义 ####

在UNIX编译器中 -D 选项可以完成。

```
-Dname
-Dname=stuff
```

第一种：定义了符号name，它的值为1

第二种：把该符号的值定义为等号后面的stuff

去除符号定义选项 -U

#### 14.3 条件编译 ####

```c
#if NAME
// xxxx
#endif
```

NAME：常量表达式：字面量常量，或者是一个由#define定义的符号。

```c
#if NAME
// xxxx
#elif NAME1
// aaaaaa
#else
// bbbbb
#endif
```

#### 14.3.1 是否被定义 ####

```c
defined(symbol)
```

#### 14.3.2 嵌套指令 ####

### 14.4 文件包含 ###

### 14.5 其他指令 ###

```c
#error text of error message

#progma
```

## 15. 输入/输出函数 ##

### 15.1 错误报告 ###

