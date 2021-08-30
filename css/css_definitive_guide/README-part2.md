# CSS权威指南 #

## CSS属性 ##

### float ###

**取值**：`left | right | none`

**初始值**：none

**适用于**：所有元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### clear ###

**取值**：`left |right | both | none`

**初始值**：none

**适用于**：块级元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### shape-outside ###

**取值**：`none | [<basic-shape> || <shape-box>] | <image>`

**初始值**：none

**适用于**：浮动元素

**计算值**：视情况而定

**继承性**：:x:

**动画性**：`<basic-shape>`

### shape-image-threshold ###

**取值**：`<number>`

**初始值**：0.0

**适用于**：浮动元素

**计算值**：于指定的值相同

**继承性**：:x:

**动画性**：:heavy_check_mark:

### shape-margin ###

**取值**：`<length>|<percentage>`

**初始值**：0

**适用于**：浮动元素

**计算值**：绝对长度

**继承性**：:x:

**动画性**：:heavy_check_mark:

### position ###

**取值**：`static | relative | sticky | absolute | fixed`

**初始值**：static

**适用于**：所有元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### top ###

**取值**：`<length>|<precentage>|auto`

**初始值**：auto

**适用于**：定位元素

**计算值**：相对于容纳块的高度计算

**继承性**：:x:

**动画性**：`<length>,<precentage>`

### min-width ###

**取值**：`<length>|<precentage>`

**初始值**：0

**适用于**：特定的所有元素

**计算值**：相对于容纳块的宽度计算。

**继承性**：:x:

**动画性**：`<length>,<precentage>`

### overflow ###

**取值**：`visible|hidden|scroll|auto`

**初始值**：visible

**适用于**：块级元素和置换元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### visibility ###

**取值**：`visible|hidden|collapse`

**初始值**：visible

**适用于**：所有元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### z-index ###

**取值**：`<integer>|auto`

**初始值**：auto

**适用于**：定位元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### flex-direction ###

**取值**：`row|row-reverse|column|column-reverse`

**初始值**：row

**适用于**：弹性容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### flex-wrap ###

**取值**：`nowrap|wrap|wrap-reverse`

**初始值**：nowrap

**适用于**：弹性容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### flex-flow ###

**取值**：`<flex-direction> || <flex-wrap>`

**初始值**：row nowrap

**适用于**：弹性容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### justify-content ###

**取值**：`flex-start|flex-end|center|space-between|space-around|space-evenly`

**初始值**：flex-start

**适用于**：弹性容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### align-items ###

**取值**：`flex-start|flex-end|center|baseline|stretch`

**初始值**：stretch

**适用于**：弹性容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### align-self ###

**取值**：`auto|flex-start|flex-end|center|baseline|stretch`

**初始值**：auto

**适用于**：弹性元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### align-content ###

**取值**：`flex-start|flex-end|center|space-between|space-around|space-evenly|stretch`

**初始值**：stretch

**适用于**：弹性容器(多行)

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### flex ###

**取值**：`[ <flex-grow> <flex-shrink> ? || <flex-basis> ] | none`

**初始值**：0 1 auto

**适用于**：弹性元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### flex-grow ###

**取值**：`<number>`

**初始值**：0

**适用于**：弹性元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### flex-shrink ###

**取值**：`<number>`

**初始值**：1

**适用于**：弹性元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### flex-basis ###

**取值**：`content|[<length>|<precentage>]`

**初始值**：auto

**适用于**：弹性元素

**百分数**：相对容器的主轴

**计算值**：指定的值

**继承性**：:x:

**动画性**：`​width​`

### order ###

**取值**：`<integer>`

**初始值**：0

**适用于**：弹性元素以及弹性容器中绝对定位的子元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### grid-template-rows ###

**取值**：`none|<track-list>|<auto-track-list>`

**初始值**：none

**适用于**：栅格容器

**百分数**：相对于容器的轴尺寸计算

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-template-areas ###

**取值**：`none|<string>`

**初始值**：none

**适用于**：栅格容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-row-start ###

**取值**：`auto|<custom-ident>|[<integer>&&<custom-ident>?]|[span&&[<integer>||<custom-ident>]]`

**初始值**：auto

**适用于**：栅格元素和绝对定位元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-row ###

**取值**：`<grid-line>[/<grid-line>]?`

**初始值**：auto

**适用于**：栅格元素和绝对定位元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-area ###

**取值**：`<grid-line>[/<grid-line>]{0,3}`

**初始值**：见各个单独的属性

**适用于**：栅格元素和绝对定位元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-auto-flow ###

**取值**：`[row|column] || dense`

**初始值**：row

**适用于**：栅格容器

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### grid-auto-rows ###

**取值**：`<track-breadth>|minmax(<track-breadth>,<track-breadth>)`

**初始值**：auto

**适用于**：栅格容器

**计算值**：取决于具体的轨道尺寸

**继承性**：:x:

**动画性**：:x:

### grid ###

**取值**：`none|subgird|[<grid-template-rows>/<grid-template-columns>]|[<line-names>? <string> <track-size>? <line-names>?]+ [/ <track-list>]?|[<grid-auto-flow> [<grid-auto-rows> [/ <grid-auto-columns>]?]?]]`

**初始值**：参考各单独属性

**适用于**：栅格容器

**计算值**：参考各单独属性

**继承性**：:x:

**动画性**：:x:

### grid-row-gap ###

**取值**：`<length>|<percentage>`

**初始值**：0

**适用于**：栅格容器

**计算值**：绝对长度

**继承性**：:x:

**动画性**：:heavy_check_mark:

### grid-gap ###

**取值**：`<grid-row-gap> <grid-column-gap>`

**初始值**：0 0

**适用于**：栅格容器

**计算值**：声明的值

**继承性**：:x:

**动画性**：:heavy_check_mark:

### caption-side ###

**取值**：`top|bottom`

**初始值**：top

**适用于**：display属性为table-caption的元素

**计算值**：声明的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### border-collapse ###

**取值**：`collapse|separate|inherit`

**初始值**：separate

**适用于**：display属性为table或者table-inline的元素

**计算值**：声明的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### border-spacing ###

**取值**：`<length> <length>?`

**初始值**：0

**适用于**：display属性为table或者table-inline的元素

**计算值**：两个绝对长度

**继承性**：:heavy_check_mark:

**动画性**：:heavy_check_mark:

### empty-cells ###

**取值**：`show|hide`

**初始值**：show

**适用于**：display属性为table-cell的元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### table-layout ###

**取值**：`auto|fixed`

**初始值**：auto

**适用于**：display属性为table或者table-inline的元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### list-style-type ###

**取值**：`disc|circle|square|...`

**初始值**：disc

**适用于**：display属性为list-item的元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### list-style-image ###

**取值**：`<uri>|<image>|none|inherit`

**初始值**：none

**适用于**：display属性为list-item的元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### list-style-position ###

**取值**：`inside|outside|inherit`

**初始值**：outside

**适用于**：display属性为list-item的元素

**计算值**：指定的值

**继承性**：:heavy_check_mark:

**动画性**：:x:

### Transform ###

**取值**：`<transform-list>|none`

**初始值**：None

**适用于**：除 "基元行内" 框之外的所有元素

**计算值**：声明的值

**继承性**：:x:

**动画性**：作为一种变形

### transform-origin ###

**取值**：`[left|center|right|top|bottom|<precentage>|<length>]|[left|center|right|top|bottom|<precentage>|<length>]&&[left|center|right|top|bottom|<precentage>|<length>]]<length>?`

**初始值**：50% 50%

**适用于**：任何可变性的元素

**计算值**：计算为一个百分数；值为长度值时，计算为绝对长度

**继承性**：:x:

**动画性**：`<length>,<percentage>`

### transform-style ###

**取值**：`flat|preserve-3d`

**初始值**：flat

**适用于**：任何可变性的元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### perspective ###

**取值**：`none|<length>`

**初始值**：none

**适用于**：任何可变性的元素

**计算值**：绝对长度

**继承性**：:x:

**动画性**：:heavy_check_mark:

### backface-visibility ###

**取值**：`visible|hidden`

**初始值**：visible

**适用于**：任何可变性的元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### transition-property ###

**取值**：`none|[all|<property-name>]#`

**初始值**：all

**适用于**：所有元素，以及`:before` 和 `:after` 伪元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### transition-duration ###

**取值**：`<time>#`

**初始值**：0s

**适用于**：所有元素，以及`:before` 和 `:after` 伪元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

### transition-timing-function ###

**取值**：`<time-function>#`

**初始值**：ease

**适用于**：所有元素，以及`:before` 和 `:after` 伪元素

**计算值**：指定的值

**继承性**：:x:

**动画性**：:x:

## 10. 浮动及其形状 ##

### 10.1 浮动 ###

在css中，浮动通过[float](###float###)实现。

#### 10.1.1 浮动的元素 ####

浮动的元素脱离了常规的文档流，不过对布局仍有影响，浮动的元素基本上算是处在单独的平面上。

元素浮动后，其他内容将围绕它流动。

浮动元素四周的外边距不折叠。如果浮动图像有20外边距，图像周围至少有20像素的空白。如果与图像相邻的其他元素也有外边距，那么边距不会与浮动图像的外边距折叠在一起。

如果浮动的是非置换元素，要为元素设定宽度。

#### 10.1.2 浮动详解 ####

浮动元素的容纳块是最近的块级祖辈元素。不管元素是什么类型，浮动后得到的都是块级框。一些规则：

- 浮动元素的外边界不能超过容纳块的内边界。
- 如果在文档中处于前面的元素向左浮动，那么后面的浮动元素的左外边界必定在前一个元素有外边边界的右侧，除非后一个元素的顶边在前一个元素的底边以下。
- 左浮动元素的右外边界不能在右浮动元素的左外边界的右侧。
- 浮动元素的顶边不能比父元素的内顶边高。如果浮动元素位于两个折叠的外边距之间，在两个元素之间放置它的时候，将视其有个块级父元素。
- 浮动元素的顶边不能比前方任何一个浮动元素或块级元素的顶边高。
- 浮动元素的顶边不能高于文档源码中出现在浮动元素之前的元素生成的框体所在的行框的顶边。
- 左浮动元素的左边如果还有一个向左浮动的元素，那么它的右外边界不能再容纳块右边界的右侧。
- 浮动元素必须放在尽可能高的位置上。
- 左浮动元素必须尽量向左移动，右浮动元素必须尽量向右移动。

#### 10.1.3 具体行为 ####

如果浮动的元素太高，不会把父元素撑开，会从父元素的底部冒出来。

浮动元素的后代也浮动时，将扩大范围，涵盖浮动的后代元素。元素随父元素一起浮动。

背景与文档中靠前的浮动元素之间的关系。

**负外边距对浮动的影响**

负外边距将导致浮动元素移动到父元素的外面，由于内容的外移。

#### 10.1.4 浮动元素与内容重叠 ####

内容流动方向那一侧的外边距为负值时。

- 行内框与浮动元素重叠时，其边框，背景和内容都在浮动元素之上渲染。
- 块级框与浮动元素重叠时，其边框和背景在浮动元素背后渲染，而内容在浮动元素之上渲染。

### 10.2 清除浮动 ###

要禁止每个区域的第一个元素出现在浮动元素旁边，如果第一个元素在浮动元素旁边，它的位置会下移到浮动元素的下方，使用 [clear](###clear###)清除浮动。

声明 `h3 {clear:left;}` 的意思可以理解为 确保h3元素的左边远离浮动图像。

css2.1 引入来了间距 (clearane) 这个概念。

浮动框的边界由浮动元素外边距的边界划定。

### 10.3 浮动形状 ###

CSS Shapes

#### 10.3.1 定义形状 ####

规定浮动元素周围的内容按什么形状流动：[shape-outside](###shape-outside###)

设为image时，内容将流入浮动元素的透明区域。

basic-shape的基本类型可以是以下一个：

- `inset()` 内凹形状，可以设置每个边的值。
- `circle()`
- `ellipse()`
- `polygon()`：设置多边形形状。

basic-box的值可以是下面的一个：

- margin-box
- border-box
- padding-box
- content-box

#### 10.3.2 使用透明图像定义形状 ####

用于指定透明度为多少时允许内容流入：[shape-image-threshold](###shape-image-threshold###) 不透明度为多少时算在浮动元素形状内。

还可以为形状添加外边框：[shape-margin](###shape-margin###)，但是形状绝不会超过形状框，不会超过外边距。

## 11. 定位 ##

### 11.1 基本概念 ###

#### 11.1.1 定位的类型 ####

定位类型使用[position](###position###)属性指定。

- static: 正常生成元素框。
- relative：元素框偏移一定的距离。元素的形状与未定位时一样，而且元素所占的空间也与正常情况下相同。
- absolute：元素框完全从文档流中移除，相对容纳块定位。正常情况下元素在文档流中占据的空间不复存在，定位后生成的都是块级框。
- fixed：元素框的行为类似于absolute，不过容纳块是视区自身。
- sticky：元素一开始在常规的文档流中，达到触发粘滞的条件时，从常规的文档流中移除，不过在常规文档流中占据的空间得以保留。

#### 11.1.2 容纳块 ####

对非根元素来说，如果position属性的值是relative或static，其容纳块由最近的块级元素的内容边界划定。

对非根元素来说，如果position属性为absolute，其容纳块是position属性的值不是static的最近的祖辈元素(任何类型)，具体规则如下：

- 如果祖辈是块级元素，容纳块是那个元素的内边距边界，由边框限定的区域。
- 如果祖辈是行内元素，容纳块是祖辈元素的内容边界。
- 如果没有祖辈元素，元素的容纳块是初始容纳块。

### 11.2 偏移属性 ###

用四个属性指定定位元素的各边相对容纳块的偏移：[top](###top###),right,bottom,left.

指定距容纳块最近的边的偏移。可以为正，可以为负。

定位元素的外边距边界偏移后，元素的一切都随之移动。

### 11.3 宽度和高度 ###

#### 11.3.1 设定宽度和高度 ####

使用width和height设定元素的宽和高。

如果使用四个条件限定了元素的位置，那么就不需要height和width的值。

需要考虑内边距，边框和外边距对元素大小的影响。

或者调整元素的box-sizing属性为border-box

```css
position: absolute;top: 0;left: 0;bottom: 0;right: 50%;width: 50%;height: 100%;padding: 2em;
```

以上元素会超出容纳块的边界。

#### 11.3.2 限制宽度和高度 ####

有四个属性：[min-width](###min-width###),min-height,max-width,max-height，这些属性不能为负值。

### 11.4 内容溢出和裁剪 ###

#### 11.4.1 溢出 ####

使用[overflow](###overflow###)处理内容的溢出

- scroll：元素的内容在元素框的边界处裁剪。
- hidden：元素的内容将在元素框的边界处裁剪。

### 11.5 元素的可见性 ###

控制整个元素的可见性：[visibility](###visibility###)

在不可见的状态下，元素依然影响文档布局。`display:none` 导致元素不显示，完全从文档中移除。

三个控制可见的区别：

- `display:none`
- `visibility:hidden`
- `opacity:0`

### 11.6 绝对定位 ###

#### 11.6.1 绝对定位元素的容纳块 ####

绝对定位元素不围绕其他元素的内容流动，而且其内容也不围绕定位元素流动。

应该把容纳块position的值设置为relative。

确保body元素是所有后代元素的容纳块，而不让用户代理自行选择初始容纳块： `body {position:relative;}`

绝对定位元素是其后代元素的容纳块。

#### 11.6.3 自动确定边界的位置 ####

- `top:auto;left:0;` 定位元素的顶边将与没有定位时的顶边位置对齐。
- `top:auto;left:auto;` 将与未定位时的位置一样，只不过不占空间的感觉。

#### 11.6.4 非置换元素的位置和尺寸 ####

元素个宽度设为 自动缩放，因此元素内容区的宽度将恰好能放得下内容。非静态定位属性设为auto的意思是占据余下的距离。

```css
top: 0;
left: 1em;
right: 1em;
width: 10em;
margin: 0 auto;
```

当为定位元素的margin-left margin-right设为auto时，元素居中显示，与在常规文档中把外边距设为auto居中显示元素的原理基本一样。这种情况下浏览器将忽略right属性声明的值，补上差值。

当只有一个margin设为auto值得时候，将通过那个属性补足本节前面给出的等式。

#### 11.6.5 置换元素的位置和尺寸 ####

1. 如果width设为auto，width的具体值由元素内容的内在宽度确定。
2. 在从左至右书写的语言中，如果left的值是auto，auto将替换为静态位置。
3. 如果left或right的值仍然是auto，把margin-left或者margin-right的auto值替换为0
4. 如果此时margin-left或者margin-right的值仍然为auto，把二者设为相等的值
5. 如果还有一个属性的值为auto，修改为满足等式所需的值。

#### 11.6.6 Z轴上的位置 ####

[z-index](###z-index###)用于调整元素之间重叠的方式。

z-index的值越大，元素离读者的距离越近。

不管z-index多大，都显示在父元素前面。

### 11.7 固定定位 ###

固定定位元素的容纳块是视区。

`{position:fixed;}`

### 11.8 相对元素 ###

相对元素使用偏移属性移动元素。

在相对定位中，元素从常规的位置移开了，但是其占据的空间并没有消息。

过约束的情况：相对定位出现过约束，把其中一个值设为另一个值得相反数。

## 12. 弹性盒布局 ##

CSS Flexiable Box Module Level1: Flexbox

### 12.1 弹性盒基础 ###

指明空间的分布方式，内容的对齐方式和元素的视觉顺序。

弹性盒布局，能让元素对不同元素对不同的屏幕尺寸和不同的显示设备做好适应准备。

弹性盒依赖父子关系。在元素上声明 `display:flex` `display:inline-flex` 便激活弹性盒布局。这个元素变成弹性容器(flex container), 子元素称为弹性元素 (flex item)。

- `display:flex`生成的是块级框。弹性元素在其中布局。
- `display:inline-flex` 行内块级框。

只有直接子元素使用弹性盒布局，其他后代元素不受影响。

弹性盒的目的是实现一维布局。

### 12.2 弹性容器 ###

弹性容器中的绝对定位子元素也是弹性元素，不过确定其尺寸和位置时，将其视为弹性容器中的唯一弹性元素。

#### 12.2.1 flex-direction ####

控制排布弹性元素的主轴：[flex-direction](###flex-direction###)

需要弄清楚该属性和书写模式 `writing-mode` `direction` `text-orientation` 之间的关系。

#### 12.2.3 换行 ####

如果弹性元素在弹性容器的主轴上放不下，默认情况下弹性元素不会换行，也不会自行调整尺寸。将会从容器框的边界溢出。

可以通过[flex-wrap](###flex-wrap###)修改此行为：

- wrap: 往垂轴方向换行
- wrap-reverse: 往垂轴相反的方向换行。

#### 12.2.4 定义弹性流 ####

[flex-flow](###flex-flow###) 定义主轴和垂轴的方向，以及是否允许弹性元素换行。

**深入理解各种轴**

弹性元素沿着主轴排布，各行弹性元素沿着垂轴的方向添加。

- 主轴：内容沿着此轴流动。
- 主轴尺寸：主轴方向上内容的总长度
- 主轴起边：
- 主轴终边
- 垂轴：块级元素沿着此轴堆叠
- 垂轴尺寸
- 垂轴起边
- 垂轴终边

### 12.3 布置弹性元素 ###

有三个属性：`justify-content` `align-content` `align-items`

### 12.5 调整内容 ###

[justify-content](###justify-content###)属性指明在弹性容器的主轴上如何分布各行里的弹性元素，应用于弹性容器。

如何把弹性容器的空间分配到弹性元素的四周或者弹性元素之间。

该属性还影响弹性元素如何从弹性容器中溢出。

### 12.6 对齐元素 ###

[align-items](###align-items###) 定义弹性元素在垂轴方向上的对齐方式，应用于弹性容器：

- stretch：所有可拉伸的弹性元素将与所在行中最高或者最宽的弹性元素一样高或一样宽。不过 min-height ... width height 属性优先级更高。
- baseline：一行中的弹性元素向第一条基线对齐。

单独对齐某个弹性元素：[align-self](###align-self###)

### 12.8 对齐内容 ###

[align-content](###align-content###)属性定义弹性容器有额外的空间时在垂轴方向上如何对齐各弹性元素行，以及空间不足以放下所有弹性元素行时从哪个方向溢出。

指定垂轴方向上的额外空间如何分配到弹性元素行之间和周围。

如果弹性元素行从弹性容器中溢出：

- flex-start, space-between, stretch 将从垂轴终边一侧溢出。
- space-around, center 将从垂轴两边溢出。
- flex-end 将从垂轴起边溢出。

### 12.9 弹性元素 ###

对于弹性容器中的文本子节点来说，如果文本节点不是空的,将放在一个匿名弹性元素中，其行为与其它同辈弹性元素一样。

#### 12.9.2 弹性元素的特性 ####

弹性元素的外边距不折叠。

float和clear对弹性元素不起作用，不会把弹性元素移出文档流。但对框体的生成仍然有影响，因为display属性的计算值受它影响。

绝对定位弹性容器的子元素，将从文档流中移除。绝对定位的弹性元素不再参与弹性布局。但这些元素将受应用在弹性容器上的样式影响。

order属性对弹性容器中绝对定位的子元素的位置没有影响，但是对同辈元素的绘制顺序有影响。

#### 12.9.3 最小宽度 ####

对于弹性元素来说，未设定min-width时，默认为auto，而不是0。

如果设置的min-width值比auto的计算值小，那么在不换行的情况下，元素将比实际内容的宽度小。

### 12.10 弹性元素的属性 ###

弹性元素的对齐方式，顺序和弹性(flexibility) 

简写属性flex，以及构成它的flex-grow, flex-shrink, flex-basis 属性用于控制弹性元素的弹性。在主轴方向上可以增加或缩减多少尺寸。

### 12.11 flex属性 ###

能把弹性元素变得具有弹性，即在主轴方向上调整元素的宽度或者高度，占满可用空间。弹性容器根据弹性增长因子 (flex grow factor) 按比例分配额外的空间，或者根据弹性缩减因子 (flex shrink factor) 按比例缩小弹性元素。

增长因子和缩减因子由弹性元素的flex属性声明：[flex](###flex###)

弹性元素所在的框体尺寸由flex确定，而不是确定主轴尺寸大小的属性。flex属性包括增长因子、缩减因子和弹性基准。

弹性基准指明如何应用弹性增长因子和弹性缩减因子。

### 12.12 flex-grow属性 ###

有多余的空间时是否允许弹性元素增大，以及允许增大且有多余的空间时，相对其他同辈元素以什么比例增大。

[flex-grow](###flex-grow###)

弹性容器中有多余的空间，多出的空间将根据各弹性元素的增长因子按比例分配给各个弹性元素。

- 线计算可用空间。
- 算出总共的增长因子大小，算出每一份所占的宽度。
- 弹性增长时，根据原宽度和每一份得到的宽度相加，得出最后的宽度。

#### 12.12.1 在flex中属性中设定增长因子 ####

如果flex和flex-grow都没有声明，增长因子默认为0。

当只声明flex-grow时，弹性基准默认为auto。

flex默认缩减因子为1，默认基准为0%

如果flex属性通过计算得出的弹性基准为0%，而且增长因子为0，那么元素的尺寸在主轴上将缩小为内容允许的最小长度，或者更小一点。

如果flex属性的增长因子都允许增大，而且弹性基准为0%，那么所有空间将按比例分配。

### 12.13 flex-shrink属性 ###

[flex-shrink](###flex-shrink###)指定弹性缩减因子。默认数值是1.

缩减因子定义空间不足以放下所有弹性元素时，当前弹性元素将缩小多少。

情况：容器不能增大尺寸或者不能换行时如何分配 “缺少的空间”。

计算方式：需要缩减的量按比例分配到每个可缩减的元素上面。

如果弹性元素中的内容不能换行，也不能在主轴方向上缩小，那么弹性元素无法进一步缩小。

#### 12.13.1 根据宽度和缩减因子按比例缩小 ####

在各个弹性元素宽度不相等的情况下，根据缩减因子和元素的宽度按比例缩小。

$缩小比例=\frac{缺少的空间}{宽度1\times缩减因子1 + ... + 宽度1\times缩减因子1}$

然后减去缩小比例乘上份数的宽度。

#### 12.13.2 不同的基准 ####

缩减因子为任何正数都会导致内容换行。

缩减因子的占比还会影响内容的换行次数。

#### 12.13.3 响应式弹性布局 ####

```css
nav {flex: 0 1 200px;min-width: 150px;}
article {flex: 1 2 600px;}
aside {flex: 0 1 200px;min-width: 150px;}
```

### 12.14 flex-basis 属性 ###

弹性元素的尺寸受内容以及盒模型的影响，而且可以通过flex属性的三个要素重置。

flex属性中的 [flex-basis](###flex-basis###) 定义弹性元素的初始尺寸。

在弹性因子分配多余或者缺少的空间前，弹性容器的大小。

弹性基准设定弹性元素的元素框(由box-sizing设置)

#### 12.14.1 content关键字 ####

#### 12.14.2 自动确定弹性基准 ####

设为auto时，flex-basis等于元素在主轴方向上的尺寸，就像没有把元素变成弹性元素一样。

在弹性基准值为auto的情况下：

- 如果width的值是长度，弹性基准等于那个长度。
- 如果width是auto，那么弹性基准回落为content。

在不声明flex-basis和flex的情况下，基准为默认值auto：

- 那么弹性基准的计算值为个元素的width

当基准设置为特定的长度值时：

- 如果设置了width值，那么弹性基准优先级比width高。但是不会比`min-width`的优先级高

弹性基准的百分数相对于主轴尺寸计算。

#### 12.14.5 零基准 ####

如果声明了flex，但是没有设定基准的值，那么弹性基准默认为0。

基准为0时，弹性容器的尺寸根据增长因子按比例分给各个弹性元素。但是还是会受到min-width的影响。

### 12.15 flex属性简写 ###

- initial: 这个值根据width属性确定弹性元素的尺寸，允许缩小。
- auto：这个值根据width属性确定弹性元素的尺寸，允许缩小或者增大。
- none: 这个值根据width属性确定弹性元素的尺寸，不允许缩小或者增大，没有弹性。
- `<number>` : 增长因子设为number，缩小银子设为0，基准设为0。这意味width属性的值相当于最小尺寸，弹性元素在有多余的空间时将增大。

### 12.16 order属性 ###

css属性： [order](###order###)

## 13. 栅格系统 ##

### 13.1 创建栅格容器 ###

第一步：定义一个栅格容器(grid container), 栅格容器为其中的内容定义一个栅格格式化上下文(grid formatting context).

栅格容器的子元素是栅格元素(grid item)。

栅格有两种：常规栅格(grid)和行内栅格(inline-grid)。

栅格容器不是块级容器：

- 浮动元素不会打乱栅格容器。

- 栅格容器的外边距不与其后代的外边距折叠。

有些css属性和功能不能用在栅格容器和栅格元素上：

- 栅格容器的column属性都被忽略
- 栅格容器没有 `::first-line` 和 `::first-letter` 伪元素。
- 栅格元素上的float和clear属性被忽略
- vertical-align属性对栅格元素不起作用。

### 13.2 基本概念 ###

栅格元素是在栅格格式化上下文中参与栅格布局的东西。可以是子元素也可以是匿名文本。

- 栅格线。

- 栅格轨道(grid track)：指两条相邻的栅格线之间夹住的整个区域，栅格轨道的尺寸由栅格线的位置确定。
- 栅格单元(grid cell)：值四条栅格线限定的区域。这是栅格布局中区域的最小单位。没有属性能把一个栅格元素放在指定的栅格单元里。
- 栅格区域(grid area): 任何四条栅格线限定的矩形区域。

栅格元素可以重叠，栅格线可以重叠。

如果栅格元素在轨道的外部，那么栅格系统将会自动天剑栅格线和轨道。

### 13.3 放置栅格线 ###

[grid-template-rows](###grid-template-rows###), grid-template-columns属性可以大致定义栅格模板(grid template, CSS规范称之为explicit grid, 显式栅格)中栅格线。

栅格线始终可以使用数字，也可以为其命令。

#### 13.3.1 宽度固定的栅格轨道 ####

栅格线之间的距离不随栅格轨道中的内容的变化而变化。

```css
.d-grid {
    display: grid; 
    grid-template-columns: 200px 50% 100px; 
}
```

```css
.d-grid {
    display: grid;
    /*grid-template-columns: 200px 50% 100px;*/
    grid-template-columns: [start col-a] 200px [col-b] 50% [col-c] 100px [stop end last];
}
```

如上，给栅格线命名：行和列不共用命令空间。

```css
grid-template-rows: [start masthead] 3em [content] 100% [footer] 2em [stop end];
```

以上声明方式行轨道将被完全推到容器外部。这种问题的处理方式之一：为行的尺寸设定极值，指明最大值和最小值：

```css
grid-template-rows: [start masthead] 3em [content] minmax(3em, 100%) [footer] 2em [stop end];
```

以上得出，行的高度将会在3em和容器的高低之间。

第二种方式是使用 calc进行计算。

#### 13.3.2 弹性栅格轨道 ####

弹性栅格轨道的尺寸基于弹性容器中非弹性轨道以外的空间确定，或者基于整个轨道中的具体内容而定。

**份数单位**

`fr`单位

```css
grid-template-columns: [A] 1fr [B] 1fr [C] 1fr [D] 1fr [E];
```

可用空间除以fr值之和，个轨道的尺寸等于fr值所对应的份数。

```css
grid-template-columns: 15em 1fr 10%;
```

先为第一个和第三个轨道分配固定的宽度，余下的空间都分给第二个轨道。

minmax表达式的最小值部分不允许使用fr单位。

**根据内容设定轨道的尺寸**

可以使用 min-content 和 max-content。

max-content：占据内容所需的最大空间。

这两个关键字的特性：将应用于整个栅格轨道上，如果把一列的尺寸设为max-content, 那么整个轨道的宽度都与列中最宽的内容一样。

每个列轨道的宽度都与轨道中最宽的图像相等。

还有一个关键字auto，用作最小值时，视作栅格元素的最小尺寸，既有min-width或min-height定义的值。

#### 13.3.3 根据轨道中的内容适配 ####

还可以使用 `fit-content()` 函数以简练的方式表达特定类型的尺寸模式。

该函数参数为一个长度或者一个百分数。

```css
grid-template-columns: 2fr fit-content(150px) 2fr;
grid-template-columns: 2fr fit-content(50%) 2fr;

fit-content(argument) => min(max-content, max(min-content, argument))
```

先从min-content和argument中找出较大的那个值，然后与max-content的值相比，找出较小的。

fit-content参数设定的值是上限，而不是定值。

#### 13.3.4 重复栅格线 ####

使用`repeat()`

例如，想每隔5em放置一列栅格线，一共有10个列轨道，第一个所示：

```css
grid-template-columns: repeat(10, 5em);
grid-template-columns: repeat(3, 2em 1fr 1fr);
grid-template-columns: repeat(3, 2em 1fr 1fr) 2em;
grid-template-columns: repeat(4, 10px [col-start] 250px [col-end]) 10px;
```

**自动填充的轨道**

有两个关键字： auto-fit 和 auto-fill

直到填满整个栅格轨道容器为止：

```css
grid-template-columns: repeat(auto-fill, [top] 5em [bottom]);
```

局限：只能有一个可选的栅格线名称、一个尺寸固定的轨道和另一个可选的栅格线名称。

但是如果使用auto-fit，没有栅格元素的轨道将被剔除。剔除轨道后留下的空间根据 align-content和justify-content的值处理。

#### 13.3.5 栅格区域 ####

属性：[grid-template-areas](###grid-template-areas)

```css
grid-template-areas: 
        "h h h h" 
        "l c c r"
        "l f f f";
```

这样，每个标识符表示一个栅格单元。

如果只想把部分栅格单元定义为栅格区域的一部分，可以使用一个或者多个 `.` 字符占位。

该属性和 grid-template-columns，gird-templdate-rows一起使用，可以使具名栅格区域创建的列和行有轨道尺寸。如果提供的轨道尺寸数量比区域轨道多，多出的轨道将放在具名区域后面。

命名栅格区域会自动为首尾两条栅格线命名。 `xx-start` `xx-end`

这种隐式命名机制还可以方向操作：

```css
grid-template-columns: [header-start footer-start] 1fr [content-start] 1fr [content-end] 1fr [header-end footer-end];
grid-template-rows: [header-start] 3em [header-end content-start] 1fr [content-end footer-start] 3em [footer-end];
```

### 13.4 在栅格中附加元素 ###

#### 13.4.1 使用列线和行线 ####

把元素附加到栅格线上的四个属性： [grid-row-start](###grid-row-start###), grid-row-end, grid-column-start, grid-column-end

如果省略结束栅格线，那么结束栅格线使用序列中的下一条栅格线。

```css
.one {
    grid-row-start: 2;
    grid-row-end: 4;
    grid-column-start: 2;
    grid-column-end: 4;
    background-color: green;
}
.two {
    grid-row-start: 1;
    grid-row-end: 3;
    grid-column-start: 5;
    grid-column-end: 10;
    background-color: red;
}
.three {
    grid-row-start: 4;
    /*grid-row-end: 5;*/
    grid-column-start: 6;
    /*grid-column-end: 7;*/
    background-color: yellow;
}
```

对于三还有一种相同的方式：

```css
grid-row-start: 4;
grid-row-end: span 1;
grid-column-start: 6;
grid-column-end: span 1;
background-color: yellow;
```

span 向确定了编号的栅格线的反方向计数。

栅格线的编号可以使用负值，不过只有通过`grid-template-*`定义的才行

还可以使用编号，如果多条栅格线使用同一个名称，还要加上编号。

此外还有一种引用栅格线名称的方式，通过栅格区域隐式创建的栅格线名称。

#### 13.4.2 行和列的简写属性 ####

相应的简写属性： [grid-row](###grid-row###), grid-column

```css
grid-row: R 3 / 7;
grid-column: col-B / span 2;
```

如果没有斜线的值，结束栅格线取决于开始栅格线的值。栅格元素将从指定名称的栅格线开始一直延伸到下一条同名栅格线。

如果只提供第一个数字，那么第二个数字被设为auto。

`grid-template-areas`的使用方式。

#### 13.4.3 隐式栅格 ####

如果栅格元素(或其一部分)超出了显式定义的栅格呢？

```css
#grid {
    grid-template-columns: repeat(6, 4em);
    grid-template-rows: 2em 2em;
}

.box01 {
    grid-column: 1;
    grid-row: 1 / 4;
}
```

遇到这种情况，浏览器会再创建一条行线。这条栅格线，以及由此而生的一个行轨道都是隐式栅格的一部分。

跨度是从显式栅格开始计数的，然后向隐式栅格延伸，但是不能从隐式栅格开始计数。

#### 13.4.5 使用区域 ####

通过一个属性[grid-area](###grid-area###)引用栅格区域。

这个属性可以和方便的把grid-template-areas声明结合使用。

栅格线值的顺序是：row-start, column-start, row-end, column-end

#### 13.4.6 栅格元素重复 ####

重叠时会分层。

### 13.5 栅格流 ###

如果不明确指定，栅格元素将自动放入栅格中。

在栅格流的作用下，栅格元素将放在第一个适合它的区域中。最简单的情况是，按顺序一个一个把栅格元素放入栅格轨道中。

栅格流主要分为两种模式：行优先和列优先，不过二者都可以通过密集流(denseflow)增强。

栅格流通过[grid-auto-flow](###grid-auto-flow###)设置

栅格流放置的其实是栅格区域，然后再把栅格元素附加到栅格区域中。

### 13.6 自动增加栅格线 ###

当栅格元素超出边界时，根据布局增加所需的行或者列。

控制自动增加的尺寸通过 [grid-auto-rows](###grid-auto-rows###), grid-auto-columns 属性

设定自动创建的行或列轨道时的尺寸时，可以提供一个尺寸值，也可以提供一对极值。

### 13.7 grid简写属性 ###

css属性 [grid](###grid###)

如果定义了栅格模板，那么栅格流和自动增加的轨道的尺寸都归为默认值。

```css
grid:
"header header header header" 3em
". content sidebar ." 1fr
"footer footer footer footer" 5em /
2em 3fr minmax(10em, 1fr) 2em;
```

### 13.8 释放栅格空间 ###

#### 13.8.1 栏距 ####

栏距(gutter)是两个栅格轨道之间的距离。栏距能在栅格单元之间添加间隔。一个轴上只能设定一个间隔值。

栏距使用[grid-row-gap](###grid-row-gap###)和grid-column-gap属性设定。(row-gap, column-gap)

在计算栅格轨道的尺寸时，栏距被视作栅格轨道，因此实际上比例类型的栅格轨道的大小将会变小。

栏距的简写：[grid-gap](###grid-gap###)，现已改名为gap

#### 13.8.2 栅格元素与盒模型 ####

元素在外边距的边界处附加到栅格中。

计算栅格轨道的尺寸时将忽略栅格元素的外边距，这表示，不管栅格元素的外边距多大，都不会改变min-content列的尺寸。

### 13.9 栅格的对齐方式 ###

对其属性的作用:

| 属性            | 对齐的目标               | 适用于   |
| --------------- | ------------------------ | -------- |
| justify-self    | 行内方向上的一个栅格元素 | 栅格元素 |
| justify-items   | 行内方向上的全部栅格元素 | 栅格容器 |
| justify-content | 行内方向上的整个栅格     | 栅格容器 |
| align-self      | 块级方向上的一个栅格元素 | 栅格元素 |
| align-items     | 块级方向上的全部栅格元素 | 栅格容器 |
| align-content   | 块级方向上的整个栅格     | 栅格容器 |

## 14. 表格布局 ##

不管单元格中的内容是什么，一行中的所有单元格都具有相同的高度。在同一列中，单元格的宽度也是一样宽。

### 14.1 表格格式化 ###

了解表格的基本构成，以及表格中元素之间的关系。

#### 14.1.1 表格的视觉排布 ####

表格元素和表格内容元素是两个不同的概念。

在css中，表格内部元素生成矩形框，有内容、内边距和边框，但是没有外边距。

这些规则的基础是单元格，即由绘制表格的栅格线围成的区域。

每个单元格的边界都沿着栅格单元的边界放置。

**表格排布规则**

- 一个行框(row box)包含一个由栅格单元构成的行，表格中的全部行框按出现在文档源码中的顺序从上到下排列。因此，表格中栅格行的数量与行元素的数量相等。
- 一个行组(row group) 框包含的栅格单元就是行组中各行框包含的栅格单元。
- 一个列框(column box)包含一个或多个由栅格单元构成的列。
- 一个列组(column group)框包含的栅格单元就是列组中各列框包含的栅格单元。
- 虽然单元格可能跨多行或多列，但是css没有定义具体方式。这一方面由编写文档的语言完成。
- 单元格的矩形框不能超出表格或行组的最后一个行框。

一列中的所有栅格单元具有相同的宽度。一行中的所有栅格单元具有相同的高度。

#### 14.1.2 设定显示方式的值 ####

- table: 把元素定义为块级表格。 对应 `table`
- inline-table：把元素定义为行内表格。
- table-row：把元素定义为有单元格构成的行。对应 `tr`
- table-row-group: 把元素定义为由一行或多行构成的行组。对应 `tbody`
- table-header-group: 表头行组始终显示在其他行和行组前面，并且显示在上表题后面。对应 `thead`
- table-footer-group: 表脚行组始终显示在其他行和行组后面，并且显示在下表题前面。对应 `tfoot`
- table-column: 把元素声明为由单元格构成的列。对应 `col`
- table-column-group: 把元素声明为有一列或多列构成的列组。对应 `colgroup`
- table-cell: 把元素定义为表格中的一个单元格。 HTML中的 `th` 和 `td` 都是应用table-cell的元素。
- table-caption: 定义表题。

``` css
table {display: table;}
tr {display: table-row;}
thead {display: table-header-group;}
tbody {display: table-row-group;}
tfoot {display: table-footer-group;}
col {display: table-column;}
colgroup {display: table-column-group;}
td, th {display: table-cell;}
caption {display: table-caption;}
```

表格是以行主导的，列则从行中单元格的布局衍生出来。

在css中，行和行组只能应用四个与表格无关的属性：border，background，width，visibility。

#### 14.1.3 匿名表格对象 ####

css定义了一种插入机制：以匿名对象的形式插入 "缺少的" 表格组件。

- 如果table-cell的父元素不是table-row，在table-cell和其父元素之间插入一个匿名的table-row对象。
- 如果table-row元素的父元素不是table，inline-table，table-row-group，在其和其父元素之间插入一个匿名table元素。
- table-column插入table
- table-row-group插入table
- table-row-group的子元素不是table-row，插入table-row。
- table-row的子元素不是table-cell，插入table-cell。

#### 14.1.4 表格中的层 ####

为了完整表示一个表格，css定义了6个独立的层。

从外到内是：单元格，行，行组，列，列组，表格。

#### 14.1.5 表题 ####

[caption-side](###caption-side###)可以把表题放在表格上方或者下方。

表题的宽度由table元素中的内容的宽度决定。

### 14.2 单元格的边框 ###

css中有两种完全不同的边框模型：分离边框模型和折叠边框模型，可以通过[border-collapse](###border-collapse###)设置边框模型。

#### 14.2.1 分离单元格的边框 ####

在这种模型中，表格中的每个单元格都与其他单元格相隔一定的距离，而且单元格之间的边框不会折叠在一起。

把单元格的边框分开以后，还可以让边框相隔一定的距离：[border-spacing](###border-spacing###),第一个值是横向间隔，第二个值是纵向间隔。

间隔值在外侧的单元格和table元素之间也存在。

在分离边框模型中，不能为行，行组，列和列组设定边框。

**处理空单元格**

空单元格的处理方式：[empty-cells](###empty-cells###)

#### 14.2.2 折叠单元格的边框 ####

当border-collapse的值为collapse时：

- table元素不能有内边距，所以表格四周的边框与最外层的单元格之间没有间隔。
- 边框可以应用于单元格，行，行组，列和列组。
- 单元格的边框之间肯定没有间隔。
- 折叠的边框居中放在单元格之间假想的栅格线上。

### 14.3 表格的尺寸 ###

表格的宽度有两种方式：固定宽度布局和自动宽度布局。表格的高度都自动计算。

#### 14.3.1 宽度 ####

[table-layout](###table-layout###)确定宽度的布局方式.

固定布局下，列的宽度由表格的第一行决定，后续各行中的单元格都与第一行确定的列宽度保持一致。

#### 14.3.2 高度 ####

#### 14.3.3 对齐方式 ####

横向对齐单元格中的内容：text-align.

单元格中内容的纵向对齐方式：vertical-align.

## 15. 列表和生成的内容 ##

### 15.1 列表 ###

#### 15.1.1 列表的类型 ####

改变列表项目所用的记号类型，使用[list-style-type](###list-style-type###)

none的作用是禁止在本该显示记号的位置上出现任何内容，不过却不阻断有序列表的计数。

#### 15.1.2 列表项目图像 ####

利用[list-style-image](###list-style-image###)实现图像记号设定。

#### 15.1.3 列表记号的位置 ####

在列表项目内容的外部还是内部显示记号：[list-style-position](###list-style-position###)

## 16. 变形 ##

### 16.1 坐标系 ###

笛卡尔坐标系： x轴左负右正，y轴上负下正，z轴后负前正。

球坐标系：描述3D空间中的角度。

对于旋转来说，2D旋转其实是在绕z轴旋转。

### 16.2 变形 ###

变形的css属性: [Transform](###Transform###)

范围框：边框的框，不包括轮廓和外边距。元素在页面上所占用的空间与变形前保持不变。

`<transform-list>` 表示一个或者多个变形函数。

- 变形函数一次只处理一个，从第一个到最后一个。
- 变形函数有先后顺序关系，不同的先后顺序，结果是不相同的
- 确保每个变形函数的值都正确设置
- 变形通常不叠加，如果改变了元素的形态，而后想再添加一种变形，那么要在原变形的基础上修改。
- 动画变形例外，不管使用过渡还是真正的动画，效果是叠加的。

**变形函数**

- 平移函数`tanslate*()`

- 缩放函数`scale*()`

- 旋转函数`rotate*()`

- 倾斜函数`skew*()`

`matrix*()`

- 视域函数`perspective()`

### 16.3 其他变形属性 ###

#### 16.3.1 移动原点 ####

默认元素以绝对中心为原点。

使用[transform-origin](###transform-origin###)修改这一默认行为。

## 17. 过渡 ##

### 17.1 CSS过渡 ###

css过渡能控制一段时间内属性的值如何变成另一个值。

### 17.2 定义过渡的属性 ###

在css中，过渡使用四个属性定义：

```css
transition-property: color;
transition-duration: 200ms;
transition-timing-function: ease-in;
transition-delay: 50ms;
```

#### 17.2.1 限制受过渡影响的属性 ####

[transition-property](###transition-property###)属性指定想应用过渡效果的CSS属性属性名称。

```css
transition-property: all, border-radius, opacity;
transition-duration: 1s, 2s, 3s;
```

这样可以为少数的属性设置独特的时间、速度或者步调。

可以使用none禁用所有属性的过渡效果。

**过渡事件**

在过渡结束后会触发过渡事件 `transitionend`，简写属性中每个支持动画的属性有各自的过渡事件。

#### 17.2.2 设置过渡持续时间 ####

[transition-duration](###transition-duration###)属性的值事宜逗号分隔的时间长度列表，单位为秒(s)或者毫秒(ms)。

持续时间在100到200毫秒之间的过渡效果最好

#### 17.2.3 调整过渡的内部时序 ####

css属性: [transition-timing-function](###transition-timing-function###)

三次方贝塞尔函数的别名。

**步进时序**

此外，还可以使用步进时序函数。规范预定义了两个步进值

| 时序函数        | 定义                                                 |
| --------------- | ---------------------------------------------------- |
| step-start      | 整个过渡都处在最终关键帧上。等同于 `steps(1, start)` |
| step-end        | 整个过渡都处在初始关键帧上。等同于 `steps(1, end)`   |
| steps(n, start) | 显示n个镜头，其中第一个固定镜头占整个过渡的百分之n   |
| steps(n, end)   | 显示nge固定镜头，前百分之n的时间处于初始值状态       |

如果只在全局状态中声明过渡，所有的属性的变化都会引用同一个过渡属性。

## 18. 动画 ##

### 18.1 定义关键帧 ###

若想为元素添加动画效果，要有一个关键帧，而这有要求有一个具名关键帧动画。

