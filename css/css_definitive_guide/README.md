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

