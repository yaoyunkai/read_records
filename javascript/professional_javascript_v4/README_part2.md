[toc]

# Javascript_Pro_v4 #

## 11 Promise 函数 ##

## 12 BOM ##

### 12.1 window对象 ###

 window 对象在浏览器中有两重身份，一个是ECMAScript 中的 Global 对象，另一个就是浏览器窗口的 JavaScript 接口。这意味着网页中定义的所有对象、变量和函数都以 window 作为其 Global 对象，都可以访问其上定义的 parseInt() 等全局方法。

#### 12.1.1 Global对象 ####

因为 window 对象被复用为 ECMAScript 的 Global 对象，所以通过 var 声明的所有全局变量和函数都会变成 window 对象的属性和方法。

#### 12.1.2 窗口关系 ####

top 对象始终指向最上层（最外层）窗口，即浏览器窗口本身。

而 parent 对象则始终指向当前窗口的父窗口。

如果当前窗口是最上层窗口，则 parent 等于 top （都等于 window ）。

还有一个 self 对象，它是终极 window 属性，始终会指向 window 。实际上， self 和 window 就是同一个对象。之所以还要暴露 self ，就是为了和 top 、 parent 保持一致。

#### 12.1.3 窗口位置与像素比 ####

window 对象的位置可以通过不同的属性和方法来确定。

`screenLeft` 和`screenTop` 属性，用于表示窗口相对于屏幕左侧和顶部的位置 ，返回值的单位是 CSS 像素。

可以使用 moveTo() 和 moveBy() 方法移动窗口。

- 这两个方法都接收两个参数，其中 moveTo() 接收要移动到的新位置的绝对坐标 x 和 y；

- 而 moveBy() 则接收相对当前位置在两个方向上移动的像素数。

**像素比**

CSS 像素是 Web 开发中使用的统一像素单位。

这个物理像素与 CSS 像素之间的转换比率由`window.devicePixelRatio` 属性提供。

window.devicePixelRatio 实际上与每英寸像素数（DPI，dots per inch）是对应的。

DPI 表示单位像素密度，而 window.devicePixelRatio 表示物理像素与逻辑像素之间的缩放系数。

#### 12.1.4 窗口大小 ####

- `innerWidth` `innerHeight` 返回浏览器窗口中页面视口的大小（不包含浏览器边框和工具栏）。

- `outerWidth` `outerHeight` 返回浏览器窗口自身的大小（不管是在最外层 window 上使用，还是在窗格 <frame> 中使用）。
- `document.documentElement.clientWidth`  `document.documentElement.clientHeight` 返回页面视口的宽度和高度

```js
    let pageWidth = window.innerWidth,
        pageHeight = window.innerHeight;
    if (typeof pageWidth != "number") {
        if (document.compatMode == "CSS1Compat") {
            pageWidth = document.documentElement.clientWidth;
            pageHeight = document.documentElement.clientHeight;
        } else {
            pageWidth = document.body.clientWidth;
            pageHeight = document.body.clientHeight;
        }
    }
```

 resizeTo() 和 resizeBy() 方法调整窗口大小。

#### 12.1.5 视口位置 ####

浏览器窗口尺寸通常无法满足完整显示整个页面，为此用户可以通过滚动在有限的视口中查看文档。

度量文档相对于视口滚动距离的属性有两对，返回相等的值： 

`window.pageXoffset` / `window.scrollX` 和 `window.pageYoffset` / `window.scrollY` 。

可以使用 scroll() 、 scrollTo() 和 scrollBy() 方法滚动页面。

```js
// 相对于当前视口向下滚动 100 像素
window.scrollBy(0, 100);

// 相对于当前视口向右滚动 40 像素
window.scrollBy(40, 0);

// 滚动到页面左上角
window.scrollTo(0, 0);

// 滚动到距离屏幕左边及顶边各 100 像素的位置
window.scrollTo(100, 100);

// 正常滚动
window.scrollTo({
left: 100,
top: 100,
behavior: 'auto'
});

// 平滑滚动
window.scrollTo({
left: 100,
top: 100,
behavior: 'smooth'
});
```

#### 12.1.6 导航与打开新窗口 ####

window.open() 方法可以用于导航到指定 URL，也可以用于打开新浏览器窗口。这个方法接收 4个参数：要加载的 URL、目标窗口、特性字符串和表示新窗口在浏览器历史记录中是否替代当前加载页面的布尔值。

第二个参数也可以是一个特殊的窗口名，比如 `_self`  `_parent`  `_top` 或 `_blank` 。

特性字符串是一个逗号分隔的设置字符串，用于指定新窗口包含的特性。

```js
window.open("http://www.wrox.com/",
    "wroxWindow",
    "height=400,width=400,top=10,left=10,resizable=yes");
```

window.open() 方法返回一个对新建窗口的引用。

新创建窗口的 window 对象有一个属性 opener ，指向打开它的窗口。这个属性只在弹出窗口的最上层 window 对象（ top ）有定义，是指向调用 window.open() 打开它的窗口或窗格的指针。

**3. 弹窗屏蔽程序**

如果浏览器内置的弹窗屏蔽程序阻止了弹窗，那么 window.open() 很可能会返回 null 。

在浏览器扩展或其他程序屏蔽弹窗时， window.open() 通常会抛出错误。

```js
let blocked = false;

try {
    let demo = window.open("http://www.wrox.com", '_blank');
    if (demo == null) {
        blocked = true
    }
} catch (e) {
    blocked = true;
}

if (blocked) {
    alert("The popup was blocked!")
}
```

#### 12.1.7 定时器 ####

setTimeout() 用于指定在一定时间后执行某些代码，而 setInterval() 用于指定每隔一段时间执行某些代码。

setTimeout() 方法通常接收两个参数：要执行的代码和在执行回调函数前等待的时间（毫秒）。

```js
setTimeout(() => alert("Hello world!"), 1000);
```

如果队列是空的，则会立即执行该代码。如果队列不是空的，则代码必须等待前面的任务执行完才能执行。

调用 setTimeout() 时，会返回一个表示该超时排期的数值 ID。

要取消等待中的排期任务，可以调用 clearTimeout() 方法并传入超时 ID。

```js
// 设置超时任务
let timeoutId = setTimeout(() => console.log("Hello world!"), 1000);
// 取消超时任务
clearTimeout(timeoutId);
```

所有超时执行的代码（函数）都会在全局作用域中的一个匿名函数中运行，因此函数中的 this 值在非严格模式下始终指向 window ，而在严格模式下是 undefined 。如果给 setTimeout() 提供了一个箭头函数，那么 this 会保留为定义它时所在的词汇作用域。

setInterval() 方法也会返回一个循环定时 ID，可以用于在未来某个时间点上取消循环定时。要取消循环定时，可以调用 clearInterval() 并传入定时 ID。

```js
let num = 0, intervalId = null;
let max = 10;

let incrementNumber = function () {
    num++;

    if (num == max) {
        clearInterval(intervalId);
        console.log('done...')
    }
}

intervalId = setInterval(incrementNumber, 500);

let num = 0;
let max = 10;
let incrementNumber = function () {
    num++;
	// 如果还没有达到最大值，再设置一个超时任务
    if (num < max) {
        setTimeout(incrementNumber, 500);
    } else {
        alert("Done");
    }
}
setTimeout(incrementNumber, 500);
```

注意在使用 setTimeout() 时，不一定要记录超时 ID，因为它会在条件满足时自动停止，否则会自动设置另一个超时任务。这个模式是设置循环任务的推荐做法。

#### 12.1.8 系统对话框 ####

使用 alert() 、 confirm() 和 prompt() 方法，可以让浏览器调用系统对话框向用户显示消息。

### 12.2 location对象 ###

location 是最有用的 BOM对象之一，提供了当前窗口中加载文档的信息，以及通常的导航功能。这个对象独特的地方在于，它既是 window 的属性，也是 document 的属性。

假 设 浏 览 器 当 前 加 载 的 URL 是 `http://foouser:barpassword@www.wrox.com:80/WileyCDA/?q=javascript#contents`， location 对象的内容如下表所示。

| 属性              | 值                                                     | 说明                                                         |
| ----------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| location.hash     | #contents                                              | URL 散列值（井号后跟零或多个字符），如果没有则为空字符串     |
| location.host     | www.wrox.com:80                                        | 服务器名及端口号                                             |
| location.hostname | www.wrox.com                                           | 服务器名                                                     |
| location.href     | http://www.wrox.com:80/WileyCDA/?q=javascript#contents | 当前加载页面的完整 URL。 location 的 toString()方法返回这个值 |
| location.pathname | /WileyCDA/                                             | URL 中的路径和（或）文件名                                   |
| location.port     | 80                                                     | 请求的端口。如果URL中没有端口，则返回空字符串                |
| location.protocal | http:                                                  | 页面使用的协议                                               |
| location.search   | ?q=javascript                                          | URL 的查询字符串。这个字符串以问号开头                       |
| location.username |                                                        |                                                              |
| location.password |                                                        |                                                              |
| location.origin   | http://www.wrox.com                                    | URL 的源地址。只读                                           |

#### 12.2.1 查询字符串 ####

#### 12.2.2 操作地址 ####

可以通过修改 location 对象修改浏览器的地址。首先，最常见的是使用 assign() 方法并传入一个 URL，如下所示：

```js
location.assign("http://www.wrox.com");
```

这行代码会立即启动导航到新 URL 的操作，同时在浏览器历史记录中增加一条记录。如果给`location.href` 或 `window.location` 设置一个 URL，也会以同一个 URL 值调用 assign() 方法。

```js
window.location = "http://www.wrox.com";
location.href = "http://www.wrox.com";
```

在这 3 种修改浏览器地址的方法中，设置 location.href 是最常见的。只要修改 location 的一个属性，就会导致页面重新加载新 URL。

修改 hash 的值会在浏览器历史中增加一条新记录。

如果不希望增加历史记录，可以使用 replace() 方法。这个方法接收一个 URL 参数，但重新加载后不会增加历史记录。调用 replace() 之后，用户不能回到前一页。

```js
<!DOCTYPE html>
<html lang="">
<head>
    <title>You won't be able to get back here</title>
</head>
<body>
<p>Enjoy this page for a second, because you won't be coming back here.</p>
<script>
    setTimeout(() => location.replace("http://www.wrox.com/"), 1000);
</script>
</body>
</html>
```

最后一个修改地址的方法是 reload() ，它能重新加载当前显示的页面。

### 12.3 navigator对象 ###

客户端标识浏览器的标准。

| 属性/方法           | 说明                                                       |
| ------------------- | ---------------------------------------------------------- |
| activeVrDisplays    | 返回数组，包含 ispresenting 属性为 true 的 VRDisplay 实例  |
| appCodeName         | 即使在非 Mozilla浏览器中也会返回 "Mozilla"                 |
| appVersion          | 浏览器版本。通常与实际的浏览器版本不一致                   |
| battery             | 返回暴露 Battery Status API 的 BatteryManager 对象         |
| buildId             | 浏览器的构建编号                                           |
| connection          | 返回暴露 Network Information API的 NetworkInformation 对象 |
| cookieEnabled       | 返回布尔值，表示是否启用了 cookie                          |
| credentials         |                                                            |
| deviceMemory        | 返回单位为 GB的设备内存容量                                |
| doNotTrack          | 返回用户的“不跟踪”（do-not-track）设置                     |
| geolocation         | 返回暴露 Geolocation API的 Geolocation 对象                |
| hardwareConcurrency | 返回设备的处理器核心数量                                   |
| javaEnabled         | 返回布尔值，表示浏览器是否启用了 Java                      |
| language            | 返回浏览器的主语言                                         |
| platform            | 返回浏览器运行的系统平台                                   |

navigator 对象的属性通常用于确定浏览器的类型。

#### 12.3.1 检测插件 ####

`window.navigator.plugins`

#### 12.3.2 注册处理程序 ####

现代浏览器支持 navigator 上的（在 HTML5 中定义的） registerProtocolHandler() 方法。

### 12.4 screen对象 ###

这个对象中保存的纯粹是客户端能力信息，也就是浏览器窗口外面的客户端显示器的信息，

### 12.5 history对象 ###

history 对象表示当前窗口首次使用以来用户的导航历史记录。因为 history 是 window 的属性，所以每个 window 都有自己的 history 对象。出于安全考虑，这个对象不会暴露用户访问过的 URL，但可以通过它在不知道实际 URL 的情况下前进和后退。

#### 12.5.1 导航 ####

go() 方法可以在用户历史记录中沿任何方向导航，可以前进也可以后退。

go() 有两个简写方法： `back()` 和 `forward()` 。

#### 12.5.2 历史状态管理 ####

用户每次点击都会触发页面刷新的时代早已过去，“后退”和“前进”按钮对用户来说就代表“帮我切换一个状态”的历史也就随之结束了。

为解决这个问题，首先出现的是 hashchange 事件 / HTML5 也为history 对象增加了方便的状态管理特性。

hashchange 会在页面 URL 的散列变化时被触发，开发者可以在此时执行某些操作。

而状态管理API 则可以让开发者改变浏览器 URL 而不会加载新页面。

## 14 DOM ##

### 14.1 节点层级 ###

其中， document 节点表示每个文档的根节点。在这里，根节点的唯一子节点是 <html> 元素，我们称之为文档元素（ documentElement ）。

#### 14.1.1 Node 类型 ####

每个节点都有 nodeType 属性，表示该节点的类型。节点类型由定义在 Node 类型上的 12 个数值常量表示：

- Node.ELEMENT_NODE (1)
- Node.ATTRIBUTE_NODE (2)
- Node.TEXT_NODE (3)
- Node.CDATA_SECTION_NODE (4)
- Node.ENTITY_REFERENCE_NODE (5)
- Node.ENTITY_NODE (6)
- Node.PROCESSING_INSTRUCTION_NODE (7)
- Node.COMMENT_NODE (8)
- Node.DOCUMENT_NODE (9)
- Node.DOCUMENT_TYPE_NODE (10)
- Node.DOCUMENT_FRAGMENT_NODE (11)
- Node.NOTATION_NODE (12)

**1. nodeName 与 nodeValue**

对元素而言， nodeName 始终等于元素的标签名，而 nodeValue 则始终为 null 。

**2. 节点关系**

每个节点都有一个 childNodes 属性，其中包含一个 NodeList 的实例。 NodeList 是一个类数组对象，用于存储可以按位置存取的有序节点。注意， NodeList 并不是 Array 的实例，但可以使用中括号访问它的值，而且它也有 length 属性。

NodeList 对象独特的地方在于，它其实是一个对 DOM结构的查询，因此 DOM 结构的变化会自动地在 NodeList中反映出来。

每个节点都有一个 parentNode 属性，指向其 DOM 树中的父元素。

父节点和它的第一个及最后一个子节点也有专门属性： firstChild 和 lastChild 分别指向childNodes 中的第一个和最后一个子节点。

![image-20210719194851917](.assets/image-20210719194851917.png)

ownerDocument 属性是一个指向代表整个文档的文档节点的指针。

**3. 操纵节点**

- `appendChild()` 用于在 childNodes 列表末尾添加节点。添加新节点会更新相关的关系指针，包括父节点和之前的最后一个子节点。如果把文档中已经存在的节点传给 appendChild() ，则这个节点会从之前的位置被转移到新位置。

- `insertBefore()` 这个方法接收两个参数：要插入的节点和参照节点。调用这个方法后，要插入的节点会变成参照节点的前一个同胞节点，并被返回。

- `replaceChild()` 方法接收两个参数：要插入的节点和要替换的节点。要替换的节点会被返回并从文档树中完全移除，要插入的节点会取而代之。
- `removeChild()` 这个方法接收一个参数，即要移除的节点。被移除的节点会被返回.

**4. 其他方法**

- `cloneNode()` 返回与调用它的节点一模一样的节点, 接收一个布尔值参数，表示是否深复制。

- `normalize()` 这个方法唯一的任务就是处理文档子树中的文本节点。

#### 14.1.2 Document 类型 ####

Document 类型是 JavaScript 中表示文档节点的类型。在浏览器中，文档对象 document 是HTMLDocument 的实例（ HTMLDocument 继承 Document ），表示整个 HTML页面。 document 是 window对象的属性，因此是一个全局对象。

 Document 类型的节点有以下特征：

- nodeType 9
- nodeName "#document"
- nodeValue null
- parentNode null
- ownerDocument null
- 子节点可以是 DocumentType （最多一个）、 Element （最多一个）、 ProcessingInstruction或 Comment 类型。

**1. 文档子节点**

两个访问子节点的快捷方式。

第一个是 documentElement 属性，始终指向 HTML 页面中的 <html> 元素。

document 对象还有一个 body 属性，直接指向 <body> 元素。

还可以通过doctype属性访问  `<!doctype>` 标签

**2. 文档信息**

- title属性： 通过这个属性可以读写页面的标题，修改后的标题也会反映在浏览器标题栏上。不过，修改 title 属性并不会改变 <title> 元素。
- URL: 包含当前页面的完整 URL
- domain: 页面的域名
- referrer: 包含链接到当前页面的那个页面的 URL

当页面中包含来自某个不同子域的窗格（ <frame> ）或内嵌窗格（ <iframe> ）时，设置document.domain 是有用的。

浏览器对 domain 属性还有一个限制，即这个属性一旦放松就不能再收紧。比如，把document.domain 设置为 "wrox.com" 之后，就不能再将其设置回 "p2p.wrox.com"

**3. 定位元素**

- `getElementById()` 如果页面中存在多个具有相同 ID的元素，则 getElementById() 返回在文档中出现的第一个元素。
- `getElementsByTagName()` 接收一个参数，即要获取元素的标签名，返回包含零个或多个元素的 NodeList, 这个方法返回一个HTMLCollection 对象。HTMLCollection 对象还有一个额外的方法 namedItem() ，可通过标签的 name 属性取得某一项的引用。对 HTMLCollection 对象而言，中括号既可以接收数值索引，也可以接收字符串索引。而在后台，数值索引会调用 item() ，字符串索引会调用 namedItem() 。
- ` getElementsByName()` 返回具有给定 name 属性的所有元素。 getElementsByName() 方法最常用于单选按钮，因为同一字段的单选按钮必须具有相同的 name 属性才能确保把正确的值发送给服务器。

**4. 特殊集合**

几个特殊集合，这些集合也都是 HTMLCollection 的实例

- document.anchors  包含文档中所有带 name 属性的 <a> 元素。
- document.applets
- document.forms
- document.images
- document.links

**5. DOM兼容性检测**

document.implementation

**6. 文档写入**

document 对象有一个古老的能力，即向网页输出流中写入内容。

`write()` `writeln()` `open()` `close()`

#### 14.1.3 Element 类型 ####

 Element 类型的节点具有以下特征：

- nodeType 1
- nodeName 元素标签名
- nodeValue null
- parentNode 值为 Document 或 Element 对象
- 子节点可以是 Element 、 Text 、 Comment 、 ProcessingInstruction 、 CDATASection 、EntityReference 类型。

可以通过 nodeName 或 tagName 属性来获取元素的标签名。

**1. HTML元素**

所有 HTML 元素都通过 HTMLElement 类型表示，包括其直接实例和间接实例。

它们是所有 HTML 元素上都有的标准属性：

- id 元素在文档中的唯一标识符；
- title 包含元素的额外信息，通常以提示条形式展示；
- lang 元素内容的语言代码
- dir 语言的书写方向
- className 相当于 class 属性，用于指定元素的 CSS 类

**2. 取得属性**

每个元素都有零个或多个属性，通常用于为元素或其内容附加更多信息

与属性相关的 DOM 方法主要有 3 个： getAttribute() 、 setAttribute() 和 removeAttribute() 。

属性名不区分大小写，因此 "ID" 和 "id" 被认为是同一个属性。另外，根据 HTML5 规范的要求，自定义属性名应该前缀 `data-` 以方便验证。

元素的所有属性也可以通过相应 DOM 元素对象的属性来取得。还有所有公认（非自定义）的属性也会被添加为 DOM 对象的属性。

在使用 getAttribute() 访问 style 属性时，返回的是 CSS字符串。而在通过 DOM对象的属性访问时， style 属性返回的是一个（ CSSStyleDeclaration ）对象。

getAttribute() 主要用于取得自定义属性的值。

**3. 设置属性**

- `setAttribute()`
- 直接给 DOM 对象的属性赋值也可以设置元素属性的值

**4. attributes 属性**

Element 类型是唯一使用 attributes 属性的 DOM 节点类型。 attributes 属性包含一个NamedNodeMap 实例

元素的每个属性都表示为一个 `Attr` 节点，并保存在这个 NamedNodeMap 对象中。

- getNamedItem(name) ，返回 nodeName 属性等于 name 的节点
- removeNamedItem(name) ，删除 nodeName 属性等于 name 的节点
- setNamedItem(node) ，向列表中添加 node 节点，以其 nodeName 为索引
- item(pos) ，返回索引位置 pos 处的节点

attributes 属性中的每个节点的 nodeName 是对应属性的名字， nodeValue 是属性的值。

**5. 创建元素**

```js
let div = document.createElement("div");
```

**6. 元素后代**

 childNodes属性包含元素所有的子节点，这些子节点可能是其他元素、文本节点、注释或处理指令。

#### 14.1.4 Text 类型 ####

Text 节点由 Text 类型表示，包含按字面解释的纯文本，也可能包含转义后的 HTML 字符，但不含 HTML 代码。

 Text 类型的节点具有以下特征：

- nodeType 3
- nodeName #text
- nodeValue 为节点中包含的文本
- parentNode  值为 Element 对象；
- 不支持子节点。

Text 节点中包含的文本可以通过 nodeValue 属性访问，也可以通过 data 属性访问，这两个属性包含相同的值。

文本节点暴露了以下操作文本的方法：

- appendData(text)
- deleteData(offset, count)
- insertData(offset, text)
- replaceData(offset, count, text)
- splitText(offset)
- substringData(offset, count)

**1. 创建文本节点**

```js
let element = document.createElement("div");
element.className = "message";

let textNode = document.createTextNode("Hello world!");
element.appendChild(textNode);
let anotherTextNode = document.createTextNode("Yippee!");
element.appendChild(anotherTextNode);
document.body.appendChild(element);
```

在将一个文本节点作为另一个文本节点的同胞插入后，两个文本节点的文本之间不会包含空格。

**2. 规范化文本节点**

`normalize()`

浏览器在解析文档时，永远不会创建同胞文本节点。同胞文本节点只会出现在 DOM脚本生成的文档树中。

**3. 拆分文本节点**

` splitText()` 这个方法可以在指定的偏移位置拆分 nodeValue ，将一个文本节点拆分成两个文本节点。

#### 14.1.5 Comment 类型 ####

 Comment 类型的节点具有以下特征：

- nodeType 8
- nodeName #comment
- nodeValue 注释的内容
- parentNode 值为 Document 或 Element 对象
- 不支持子节点

Comment 类型与 Text 类型继承同一个基类（ CharacterData ）

#### 14.1.7 DocumentType 类型 ####

DocumentType 类型的节点包含文档的文档类型（ doctype ）信息，具有以下特征：

- nodeType 10
- nodeName 值为文档类型的名称
- nodeValue null
- parentNode 值为 Document 对象
- 不支持子节点

#### 14.1.8 DocumentFragment 类型 ####

DocumentFragment 节点具有以下特征：

- nodeType 11
- nodeName #document-fragment
- nodeValue 值为 null
- parentNode 值为 null
- 子节点可以是 Element 、 ProcessingInstruction 、 Comment 、 Text 、 CDATASection 或EntityReference

#### 14.1.9 Attr 类型 ####

元素数据在 DOM中通过 Attr 类型表示。 Attr 类型构造函数和原型在所有浏览器中都可以直接访问。

- nodeType 2
- nodeName 属性名
- nodeValue 属性值
- parentNode 值为null
- 在 HTML 中不支持子节点
- 在 XML 中子节点可以是 Text 或 EntityReference

可以使用 document.createAttribute() 方法创建新的 Attr 节点，参数为属性名。

### 14.2 DOM编程 ###

#### 14.2.1 动态脚本 ####

动态脚本就是在页面初始加载时不存在，之后又通过 DOM 包含的脚本。

有两种方式通过 <script> 动态为网页添加脚本：引入外部文件和直接插入源代码。

```js
<script src="foo.js"></script>

function loadScript(url) {
    let script = document.createElement("script");
    script.src = url;
    document.body.appendChild(script);
}
```

#### 14.2.2 动态样式 ####

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

这个元素很容易使用 DOM 编程创建出来：

```js
let link = document.createElement("link");
link.rel = "stylesheet";
link.type = "text/css";
link.href = "styles.css";
let head = document.getElementsByTagName("head")[0];
head.appendChild(link);
```

#### 14.2.4 使用NodeList ####

理解 NodeList 对象和相关的 NamedNodeMap 、 HTMLCollection ，是理解 DOM 编程的关键。

### 14.3 MutationObserver 接口 ###

添加到 DOM 规范中的 MutationObserver 接口，可以在 DOM 被修改时异步执行回调。

#### 14.3.1 基本用法 ####

MutationObserver 的实例要通过调用 MutationObserver 构造函数并传入一个回调函数来创建：

```js
let observer = new MutationObserver(() => console.log('DOM was mutated.'));
```

**1. observe()**

要把这个 observer 与 DOM 关联起来，需要使用 observe() 方法。这个方法接收两个必需的参数：要观察其变化的 DOM 节点，以及一个 MutationObserverInit 对象。

MutationObserverInit 对象用于控制观察哪些方面的变化，是一个键/值对形式配置选项的字典。

```js
observer.observe(document.body, {'attributes': true});

let observer = new MutationObserver(() => console.log('DOM was mutated.'));
observer.observe(document.body, {'attributes': true});
document.body.className = 'foo';
console.log('changed body class');
```

**2. 回调与MutationRecord**

每个回调都会收到一个 MutationRecord 实例的数组。

因为回调执行之前可能同时发生多个满足观察条件的事件，所以每次执行回调都会传入一个包含按顺序入队的 MutationRecord 实例的数组。

```js
// [
// {
// addedNodes: NodeList [],
// attributeName: "foo",
// attributeNamespace: null,
// nextSibling: null,
// oldValue: null,
// previousSibling: null
// removedNodes: NodeList [],
// target: body
// type: "attributes"
// }
// ]
```

下表列出了 MutationRecord 实例的属性。

| 属性     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| target   | 被修改影响的目标节点                                         |
| type     | 字符串，表示变化的类型： "attributes" 、 "characterData" 或 "childList" |
| oldValue |                                                              |

传给回调函数的第二个参数是观察变化的 MutationObserver 的实例，演示如下：

```js
let observer = new MutationObserver((mutationRecords, mutationObserver) => console.log(mutationRecords, mutationObserver));
observer.observe(document.body, {attributes: true});
document.body.className = 'foo';
```

**3. disconnect()**

要提前终止执行回调，可以调用 disconnect() 方法。

**4. 复用MutationObserver**

多次调用 observe() 方法，可以复用一个 MutationObserver 对象观察多个不同的目标节点。此时， MutationRecord 的 target 属性可以标识发生变化事件的目标节点。

```js
let observer = new MutationObserver((mutationRecords) => console.log(mutationRecords.map((x) => x.target)));
// 向页面主体添加两个子节点
let childA = document.createElement('div'),
    childB = document.createElement('span');
document.body.appendChild(childA);
document.body.appendChild(childB);
// 观察两个子节点
observer.observe(childA, {attributes: true});
observer.observe(childB, {attributes: true});
// 修改两个子节点的属性
childA.setAttribute('foo', 'bar');
childB.setAttribute('foo', 'bar');
```

**5. 重用MutationObserver**

调用 disconnect() 并不会结束 MutationObserver 的生命。还可以重新使用这个观察者，再将它关联到新的目标节点。

#### 14.3.2 MutationObserverInit与观察范围 ####

MutationObserverInit 对象用于控制对目标节点的观察范围。粗略地讲，观察者可以观察的事件包括属性变化、文本变化和子节点变化。

| 属性                  | 说明                                                     |
| --------------------- | -------------------------------------------------------- |
| subtree               | 布尔值，表示除了目标节点，是否观察目标节点的子树（后代） |
| attributes            | 布尔值，表示是否观察目标节点的属性变化，默认false        |
| attributeFilter       | 字符串数组，表示要观察哪些属性的变化，默认为观察所有属性 |
| attributeOldValue     | 布尔值，表示 MutationRecord 是否记录变化之前的属性值     |
| characterData         | 布尔值，表示修改字符数据是否触发变化事件                 |
| characterDataOldValue | 布尔值，表示 MutationRecord 是否记录变化之前的字符数据   |
| childList             | 布尔值，表示修改目标节点的子节点是否触发变化事件         |

在调用 observe() 时， MutationObserverInit 对象中的 attribute 、 characterData 和 childList 属性必须至少有一项为 true。

## 15 DOM扩展 ##

诞生了描述 DOM扩展的两个标准：Selectors API与 HTML5。

### 15.1 Selectors API ###

Selectors API Level 1 的核心是两个方法： querySelector() 和 querySelectorAll() 。 Document 类型和 Element 类型的实例上都会暴露这两个方法

Selectors API Level 2 规范在 Element 类型上新增了更多方法，比如 matches() 、 find() 和 findAll() 。

#### 15.1.1 querySelector() ####

querySelector() 方法接收 CSS 选择符参数，返回匹配该模式的第一个后代元素，如果没有匹配项则返回 null 。

#### 15.1.2 querySelectorAll() ####

querySelectorAll() 方法跟 querySelector() 一样，也接收一个用于查询的参数，但它会返回所有匹配的节点，而不止一个。这个方法返回的是一个 NodeList 的静态实例。

### 15.2 元素遍历 ###

Element Traversal API 为 DOM 元素添加了 5 个属性：

- childElementCount, 返回子元素数量（不包含文本节点和注释）；
- firstElementChild ，指向第一个 Element 类型的子元素（ Element 版 firstChild ）；
- lastElementChild ，指向最后一个 Element 类型的子元素（ Element 版 lastChild ）；
- previousElementSibling ， 指 向 前 一 个 Element 类 型 的 同 胞 元 素 （ Element 版previousSibling ）；
- nextElementSibling ，指向后一个 Element 类型的同胞元素（ Element 版 nextSibling ）。

### 15.3 HTML5 ###

HTML5 规范却包含了与标记相关的大量 JavaScript API 定义。其中有的 API 与 DOM 重合，定义了浏览器应该提供的 DOM扩展。

#### 15.3.1 CSS类扩展 ####

**1. getElementsByClassName()**

暴露在 document 对象和所有 HTML 元素上。

getElementsByClassName() 方法接收一个参数，即包含一个或多个类名的字符串，返回类名中包含相应类的元素的 NodeList 。这个方法只会返回以调用它的对象为根元素的子树中所有匹配的元素。

**2. classList属性**

要操作类名，可以通过 className 属性实现添加、删除和替换。但 className 是一个字符串，所以每次操作之后都需要重新设置这个值才能生效，即使只改动了部分字符串也一样。

classList 是一个新的集合类型 DOMTokenList 的实例。

- length 表示自己包含多少项
- item() 可以通过 item() 或中括号取得个别的元素
- add(value) ，向类名列表中添加指定的字符串值 value
- contains(value) 返回布尔值，表示给定的 value 是否存在
- remove(value) 从类名列表中删除指定的字符串值 value 
- toggle(value) 如果类名列表中已经存在指定的 value ，则删除；如果不存在，则添加。

#### 15.3.2 焦点管理 ####

首先是 document.activeElement ，始终包含当前拥有焦点的 DOM元素。页面加载时，可以通过用户输入（按 Tab 键或代码中使用 focus() 方法）让某个元素自动获得焦点。

其次是 document.hasFocus() 方法，该方法返回布尔值，表示文档是否拥有焦点

#### 15.3.3 HTMLDocument 扩展 ####

**1. readyState**

readyState 是 IE4 最早添加到 document 对象上的属性，后来其他浏览器也都依葫芦画瓢地支持这个属性。

 document.readyState 属性有两个可能的值：

- loading 表示文档正在加载
- complete 表示文档加载完成

在这个属性得到广泛支持以前，通常要依赖 onload 事件处理程序设置一个标记，表示文档加载完了。

**2. compatMode**

**3. head属性**

`let head = document.head;`

#### 15.3.4 字符集属性 ####

```js
console.log(document.characterSet); // "UTF-16"
document.characterSet = "UTF-8";
```

#### 15.3.5 自定义数据属性 ####

#### 15.3.6 插入标记 ####

**1. innerHTML属性**

在读取 innerHTML 属性时，会返回元素所有后代的 HTML 字符串，包括元素、注释和文本节点。而在写入 innerHTML 时，则会根据提供的字符串值以新的 DOM 子树替代元素中原来包含的所有节点。

**3. outerHTML属性**

读取 outerHTML 属性时，会返回调用它的元素（及所有后代元素）的 HTML 字符串。

```js
div.outerHTML = "<p>This is a paragraph.</p>";
// 则会得到与执行以下脚本相同的结果：
let p = document.createElement("p");
p.appendChild(document.createTextNode("This is a paragraph."));
div.parentNode.replaceChild(p, div);
```

**4. insertAdjacentHTML() 与 insertAdjacentText()**

