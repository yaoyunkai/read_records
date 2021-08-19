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

## CSS 属性 ##

### all ###

- 取值：`inherit | initial | unset`
- 初始值

### display ###

- **取值** `[<display-outside || <display-inside>] | <display-listitem> | <display-internal> | <display-box> | <display-legacy>`
- **定义**
- **默认值** ：inline
- **适用于**：所有元素
- **计算值** ：指定的值
- **继承性**：:x:
- **动画性**：:x:

### font-family ###

- **取值** `[<family-name>|<generic-family]#`
- **初始值**：由浏览器指定
- **适用于**：所有元素
- **计算值** ：指定的值
- **继承性**​： :heavy_check_mark:
- **动画性**： :x:

### font-weight ###

- **取值**： `normal | bold | bolder | lighter | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900`
- **初始值**：normal
- **适用于**： 所有元素
- **计算值**：其中一个数值，或者一个数值加一个相对值
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font-size ###

- **取值**： `xx-small|x-small|small|medium|large|x-large|xx-large|smaller|larger|<length>|<percentage>`
- **初始值**：medium
- **适用于**： 所有元素
- **计算值**：一个绝对长度
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### font-size-adjust ###

- **取值**： `<number>|none|auto`
- **初始值**：none
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### font-style ###

- **取值**： `italic|oblique|normal`
- **初始值**：normal
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font-stretch ###

- **取值**： `nromal | ultra-condensed | extra-condensed | condensed |...`
- **初始值**：normal
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font-kerning ###

- **取值**： `auto | normal | none`
- **初始值**：auto
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font-variant ###

- **取值**： `normal | small-caps`
- **初始值**：normal
- **计算值**：指定的值
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font-feature-settings ###

- **取值**： `normal | <feature-tag-value>#`
- **初始值**：normal

### font-synthesis ###

- **取值**： `none | weight || style`
- **初始值**：weight style
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### font ###

- **取值**： `[[<font-style> || [normal | small-caps] || <font-weight>]? <font-size> [/ <line-height>]? <font-family>] | caption | icon | menu | message-box | small-caption | status-bar`
- **初始值**：各个单独的属性
- **适用于**： 所有元素
- **百分数**：`<font-size>` 基于父元素计算。
- **继承性**：:heavy_check_mark:

## 1. CSS & Document ##

### 1.2 元素 ###

#### 1.2.1 置换元素和非置换元素 ####

**置换元素** 用来置换元素内容的部分不由文档内容直接表示。

**非置换元素** 由浏览器再元素自身生成的框中显示。

#### 1.2.2 元素的显示方式 ####

分为块级元素和行内元素。

**块级元素** 生成一个填满父级元素内容区域的框，旁边不能有其他元素。

**行内元素** 在一行内生成元素框，补打断所在的行。

css属性：[display](###display###)

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

### 4.1 关键字，字符串和其他文本值 ###

#### 4.1.1 关键字 ####

- 全局关键字： `inherit` `initial` `unset`
  - inherit 强制继承
  - initial 把属性设置为预定义的初始值
  - unset：是inherit和initial的通用替身，对继承的属性来说，unset相当于inherit，对于不继承的属性来说，unset的作用与initial一样。

这三个关键字所有属性都可以使用 [all](###all###)

#### 4.1.2 字符串 ####

`"this is me"`

### 4.3 距离 ###

长度为0时不需要单位

长度单位分为两种：绝对长度单位和相对长度单位

#### 4.3.1 绝对长度单位 ####

- 英寸 in
- 厘米 cm
- 毫米 mm
- 四分之一毫米 q
- 点 pt ：标准的印刷度量单位
- 派卡 pc : 1pc = 10 pt
- 像素 px ：使用屏幕上的像素，缩放页面或打印要考虑缩放。

#### 4.3.2 分辨率单位 ####

随着媒体查询和响应式设计的出现。

- 点每英寸 dpi ：在长为1英寸的范围内显示的点数
- 点每厘米 dpcm 
- 点每像素单位 dppx

#### 4.3.3 相对长度单位 ####

指其长度相对其他东西而言的，有些相对单位的实际尺寸始终相对当前元素，不同的元素也不同。

**em & ex**

1em 等于元素的font-size属性值。

em的值相对于父元素的字号而言。

1em等于所用字体中小写字母m的宽度。

ex指所用字体中小写字母x的高度。

**rem单位**

rem始终相对根元素计算，在HTML中，根元素是html。

**ch单位**

**视区相关单位**

- 视区宽度单位 vw ：这个单位根据视区的宽度计算，然后除以100.
- 视区高度单位 vh
- 视区尺寸最小值单位 vmin ：宽度或者高度中较小的那个
- 视区尺寸最大值单位 vmax

### 4.4 计算值 ###

calc()

### 4.5 属性值 ###

attr() 表达式。

```css
p::before {
    content: "[" attr(id) "]";
}
```

### 4.6 颜色 ###

具名颜色。

```css
p::before {
    content: "[" attr(id) "]";
    color: transparent;
    background: currentColor;
}
```

### 4.7 角度 ###

- deg 度数
- grad 百分度
- rad 弧度
- turn 圈数

### 4.10 自定义值 ###

```css
html {
    --base-color: #639;
    --highlight-color: #AEA;
}

h1 {
    color: var(--base-color);
}
```

## 5. font ##

### 5.1 font-family ###

为了覆盖所有情况，css定义了五种通用字体族：

- 衬线字体：`Times` `Georgia` `New Century Schoolbook`
- 无衬线字体： `helvetica` `Geneva` `Verdana` `Arial` `Univers`
- 等宽字体： `Courier` `Courier New` `Consolas` `Andale Mono`
- 草书字体
- 奇幻字体

#### 5.1.1 使用通用字体族 ####

使用属性： [font-family](###font-family###)指定。

如果想使用无衬线字体，但不要具体哪一个：

```css
body {
    font-family: sans-serif;
}
```

#### 5.1.2 指定字体族 ####

如果浏览器有Georgia字体，否则使用其他无衬线字体：

```css
h1 {
    font-family: Georgia, serif;
}
p {
    font-family: Times, 'Times New Roman', 'New Century Schoolbook', Georgia, serif;
}
```

### 5.2 使用 `@font-face` ###

出现在CSS2中。

```css
@font-face {
    font-family: 'SwitzeraADF';
    src: url("https://www.demo.com");
}

@font-face {
    font-family: 'SwitzeraADF';
    src: url("https://www.demo.com") format("opentype");
    src: url("https://www.demo.com/01") format("truetype");
}
```

必须的属性：font-family 和 src

### 5.3 字重 ###

字重的属性： [font-weight](###font-weight###)

为整个文档指定一个字体族，然后为不同的元素设定不同的字重。

### 5.4 字号 ###

[font-size](###font-size###)

em方框与字符的边界没有关系，其实他指的是在没有行距的情况下两条基线之间的距离。

font-size的作用是为字体的em方框提供一个尺寸。

字号中的百分数始终根据继承自父元素的字号计算。

#### 5.4.6 自动调整字号 ####

影响字体是否清晰易于辨认：字号和x高度。

x高度除以字号得到的结果称为高宽比值 (aspect value) 。

css提供的 [font-size-adjust](###font-size-adjust###)属性用于改变字体族之间的高宽比值。

### 5.5 字形 ###

属性：[font-style](###font-style###)

### 5.6 字体拉伸 ###

some font-family 有较宽或较窄的字母型式。css提供了一个属性 [font-stretch](###font-stretch###)，用于选择这样的变体。

## 6. 文本属性 ##

