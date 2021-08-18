# CSS: The Definitive Guide #

## 前言 ##

### 取值句法约定 ###

`<family-name>#`

`<url> || <color>`

`<url>?<color> [/<color>]`

`[ <length>|thick | thin]{1,4}`

尖括号内表示值的类型，或者是引用其他属性的值。以等宽字体显示的值是关键字，必须原样编写，不能加引号。

- 连在一起只有空格分开的两个或多个关键字，必须以给定顺序使用。
- 以 `|` 分隔的值必须取其中一个值，而且只能取一个。
- 以 `||` 分隔的值可以取一个也可以取两个值。
- 以 `&&` 连接的值必须同时取A和B
- 方括号 `[]` 用于分组。

各部分或者分组的修饰符：

- `*` 重复零次或者多次
- `+` 重复一次或多次
- `#` 可以重复一次或者多次，而且多次出现要以 `,` 分隔
- `?` 可选的
- `!` 必须的
- `{M,n}`  表示至少重复M,至多重复N次

## 1. CSS & Document ##

### 1.2 元素 ###

#### 1.2.1 置换元素和非置换元素 ####

**置换元素** 用来置换元素内容的部分不由文档内容直接表示。

**非置换元素** 由浏览器再元素自身生成的框中显示。

#### 1.2.2 元素的显示方式 ####

分为块级元素和行内元素。

**块级元素** 生成一个填满父级元素内容区域的框，旁边不能有其他元素。

**行内元素** 在一行内生成元素框，补打断所在的行。

### 1.3 应用CSS ###

#### 1.3.1 link标签 ####

```html
<link rel="stylesheet" type="text/css" href="chapter01.css" media="all">
```

必须放在head元素中。

- rel: relation
- type: text/css
- href: 样式表的URL
- media: 一个或者多个媒体描述符。
- 候选样式表：将rel定义为 `alternate stylesheet` 会使用title属性生成候选样式表列表。

#### 1.3.2 style 元素 ####

#### 1.3.3 `@import`  ####

```css
@import url(demo2.css);
@import url(demo1.css) all;
```

#### 1.3.4 HTTP链接 ####

#### 1.3.5 行内样式 ####

### 1.4 样式表中的内容 ###

一个规则由：selector 和 declaration block 组成。

#### 1.4.3 厂商前缀 ####

### 1.5 媒体查询 ###

#### 1.5.1 用法 ####

- link元素的media属性
- style元素的media属性
- @import 声明的媒体描述符部分
- @media 声明的媒体描述符部分

#### 1.5.2 简单的媒体查询 ####

```css
h1 {color: maroon;}
@media projection {
    body {background: yellow;}  
}
```

#### 1.5.3 媒体类型 ####

css2引入。

- all
- print
- screen

## 2. Selector ##

### 元素选择符 ###

```css
body {display: block flow;}
```

### 群组选择符 ###

```css
body, p {color: red;}
```

通用选择符： 

```css
* {color: red;}
```

### 类选择符和ID选择符 ###

应用样式而不关心所涉及的元素，最常用类选择符。

```css
.warning {
    font-weight: bold;
    color: red;
}
```

使用 ID选择符，类选择符，属性选择符，伪类选择符或者伪元素选择符时，如果没有依附元素选择符，隐式蕴含通用选择符。

```css
.warning {
    font-weight: bold;
    color: red;
}
p.warning {
    background: green;
}
```

多个类的写法：

```css
.warning.help {
    color: #666666;
}
```

ID选择符:

```css
*#demo-01 {
    color: red;
}
```

### 属性选择符 ###

**简单属性选择符**

简单选择具有某个属性的写法：

```css
*[title] {
    color: green;
}
/*多个属性选择, 同时拥有*/
a[href][title] {
    font-weight: bold;
}
```

**精准的属性值选择**

```css
a[href="https://demo.com/1.png"] {
    font-weight: bold;
}
```

**部分属性值选择**

| 形式             | 说明                           |
| ---------------- | ------------------------------ |
| `[foo!="bar"]`   | 值本身或者 值和`-`开头的属性   |
| `[foo~="bar"]`   | 值是以空格分隔的一组值中的一个 |
| `[foo*="bar"]`   | 匹配属性值的子串               |
| `[foo^="bar"]`   | 匹配属性值开头的子串           |
| `[foo$="bar"]`   | 匹配属性值结尾的子串           |
| `[foo$="bar" i]` | 不区分大小写                   |

### 后代选择符 (上下文选择符) ###

```css
h1 em {
    color: gray;
}
```

选择h1中的em元素，不管相隔多少代都可以。em元素在h1元素的内部。

**选择子元素**

```css
h1 > em {
    color: maroon;
}
```

**选择紧邻同胞元素**

选择同一个父元素中**紧跟**在另一个元素后面的一个元素。

```css
h1 + p {
    margin-top: 0;
}
```

**选择后续同胞**

选择一个元素后面属于同一个父元素的另一个元素，不需要紧跟的。

```css
h1 ~ p {
    color: red;
}
```

### 伪类选择符 pseudo-class  ###

```css
a:link:hover {
    color: blue;
}
a:visited:hover {
    color: maroon;
}
```

**选择根元素**

`:root`

**选择空元素**

`:empty`

**选择唯一的子代**

`:only-child`

**选择唯一的某种元素**

`:only-of-type`

**选择第一个和最后一个元素**

`:first-child`

`:last-child`

**选择第一个或者最后一个某种元素**

`:first-of-type`

`:last-of-type`

#### 动态伪类 ####

| 伪类       | 说明                   |
| ---------- | ---------------------- |
| `:link`    | 未访问                 |
| `:visited` | 已访问                 |
| `:focus`   | 当前输入焦点的元素     |
| `:hover`   | 鼠标指针放置其上的元素 |
| `:active`  | 用户输入激活的元素     |

### 伪元素选择符 ###

**装饰首字母**

`::first-letter`

## 3. 特指度和层叠 ##

### 3.1 特指度 ###

一个特指度由四部分构成。

- 选择符中的每个ID属性值加 `0,1,0,0`
- 选择符中的每个类属性值，属性选择或伪类加 `0,0,1,0`
- 选择符中的每个元素和伪元素加 `0,0,0,1` 
- 连结符和通用选择符不增加特指度 (连结符有 ` ` `+` `>` 等)

通用选择符的特指度为 `0,0,0,0`

行内样式的特指度为 `1,0,0,0`

`!important` 声明会与不重要的声明区分开处理，重要声明和非重要声明冲突时，重要声明始终胜出。

### 3.2 继承 ###

继承的值没有特指度。

### 3.3 层叠 ###

## 4. 值和单位 ##



