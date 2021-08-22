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

### text-indent ###

- **取值**： `<length> | <percentage>`
- **初始值**：0
- **适用于**： 块级元素
- **百分数**：相对于所在块级元素的宽度
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### text-align ###

- **取值**： `start | end | left | right | center | justify | match-parent | start end`
- **初始值**：start
- **适用于**： 块级元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### text-align-last ###

- **取值**： `auto | start | end | left | right | center | justify`
- **初始值**：auto
- **适用于**： 块级元素
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### line-height ###

- **取值**： `<number> | <length> | <percentage> | normal`
- **初始值**：normal
- **适用于**： 所有元素
- **百分数**：相对于元素的字号
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### vertical-align ###

- **取值**： `baseline|sub|super|top|text-top|middle|bottom|text-bottom|<length>|<precentage>`
- **初始值**：baseline
- **适用于**： 行内元素和单元格
- **百分数**：相对于元素的line-height值
- **继承性**：:x:
- **动画性**：`<length>` `<precentage>`

### word-spacing ###

- **取值**： `<length>|normal`
- **初始值**：normal
- **适用于**： 所有元素
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### letter-spacing ###

- **取值**： `<length>|normal`
- **初始值**：normal
- **适用于**： 所有元素
- **计算值**：长度值得到绝对长度；否则是normal
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### letter-spacing ###

- **取值**： `uppercase|lowercase|capitalize|none`
- **初始值**：none
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### text-decoration ###

- **取值**： `none | [underline || overline || line-through || blink]`
- **初始值**：none
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:x:

### text-rendering ###

- **取值**： `auto | optimizeSpeed | optimizeLegibility | geometricPrecision`
- **初始值**：auto
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### text-shadow ###

- **取值**： `none | [<length> || <length> <length> <length> ?]#`
- **初始值**：none
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### white-space ###

- **取值**： `normal | nowrap | pre | pre-wrap | pre-line`
- **初始值**：normal
- **适用于**： 块级元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:x:

### tab-size ###

- **取值**： `<length>|<integer>`
- **初始值**：8
- **适用于**： 块级元素
- **计算值**：指定的值对应的绝对长度
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### hyphens ###

- **取值**： `manual | auto | none`
- **初始值**：manual
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:x:

### word-break ###

- **取值**： `manual | break-all | keep-all`
- **初始值**：manual
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### line-break ###

- **取值**： `auto | loose | normal | strict`
- **初始值**：auto
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### overflow-wrap ###

- **取值**： `normal | break-word`
- **初始值**：normal
- **适用于**： 所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### writing-mode ###

- **取值**： `horizontal-tb | vertical-rl | vertical-tr`
- **初始值**：horizontal-tb
- **适用于**： 所有元素(特殊)
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### text-orientation ###

- **取值**： `mixed | upright | sideways`
- **初始值**：mixed
- **适用于**： 所有元素(特殊)
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

### box-sizing ###

- **取值**： `content-box | padding-box | border-box`
- **初始值**：content-box
- **适用于**： 能指定width或height的所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:x:

### list-style-position ###

### box-decoration-break ###

- **取值**： `slice | clone`
- **初始值**：slice
- **适用于**：所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:x:

### width ###

- **取值**： `<length> | <precentage> | auto`
- **初始值**：auto
- **适用于**：所有元素(特定)
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### height ###

- **取值**： `<length> | <precentage> | auto`
- **初始值**：auto
- **适用于**：所有元素(特定)
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### padding ###

- **取值**： `[<length> | <percentage> ]{1,4}`
- **初始值**：简写形式没有
- **适用于**：所有元素(特定)
- **百分数**：相对于容纳块的宽度
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### border-style ###

- **取值**： `[ none | hidden | solid | dotted | dashed | double | groove | ridge | inset | outset ]{1,4}`
- **初始值**：简写形式没有
- **适用于**：所有元素
- **继承性**：:x:
- **动画性**：:x:

### border-width ###

- **取值**： `[thin | medium | thick | <length> ]{1,4}`
- **初始值**：简写形式没有
- **适用于**：所有元素
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### border-color ###

- **取值**： `<color>{1,4}`
- **初始值**：简写形式没有
- **适用于**：所有元素
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### border ###

- **取值**： `[<border-width> || <border-style> || <border-color>]`
- **初始值**：参考各个单独的属性
- **适用于**：所有元素
- **继承性**：:x:
- **动画性**：参考各个单独的属性

### border-radius ###

- **取值**： `[<length> | <percentage>]{1,4}[/ [<length> | <percentage>]{1,4}]?`
- **初始值**：0
- **适用于**：除表格内的元素之外的所有元素
- **继承性**：:x:
- **动画性**：:heavy_check_mark:

### border-image-source ###

- **取值**： `none | <image>`
- **初始值**：none
- **适用于**：所有元素(特定)
- **继承性**：:x:
- **动画性**：:x:

### outline-style ###

- **取值**： `auto | none | solid | dotted | dashed | double | groove | ridge | inset | outset`
- **初始值**：none
- **适用于**：所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：:x:

### outline ###

- **取值**： `[<outline-color> || <outline-style> || <outline-width>]`
- **初始值**：none
- **适用于**：所有元素
- **计算值**：指定的值
- **继承性**：:x:
- **动画性**：参考各个单独的属性

### color ###

- **取值**： `<color>`
- **初始值**：用代理指定
- **适用于**：所有元素
- **计算值**：指定的值
- **继承性**：:heavy_check_mark:
- **动画性**：:heavy_check_mark:

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

### 6.1 缩进和行内对齐 ###

明确行内和块级两个术语

#### 6.1.1 缩进文本 ####

属性：[text-indent](###text-indent###)

把第一行文本缩进指定的长度，缩进长度可以是负值。

用在任何块级元素上，缩进将沿着行内方向展开。

如果想缩进行内元素的首行，可以通过内边距或外边距实现。

#### 6.1.2 文本对齐 ####

[text-align](###text-align###) 控制元素中各文本行的对齐方式

#### 6.1.3 对齐最后一行 ####

[text-align-last](###text-align-last###)

除了块级元素的最后一行之外，还有其他行也受这个属性影响。

### 6.2 块级对齐 ###

沿着块级方向的对齐方式。

#### 6.2.1 行的高度 ####

[line-height](###line-height###) 属性指行的基线之间的距离。

定义元素中文本行基线之间的最小距离。

line-height 不影响置换元素的布局，但是依然应用到置换元素上。

**行的构成**

文本行中的每个元素构成一个内容区 (content area), 其高度由字体的高度决定。

随内容区出现的是一个行内框 (inline box) , 如果不考虑其他因素，其高度与内容区完全相等。

line-height导致的行距是影响行内框高度的因素之一。

元素的行距等于 font-size 的计算结果减去 line-height 的计算结果。这个值是行距的总值。

确定一行内容的全部行内框之后，行框也确定了。行框恰好包围最高那个行内框的顶端和最低那个行内框的底端。

![img](.assets/images2015.cnblogs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg)

em ex 和百分数相对元素的font-size值计算。

**行高的继承**

块级元素之间继承：从父元素继承 line-height值时，根据父元素的字号计算。

#### 6.2.2 纵向对齐文本 ####

css中的 [vertical-align](###vertical-align###)属性只能用于行内元素和置换元素。

baseline 强制元素的基线与父元素的基线对齐。

bottom：把元素所在行内框的底边与行框的底边对齐。

### 6.3 单词间距和字符间距 ###

#### 6.3.1 单词间距 ####

[word-spacing](###word-spacing###) 属性的值为长度，可正可负。

指定的长度值追加到单词的标准间距上。

#### 6.3.2 字符间距 ####

[letter-spacing](###letter-spacing###) 属性修改字符或者字母之间的间距。

转换文本的大小写形式： [text-transform](###text-transform###)

### 6.7 文本阴影 ###

css属性： [text-shadow](###text-shadow###)

可以为文本定义一个或多个阴影。每个阴影由一个可选的颜色和三个长度值定义。

第一个长度设定横向偏移

第二个长度设定纵向偏移

第三个长度设定阴影的模糊半径 (blur radius)

### 6.8 处理空白 ###

[white-space](###white-space###) 影响用户代理对文档源码中空格，换行符和制表符的处理方式。

对待单词之间以及文本之间空白的方式：

- pre: 小心处理空格和换行。
- nowrap: 禁止元素中的文本换行。

### 6.9 换行和断字 ###

css属性 [hyphens](###hyphens###)，

使用默认值normal时，只有在手动插入的连字符(U+00AD 或 &shy) 处断字。

使用none时，手动也不断字。

断字属性还受css属性 [word-break](###word-break###) 属性的作用是控制不同语言处理文本软换行的方式，软换行由用户代理决定，但是使用该属性可以自行控制：

- break-all 软换行可能出现在任何字符之间。
- keep-all 禁止在字符之间软换行。

CJK语言是什么？

**文本换行**

如果文本超出了所在容器怎么办？

[overflow-wrap](###overflow-wrap###)

- normal: 在单词之间换行
- break-word：在单词的内部换行

### 6.10 书写模式 ###

设置书写模式： [writing-mode](###writing-mode###)

默认值 horizont-tb的意思：行内方向为横向，块级方向为从上到下。

改变文本方向: [text-orientation](###text-orientation###)

## 7. 视觉格式化基础 ##

### 7.1 元素框基础 ###

#### 7.1.1 概念 ####

- 常规流动
- 非置换元素：内容包含在文档中的元素
- 置换元素：为其他内容占位的元素
- 根元素
- 块级框
- 行内框
- 行内块级框：内部特征像块级框，外部特征像行内框。

#### 7.1.2 容纳块 ####

容纳块是元素框体的 布局上下文。

### 7.2 调整元素的显示方式 ###

css属性 [display](###display###)

#### 7.2.1 改变显示方式 ####

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <style>
        nav a {
            display: block;
        }

    </style>
</head>
<body>

<nav>
    <a href="https://www.baidu.com" target="_blank">Baidu1</a>
    <a href="https://www.baidu.com" target="_blank">Baidu2</a>
    <a href="https://www.baidu.com" target="_blank">Baidu3</a>
    <a href="https://www.baidu.com" target="_blank">Baidu4</a>
    <a href="https://www.baidu.com" target="_blank">Baidu5</a>
</nav>

</body>
</html>
```

把链接变成块级元素后，整个元素框都变成链接了。

#### 7.2.2 块级框 ####

![img](.assets/aliyunzixunbucket.oss-cn-beijing.aliyuncs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg)

默认块级框的宽度width等于左内边界到右内边界的距离。

高度height等于上内边界到下内边界的距离。

这些属性的处理方式可以使用 [box-sizing](###box-sizing###)调整

#### 7.2.3 横向格式化 ####

```html
<p style="width: 200px; padding: 10px; margin: 20px;background: red">wideness?</p>
```

元素框的可见区域是220px宽(200px + 10px * 2),外边距又在元素的两侧添加20px，所以元素的总体宽度为260px。

在属性为content-box 和 border-box的常规流动方式下，块级框各组成部分的横向尺寸始终等于容纳块的宽度。

#### 7.2.4 横向格式化属性 ####

有七个： margin-left, border-left, padding-left, width, padding-right, border-right, margin-right。

三个属性值能设为auto: width, margin-left, margin-right。其余的要么为具体的值，要么使用默认值。

#### 7.2.5 使用auto ####

在 width, margin-left, margin-right中，

- 如果把一个设为auto，另外两个设为具体的值，那么设为auto的那个属性的具体长度要能满足元素框的宽度等于父元素的宽度。
- 如果三个为具体的值，那么margin-right重置为auto
- 左右外边距为auto，那么width的值满足总宽度，自动确定宽度。
- 左右外边距设为auto，width具体的值：元素在父元素内居中显示。
- 某个外边距和width设为auto：设为auto的那个外边距等于0
- 三个为auto：width最大宽度，外边距为0

#### 7.2.7 负外边距 ####

```css
p {
    margin-left: 10px;
    width: auto;
    margin-right: -50px;
    background: red;
    border: 3px solid gray;
}
```

此时p的总宽度为 10px+3px+0+534px+0+3px-50px=500px;

```css
p {
    margin-left: 10px;
    width: 600px;
    margin-right: auto;
    background: red;
    border: 3px solid gray;
}
```

设为auto的右外边距也可能得到负值：10px+3px+0+600px+0+3px-116px=500px;

只有外边距的值可以小于零

#### 7.2.8 百分数 ####

需要理解百分数和长度单位混合使用的情况。

边框不接受百分数，只能设为长度值。

#### 7.2.9 置换元素 ####

当width为auto时，置换元素的width等于内容自身的宽度。

明确为width提供一个值可以覆盖这个规则。

如果置换元素的width与自身宽度不同，height值会自动按比例变化。

#### 7.2.10 纵向格式化 ####

元素的内容决定了元素的默认高度。

可以为任何块级元素设定具体的高度。得到的结果取决于多个因素，假如指定的高度大于显示内容所需的高度，此时，多出的高度看起来像是内边距。

和 overflow 属性也有关系。

height默认定义内容区的高度，而不是元素框可见区域的高度。元素框的上下内边距，边框的外边距在高度的基础上增加。

**纵向格式化属性**

margin-top, border-top, padding-top, height, padding-bottom, border-bottom, margin-bottom

七个值加在一起等于块级框的容纳块的高度。

可以设为auto的属性：height和margin-top, margin-bottom

在常规流动下，如果把块级框的margin-top 或 margin-bottom 设为auto，二者都自动计算为0

如果把块级框的高度设为百分数，百分数是相对于框体的容纳块的高度而言的。

如果未明确声明容纳块的高度，那么百分数高度将被重置为auto。

**自动调整高度**

默认：高度是从最上边的子元素上边框外侧到最下边那个块级子代元素的下边框外侧之间的距离。子元素的外边距在父元素的外部。

如果块级元素有**上内边距或下内边距，或者有上边框或下边框**，那么其高度是从最上边那个子元素的上外边距的外边界到最下边那个子元素的下外边距的外边界之间的距离。

**折叠纵向外边距**

相邻的纵向外边距会折叠。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        * {
            margin: 0;
        }

        div {
            border: 1px red solid;
        }

        ul {
            margin-bottom: 30px;
            background: #99AABB;
        }

        li {
            font-size: 24px;
            line-height: 1;
            margin-top: 10px;
            margin-bottom: 20px;
            background: rgba(233,233,223, 0.3);
        }

        h1 {
            line-height: 1;
            font-size: 36px;
            margin-top: 28px;
            background: #ddd;

        }

    </style>
</head>
<body>

<div>
    <ul>
        <li>List item #1</li>
        <li>The second list item</li>
        <li>Item the third</li>
    </ul>
    <h1>Hello world</h1>
</div>

</body>
</html>
```

**负外边距和折叠**

如果两个相邻的外边距都是负值，浏览器取其中绝对值较大的那个，然后从正外边距中减去它的绝对值。

#### 7.2.16 列表项目 ####

记号的位置可以通过 [list-style-position](###list-style-position###)属性来控制。

### 7.3 行内元素 ###

#### 7.3.1 行布局 ####

- 匿名文本：不在任何行内元素中的字符串
- 字体框：由字体定义，自行可能比字体框高或者矮
- 内容区：各个字符的字体框连在一起构成的方框。
- 行距：是font-size和line-height之差，对半分添加到内容区的上部和下部
- 行内框：内容区加行距后得到的方框。
- 行框：过一行中各行内框最高点和最低点的方框。

css还定义了一些行为和概念：

- 内容区相当于块级框的内容框。
- 行内元素的背景填充在内容区加内边距所在的区域里。
- 行内元素的边框在内容区外的内边距外侧。
- 非置换行内元素的内边距，边框和外边距在对应的方框上没有纵向效果，对行内框的高度没有影响。
- 置换元素的外边距和边框对行内框的高度有影响，进而对元素所在的行框的高度有影响。

各元素的行内框高度的确定：

- 确定非置换元素的font-size和line-height
- 确定置换元素的总高度
- 确定各个内容区在一行的基线的位置。
- 确定 vertical-align属性对元素的偏移。
- 行框的高度：基线与最高那个行内框顶边之间的距离加上基线与最低那个行内框底边之间的距离。

#### 7.3.3 行内格式化 ####

没有内容就没有行框。

#### 7.3.4 行内非置换元素 ####

内容区不包括上下行距。

行框是指本行的一个虚拟的矩形框，是浏览器渲染模式中的一个概念，并没有实际显示。行框高度等于本行内所有元素中行内框最大的值。当有多行内容时，每行都会有自己的行框。

任何一个行内元素，他的高度是由font-size和line-height共同决定的。

**纵向对齐**: [vertical-align](###vertical-align###)

- top: 元素行内框的顶边与所在行框的顶边对齐
- bottom: 底边与行框对齐
- text-top: 元素行内框的顶边与父元素内容区的顶边对齐
- middle: 元素行内框的纵向中点与父元素基线以上0.5ex对齐

**控制行高**

使用line-height的最佳方式是使用纯数字，比例因子。

行内元素的外边距会出现在元素的开头和结尾。

行内元素可以想象为外围有一圈塑料的纸片。

改变断行行为： [box-decoration-break](###box-decoration-break###)

#### 7.3.5 行内置换元素 ####

行内置换元素的line-height仍然有值，纵向对齐时有这个值才能确定定位元素的位置。

#### 7.3.6 行内块级元素 ####

inline-block，在一行中的布局方式跟图像一样，实际上 行内块级元素是当做置换元素进行格式化的。

行内块级元素的底边默认是与文本行的基线对齐的，而且内部不会断行。

## 8. 内边距、边框、轮廓和外边距 ##

### 8.1 基本元素框 ###

#### 8.1.1 宽度和高度 ####

width和height无法应用到行内非置换元素上。

[width](###width###)

[height](###height###)

### 8.2 内边距 ###

css属性： [padding](###padding###)

padding各个值得顺序：top right bottom left，从上边开始，顺时针转动。

#### 8.2.1 复制 ####

- 如果只为padding提供三个值，第四个值复制第二个值；
- 如果提供两个值，第四个值复制第二个值，第三个值复制第一个值。
- 如果只提供一个值，其他三边都复制第一个值。

### 8.3 边框 ###

边框有三个要素：宽度，样式，颜色。

边框宽度的默认值为medium

边框的默认颜色是元素自身的前景色

#### 8.3.1 边框的式样 ####

css属性： [border-style](###border-style###)

一个边框也可以有多个样式，可以为上下左右分别定义样式。

还可以单独定义某一边的样式： border-top-style

#### 8.3.2 边框宽度 ####

css属性： [border-width](###border-width###)

#### 8.3.3 边框颜色 ####

css属性：[border-color](###border-color###)

以上的三个属性均有每个边的单独属性。

还有 border-top, border-right, border-bottom, border-left

还有整个边框： [border](###border###)

#### 8.3.7 圆角边框 ####

可以使用 [border-radius](###border-radius###) 定义一个或两个圆角半径。

圆角的半径是一个圆或椭圆的半径，圆或椭圆的四分之一用作边框的圆角。

图像边框： [border-image-source](###border-image-source###)，同时图像边框也需要边框宽度。

border-image-slice

border-image-width

border-image-outset

border-image-repeat

border-image

### 8.4 轮廓 ###

实际使用中，轮廓一般直接绘制在边框外侧，轮廓与边框的区别：

- 轮廓不占空间
- 轮廓可以不是矩形
- 用户代理通常在元素处于 :focus 状态时渲染轮廓

轮廓样式：[outline-style](###outline-style###)

轮廓宽度：outline-width

轮廓颜色：outline-color

轮廓简写属性： [outline](###outline###)

## 9. 颜色、背景和渐变 ##

### 9.1 颜色 ###

任何元素包括前景色和背景色。

#### 9.1.1 前景色 ####

css属性： [color](###color###)

边框采用前景色的根源在于一个特殊的颜色关键字： currentColor

### 9.2 背景 ###

