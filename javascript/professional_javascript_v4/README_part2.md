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

它们都接收两个参数：要插入标记的位置和要插入的 HTML 或文本。

第一个参数必须是下列值中的一个：

- "beforebegin" ，插入当前元素前面，作为前一个同胞节点
- "afterbegin" ，插入当前元素内部，作为新的子节点或放在第一个子节点前面
- "beforeend" ，插入当前元素内部，作为新的子节点或放在最后一个子节点后面
- "afterend" ，插入当前元素后面，作为下一个同胞节点

#### 15.3.7 scrollIntoView() ####

scrollIntoView() 方法存在于所有 HTML 元素上，可以滚动浏览器窗口或容器元素以便包含元素进入视口。

- alignToTop
  - true: 窗口滚动后元素的顶部与视口顶部对齐
  - false: 窗口滚动后元素的底部与视口底部对齐
- scrollIntoViewOptions
  - behavior 定义过渡动画，可取的值为 "smooth" 和 "auto" ，默认为 "auto"
  - block 定义垂直方向的对齐，可取的值为 "start" 、 "center" 、 "end" 和 "nearest" ，默认为 "start" 。
  - inline ：定义水平方向的对齐，可取的值为 "start" 、 "center" 、 "end" 和 "nearest" ，默认为 "nearest" 。

### 15.4 专有扩展 ###

#### 15.4.1 children 属性 ####

children 属性是一个 HTMLCollection ，只包含元素的 Element 类型的子节点。

#### 15.4.2 contains() 方法 ####

contains() 方法应该在要搜索的祖先元素上调用，参数是待确定的目标节点。

如果目标节点是被搜索节点的后代， contains() 返回 true ，否则返回 false 。

#### 15.4.3 插入标记 ####

**1. innerHTML**

innerText 属性对应元素中包含的所有文本内容，无论文本在子树中哪个层级。在用于读取值时，innerText 会按照深度优先的顺序将子树中所有文本节点的值拼接起来。

在用于写入值时， innerText会移除元素的所有后代并插入一个包含该值的文本节点。

**2. outerHTML**

outerText 与 innerText 是类似的，只不过作用范围包含调用它的节点。

要读取文本值时，outerText 与 innerText 实际上会返回同样的内容。

但在写入文本值时， outerText 就大不相同了。写入文本值时， outerText 不止会移除所有后代节点，而是会替换整个元素。

## 16 DOM2 & DOM3 ##

- DOM Core：在 DOM1 核心部分的基础上，为节点增加方法和属性。
- DOM Views：定义基于样式信息的不同视图。
- DOM Events：定义通过事件实现 DOM 文档交互。
- DOM Style：定义以编程方式访问和修改 CSS 样式的接口。
- DOM Traversal and Range：新增遍历 DOM文档及选择文档内容的接口。
- DOM HTML：在 DOM1 HTML 部分的基础上，增加属性、方法和新接口。
- DOM Mutation Observers：定义基于 DOM变化触发回调的接口。这个模块是 DOM4 级模块，用于取代 Mutation Events。

### 16.2 样式 ###

HTML 中的样式有 3 种定义方式：外部样式表（通过 <link> 元素）、文档样式表（使用 <style> 元素）和元素特定样式（使用 style 属性）。DOM2 Style为这 3 种应用样式的机制都提供了 API。

#### 16.2.1 存取元素样式 ####

style 属性是 CSSStyleDeclaration 类型的实例，其中包含通过 HTML style 属性为元素设置的所有样式信息，但不包含通过层叠机制从文档样式和外部样式中继承来的样式。

js style属性和原生的style属性之间 驼峰大小写形式。

**1. DOM样式属性和方法**

- cssText 包含 style 属性中的 CSS 代码
- length ，应用给元素的 CSS 属性数量
- parentRule ，表示 CSS 信息的 CSSRule 对象
- getPropertyPriority(propertyName)
- getPropertyValue(propertyName) ，返回属性 propertyName 的字符串值
- item(index) 返回索引为 index 的 CSS 属性名
- removeProperty(propertyName) ，从样式中删除 CSS 属性 propertyName
- setProperty(propertyName, value, priority) ，设置 CSS 属性 propertyName 的值为value ， priority 是 "important" 或空字符串。

设置 cssText 是一次性修改元素多个样式最快捷的方式，因为所有变化会同时生效。

**2. 计算样式**

DOM2 Style在 document.defaultView 上增加了 getComputedStyle()方法。这个方法接收两个参数：要取得计算样式的元素和伪元素字符串（如 ":after" ）。

getComputedStyle() 方法返回一个 CSSStyleDeclaration对象（与 style 属性的类型一样），包含元素的计算样式。

```js
let myDiv = document.getElementById("myDiv");
let computedStyle = document.defaultView.getComputedStyle(myDiv, null);

console.log(computedStyle.backgroundColor); // "red"
console.log(computedStyle.width); // "100px"
console.log(computedStyle.height); // "200px"
console.log(computedStyle.border); // "1px solid black"（在某些浏览器中）
```

在所有浏览器中计算样式都是只读的.

#### 16.2.2 操作样式表 ####

- link : HTMLLinkElement
- style: HTMLStyleElement

CSSStyleSheet 类型表示 CSS 样式表，包括使用 <link> 元素和通过 <style> 元素定义的样式表. CSSStyleSheet 类型继承 StyleSheet。

- disabled 表示样式表是否被禁用
- href: 如果是使用 <link> 包含的样式表，则返回样式表的 URL，否则返回 null
- media: 样式表支持的媒体类型集合，这个集合有一个 length 属性和一个 item() 方法
- ownerNode: 指向拥有当前样式表的节点，在 HTML 中要么是 <link> 元素要么是 <style> 元素
- parentStyleSheet ，如果当前样式表是通过 @import 被包含在另一个样式表中，则这个属性指向导入它的样式表。
- title: ownerNode 的 title 属性。
- type: 字符串，表示样式表的类型。
- cssRules ，当前样式表包含的样式规则的集合
- ownerRule ，如果样式表是使用 @import 导入的，则指向导入规则, 否则为null
- deleteRule(index) ，在指定位置删除 cssRules 中的规则。
- insertRule(rule, index) ，在指定位置向 cssRules 中插入规则。

document.styleSheets 表示文档中可用的样式表集合。这个集合的 length 属性保存着文档中样式表的数量，而每个样式表都可以使用中括号或 item() 方法获取。

**1. CSS规则**

CSSRule 类型表示样式表中的一条规则。这个类型也是一个通用基类，很多类型都继承它，但其中最常用的是表示样式信息的 CSSStyleRule

- cssText: 返回整条规则的文本
- parentRule: 如果这条规则被其他规则（如 @media ）包含，则指向包含规则，否则就是 null 。
- parentStyleSheet ，包含当前规则的样式表
- selectorText ，返回规则的选择符文本
- style ，返回 CSSStyleDeclaration 对象，可以设置和获取当前规则中的样式
- type ，数值常量，表示规则类型

#### 16.2.3 元素尺寸 ####

**1. 偏移尺寸**

第一组属性涉及偏移尺寸（offset dimensions），包含元素在屏幕上占用的所有视觉空间。

元素在页面上的视觉空间由其高度和宽度决定，包括所有内边距、滚动条和边框（但不包含外边距）。

- offsetHeight 元素在垂直方向上占用的像素尺寸，包括它的高度、水平滚动条高度（如果可见）和上、下边框的高度。
- offsetLeft ，元素左边框外侧距离包含元素左边框内侧的像素数
- offsetTop ，元素上边框外侧距离包含元素上边框内侧的像素数
- offsetWidth ，元素在水平方向上占用的像素尺寸，包括它的宽度、垂直滚动条宽度（如果可见）和左、右边框的宽度。

![image-20210720224358302](.assets/image-20210720224358302.png)

要确定一个元素在页面中的偏移量，可以把它的 offsetLeft 和 offsetTop 属性分别与 offsetParent的相同属性相加，一直加到根元素。

```js
function getElementLeft(element) {
    let actualLeft = element.offsetLeft;
    let current = element.offsetParent;
    while (current !== null) {
        actualLeft += current.offsetLeft;
        current = current.offsetParent;
    }
    return actualLeft;
}
```

**2. 客户端尺寸**

元素的客户端尺寸（client dimensions）包含元素内容及其内边距所占用的空间

- clientWidth
- clientHeight

clientWidth 是内容区宽度加左、右内边距宽度， clientHeight 是内容区高度加上、下内边距高度

![image-20210720224823101](.assets/image-20210720224823101.png)

这两个属性最常用于确定浏览器视口尺寸，即检测 document.documentElement 的 clientWidth 和 clientHeight 。

**3. 滚动尺寸**

滚动尺寸相关的属性有如下 4 个：

- scrollHeight ，没有滚动条出现时，元素内容的总高度。
- scrollLeft ，内容区左侧隐藏的像素数，设置这个属性可以改变元素的滚动位置。
- scrollTop ，内容区顶部隐藏的像素数，设置这个属性可以改变元素的滚动位置。
- scrollWidth ，没有滚动条出现时，元素内容的总宽度。

![image-20210720225019664](.assets/image-20210720225019664.png)

scrollWidth 和 scrollHeight 可以用来确定给定元素内容的实际尺寸。

document.documentElement.scrollHeight 就是整个页面垂直方向的总高度。

**4. 确定元素尺寸**

浏览器在每个元素上都暴露了 getBoundingClientRect() 方法，返回一个 DOMRect 对象，包含6 个属性：

left 、 top 、 right 、 bottom 、 height 和 width 

![image-20210720225113366](.assets/image-20210720225113366.png)

### 16.3 遍历 ###

DOM2 Traversal and Range 模块定义了两个类型用于辅助顺序遍历 DOM 结构。

- NodeIterator
- TreeWalker

#### 16.3.1 NodeIterator ####

通过 document.createNodeIterator() 方法创建其实例。有如下四个参数：

- root 作为遍历根节点的节点
- whatToShow 数值代码，表示应该访问哪些节点
- filter ， NodeFilter 对象或函数，表示是否接收或跳过特定节点
- entityReferenceExpansion ，布尔值，表示是否扩展实体引用

whatToShow 参数是一个位掩码，通过应用一个或多个过滤器来指定访问哪些节点。

```js
let whatToShow = NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT;
// let filter = {
//     acceptNode(node) {
//         return node.tagName.toLowerCase() == 'p' ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
//     }
// }

let filter = function (node) {
    return node.tagName.toLowerCase() == "p" ?
        NodeFilter.FILTER_ACCEPT :
        NodeFilter.FILTER_SKIP;
};

let iterator = document.createNodeIterator(
    document.body, NodeFilter.SHOW_ELEMENT, filter
)
```

NodeIterator 的两个主要方法是 nextNode() 和 previousNode()

```html
<div id="div1">
    <p><b>Hello</b> world!</p>
    <ul>
        <li>List item 1</li>
        <li>List item 2</li>
        <li>List item 3</li>
    </ul>
</div>

<script>

    let div1 = document.getElementById('div1');
    let iter = document.createNodeIterator(div1, NodeFilter.SHOW_ELEMENT, null, false);
    let node = iter.nextNode()
    while (node != null) {
        console.log(node.tagName);
        node = iter.nextNode();
    }

</script>
```

#### 16.3.2 TreeWalker ####

TreeWalker 是 NodeIterator 的高级版。除了包含同样的 nextNode() 、 previousNode() 方法，TreeWalker 还添加了如下在 DOM 结构中向不同方向遍历的方法。

- parentNode() 遍历到当前节点的父节点。
- firstChild() ，遍历到当前节点的第一个子节点。
- lastChild() ，遍历到当前节点的最后一个子节点。
- nextSibling() ，遍历到当前节点的下一个同胞节点。
- previousSibling() ，遍历到当前节点的上一个同胞节点。

### 16.4 范围 ###

DOM2 在 Document 类型上定义了一个 createRange() 方法。

`let range = document.createRange();`

## 17 事件 ##

JavaScript 与 HTML 的交互是通过事件实现的，事件代表文档或浏览器窗口中某个有意义的时刻。可以使用仅在事件发生时执行的监听器（也叫处理程序）订阅事件。在传统软件工程领域，这个模型叫“观察者模式”，其能够做到页面行为（在 JavaScript 中定义）与页面展示（在 HTML 和 CSS 中定义）的分离。

### 17.1 事件流 ###

事件流描述了页面接收事件的顺序。

#### 17.1.1 事件冒泡 ####

IE 事件流被称为事件冒泡，这是因为事件被定义为从最具体的元素（文档树中最深的节点）开始触发，然后向上传播至没有那么具体的元素（文档）。

#### 17.1.2 事件捕获 ####

Netscape Communicator 团队提出了另一种名为事件捕获的事件流。事件捕获的意思是最不具体的节点应该最先收到事件，而最具体的节点应该最后收到事件。事件捕获实际上是为了在事件到达最终目标前拦截事件。

实际上，所有浏览器都是从 window 对象开始捕获事件，而 DOM2 Events规范规定的是从 document 开始。

#### 17.1.3 DOM事件流 ####

DOM2 Events 规范规定事件流分为 3 个阶段：事件捕获、到达目标和事件冒泡。事件捕获最先发生，为提前拦截事件提供了可能。然后，实际的目标元素接收到事件。最后一个阶段是冒泡，最迟要在这个阶段响应事件。

在 DOM 事件流中，实际的目标（ <div> 元素）在捕获阶段不会接收到事件。

### 17.2 事件处理程序 ###

为响应事件而调用的函数被称为事件处理程序（或事件监听器）。

#### 17.2.1 HTML事件处理程序 ####

特定元素支持的每个事件都可以使用事件处理程序的名字以 HTML 属性的形式来指定。

```html
<div id="myDiv" onclick="console.log('HHH');">Click Me</div>
```

以这种方式指定的事件处理程序有一些特殊的地方。首先，会创建一个函数来封装属性的值。这个函数有一个特殊的局部变量 event ，其中保存的就是 event 对象。

在这个函数中， this 值相当于事件的目标元素。

这个动态创建的包装函数还有一个特别有意思的地方，就是其作用域链被扩展了。在这个函数中，document 和元素自身的成员都可以被当成局部变量来访问。这是通过使用 with 实现的

#### 17.2.2 DOM0事件处理程序 ####

每个元素（包括 window 和 document ）都有通常小写的事件处理程序属性，比如 onclick 。只要把这个属性赋值为一个函数即可：

```js
let h2 = document.getElementById('h21');
h2.onclick = function (ev) {
    console.log(ev);
    console.log('clicked the h2');
}
```

像这样使用 DOM0 方式为事件处理程序赋值时，所赋函数被视为元素的方法。因此，事件处理程序会在元素的作用域中运行，即 this 等于元素。

以这种方式添加事件处理程序是注册在事件流的冒泡阶段的。

通过将事件处理程序属性的值设置为 null ，可以移除通过 DOM0 方式添加的事件处理程序。

#### 17.2.2 DOM2事件处理程序 ####

DOM2 Events 为事件处理程序的赋值和移除定义了两个方法： addEventListener() 和 removeEventListener() 

这两个方法暴露在所有 DOM 节点上，它们接收 3 个参数：事件名、事件处理函数和一个布尔值， true 表示在捕获阶段调用事件处理程序， false （默认值）表示在冒泡阶段调用事件处理程序。

```js
h2.addEventListener('click',
    (ev) => {
    console.log(ev);
    console.log(this); // 作用域问题 window
}, false);
```

通过 addEventListener() 添加的事件处理程序只能使用 removeEventListener() 并传入与添加时同样的参数来移除。这意味着使用 addEventListener() 添加的匿名函数无法移除.

### 17.3 事件对象 ###

在 DOM 中发生事件时，所有相关信息都会被收集并存储在一个名为 event 的对象中

#### 17.3.1 DOM事件对象 ####

不同的事件生成的事件对象也会包含不同的属性和方法。不过，所有事件对象都会包含下表列出的这些公共属性和方法。

| 属性/方法        | 类型    | 读/写 | 说明                                                         |
| ---------------- | ------- | ----- | ------------------------------------------------------------ |
| bubbles          | bool    | r     | 表示事件是否冒泡                                             |
| cancelable       | bool    | r     | 表示是否可以取消事件的默认行为                               |
| currentTarget    | element | r     | 当前事件处理程序所在的元素                                   |
| defaultPrevented | bool    | r     | true 表示已经调用 preventDefault() 方法（DOM3Events 中新增） |
| detail           | int     | r     | 事件相关的其他信息                                           |
| eventPhase       | int     | r     | 表示调用事件处理程序的阶段：1代表捕获阶段，2代表到达目标，3代表冒泡阶段 |
| target           | element | r     | 事件目标                                                     |
| type             | string  | r     | 被触发的事件类型                                             |

在事件处理程序内部， this 对象始终等于 currentTarget 的值，而 target 只包含事件的实际目标。如果事件处理程序直接添加在了意图的目标，则 this 、 currentTarget 和 target 的值是一样的。

```js
document.body.onclick = function(event) {
	console.log(event.currentTarget === document.body); // true
	console.log(this === document.body); // true
	console.log(event.target === document.getElementById("myBtn")); // true
};
```

这种情况下点击按钮， this 和 currentTarget 都等于 document.body ，这是因为它是注册事件处理程序的元素。而 target 属性等于按钮本身，这是因为那才是 click 事件真正的目标。

preventDefault() 方法用于阻止特定事件的默认动作。

stopPropagation() 方法用于立即阻止事件流在 DOM 结构中传播，取消后续的事件捕获或冒泡。

### 17.4 事件类型 ###

- 用户界面事件（ UIEvent ）：涉及与 BOM交互的通用浏览器事件。
- 焦点事件（ FocusEvent ）：在元素获得和失去焦点时触发。
- 鼠标事件（ MouseEvent ）：使用鼠标在页面上执行某些操作时触发。
- 滚轮事件（ WheelEvent ）：使用鼠标滚轮（或类似设备）时触发。
- 输入事件（ InputEvent ）：向文档中输入文本时触发。
- 键盘事件（ KeyboardEvent ）：使用键盘在页面上执行某些操作时触发。
- 合成事件（ CompositionEvent ）：在使用某种 IME（Input Method Editor，输入法编辑器）输入字符时触发。

#### 17.4.1 用户界面事件 ####

- load: 在 window 上当页面加载完成后触发，在窗套（ <frameset> ）上当所有窗格（ <frame> ）都加载完成后触发，在 <img> 元素上当图片加载完成后触发，在 <object> 元素上当相应对象加载完成后触发。
- unload: 在 window 上当页面完全卸载后触发，在窗套上当所有窗格都卸载完成后触发，在<object> 元素上当相应对象卸载完成后触发。
- abort: 在 <object> 元素上当相应对象加载完成前被用户提前终止下载时触发。
- error: 在 window 上当 JavaScript 报错时触发，在 <img> 元素上当无法加载指定图片时触发，在 <object> 元素上当无法加载相应对象时触发，在窗套上当一个或多个窗格无法完成加载时触发。
- resize: 在 window 或窗格上当窗口或窗格被缩放时触发
- scroll: 当用户滚动包含滚动条的元素时在元素上触发

**1. load事件**

第二种指定 load 事件处理程序的方式是向 <body> 元素添加 onload 属性。一般来说，任何在 window 上发生事件，都可以通过给 <body> 元素上对应的属性赋值来指定，这是因为 HTML 中没有 window 元素。

#### 17.4.2 焦点事件 ####

- blur ：当元素失去焦点时触发。这个事件不冒泡，所有浏览器都支持。
- DOMFocusIn ：当元素获得焦点时触发。这个事件是 focus 的冒泡版。Opera 是唯一支持这个事件的主流浏览器。DOM3 Events废弃了 DOMFocusIn ，推荐 focusin 。
- DOMFocusOut ：当元素失去焦点时触发。这个事件是 blur 的通用版。Opera 是唯一支持这个事件的主流浏览器。DOM3 Events废弃了 DOMFocusOut ，推荐 focusout 。
- focus ：当元素获得焦点时触发。这个事件不冒泡，所有浏览器都支持。
- focusin ：当元素获得焦点时触发。这个事件是 focus 的冒泡版。
- focusout ：当元素失去焦点时触发。这个事件是 blur 的通用版。

#### 17.4.3 鼠标和滚轮事件 ####

鼠标事件是 Web 开发中最常用的一组事件，这是因为鼠标是用户的主要定位设备。DOM3 Events定义了 9 种鼠标事件。

- click 在用户单击鼠标主键（通常是左键）或按键盘回车键时触发
- dblclick ：在用户双击鼠标主键（通常是左键）时触发
- mousedown ：在用户按下任意鼠标键时触发
- mouseenter ：在用户把鼠标光标从元素外部移到元素内部时触发。这个事件不冒泡，也不会在光标经过后代元素时触发
- mouseleave ：在用户把鼠标光标从元素内部移到元素外部时触发。这个事件不冒泡，也不会在光标经过后代元素时触发
- mousemove ：在鼠标光标在元素上移动时反复触发
- mouseout ：在用户把鼠标光标从一个元素移到另一个元素上时触发
- mouseover ：在用户把鼠标光标从元素外部移到元素内部时触发
- mouseup ：在用户释放鼠标键时触发

```mermaid
graph LR
A[mousedown] -->B[mouseup] --> C[click] -->D[mousedown] --> E[mouseup] --> F[click] --> G[dbclick]
```

**鼠标的坐标**

- 客户端坐标：clientX clientY
- 页面坐标：pageX pageY
- 屏幕坐标：screenX screenY

**修饰键**

DOM 规定了 4 个属性来表示这几个修饰键的状态： shiftKey 、 ctrlKey 、 altKey 和 metaKey 。

#### 17.4.4 键盘与输入事件 ####

- keydown 用户按下键盘上某个键时触发，而且持续按住会重复触发.
- keypress 用户按下键盘上某个键并产生字符时触发，而且持续按住会重复触发
- keyup 用户释放键盘上某个键时触发

输入事件：

- textInput 这个事件是对 keypress 事件的扩展，用于在文本显示给用户之前更方便地截获文本输入。 

**1. 键码**

对于 keydown 和 keyup 事件， event 对象的 keyCode 属性中会保存一个键码，对应键盘上特定的一个键。

- keyCode
- keyChar
- key
- char

**2. textInput事件**

一个区别是 keypress 会在任何可以获得焦点的元素上触发，而 textInput 只在可编辑区域上触发。

另一个区别是 textInput 只在有新字符被插入时才会触发，而 keypress 对任何可能影响文本的键都会触发（包括退格键）。

因为 textInput 事件主要关注字符，所以在 event 对象上提供了一个 data 属性。

#### 17.4.5 合成事件 ####

合成事件是 DOM3 Events 中新增的，用于处理通常使用 IME 输入时的复杂输入序列。

#### 17.4.7 HTML5事件 ####

**1. contextmenu事件**

以专门用于表示何时该显示上下文菜单，从而允许开发者取消默认的上下文菜单并提供自定义菜单。

```html
<div id="myDiv">
    Right click or Ctrl+click me to get a custom context menu.
    Click anywhere else to get the default context menu.
</div>
<ul id="myMenu" style="position:absolute;visibility:hidden;background-color:silver">
    <li><a href="http://www.somewhere.com"> somewhere</a></li>
    <li><a href="http://www.wrox.com">Wrox site</a></li>
    <li><a href="http://www.somewhere-else.com">somewhere-else</a></li>
</ul>
```

```js
window.addEventListener('load', (event) => {
    let div = document.getElementById('myDiv');

    div.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        let menu = document.getElementById('myMenu');
        menu.style.left = e.clientX + 'px';
        menu.style.top = e.clientY + 'px';
        menu.style.visibility = 'visible';
    });

    document.addEventListener('click', (ev) => {
        document.getElementById('myMenu').style.visibility = 'hidden';
    })

})
```

**2. beforeunload事件**

beforeunload 事件会在 window 上触发，用意是给开发者提供阻止页面被卸载的机会。这个事件会在页面即将从浏览器中卸载时触发，如果页面需要继续使用，则可以不被卸载。

**3. DOMContentLoaded事件**

DOMContentLoaded 事件会在 DOM 树构建完成后立即触发，而不用等待图片、JavaScript文件、CSS 文件或其他资源加载完成。

DOMContentLoaded 事件通常用于添加事件处理程序或执行其他DOM操作。这个事件始终在 load事件之前触发。

### 17.5 内存与性能 ###

#### 17.5.1 事件委托 ####

事件委托利用事件冒泡，可以只使用一个事件处理程序来管理一种类型的事件。例如， click 事件冒泡到 document 。

```html
<ul id="myLinks">
    <li id="goSomewhere">Go somewhere</li>
    <li id="doSomething">Do something</li>
    <li id="sayHi">Say hi</li>
</ul>
```

```js
let list = document.getElementById('myLinks');

list.addEventListener('click', (event) => {
    let target = event.target;
    switch (target.id) {
        case 'doSomething': {
            document.title = "I changed the document's title";
            break;
        }
        case "goSomewhere": {
            location.href = "http:// www.wrox.com";
            break;
        }
        case "sayHi": {
            console.log("hi");
            break;
        }
    }
})
```

最适合使用事件委托的事件包括： click 、 mousedown 、 mouseup 、 keydown 和 keypress 。

### 17.6 模拟事件 ###

#### 17.6.1 DOM 事件模拟 ####

任何时候，都可以使用 document.createEvent() 方法创建一个 event 对象。

## 19 表单脚本 ##

### 19.1 表单基础 ###

Web 表单在 HTML 中以 <form> 元素表示，在 JavaScript 中则以 HTMLFormElement 类型表示。

HTMLFormElement 类型继承自 HTMLElement 类型。

- acceptCharset 服务器可以接收的字符集
- action 请求的 URL，等价于 HTML 的 action 属性
- elements: 表单中所有控件的 HTMLCollection
- enctype: 请求的编码类型，等价于 HTML 的 enctype 属性
- length ：表单中控件的数量
- method ：HTTP 请求的方法类型
- name ：表单的名字，等价于 HTML 的 name 属性
- reset() ：把表单字段重置为各自的默认值
- submit() ：提交表单
- target ：用于发送请求和接收响应的窗口的名字，等价于 HTML 的 target 属性

有几种方式可以取得对 <form> 元素的引用:

- 使用id
- 使用document.forms

#### 19.1.1 提交表单 ####

提交按钮可以使用 type 属性为 "submit" 的 <input> 或 <button> 元素来定义，图片按钮可以使用 type 属性为 "image" 的 <input> 元素来定义。

```html
<!-- 通用提交按钮 -->
<input type="submit" value="Submit Form">

<!-- 自定义提交按钮 -->
<button type="submit">Submit Form</button>

<!-- 图片按钮 -->
<input type="image" src="graphic.gif">
```

以这种方式提交表单会在向服务器发送请求之前触发 submit 事件。

这样就提供了一个验证表单数据的机会，可以根据验证结果决定是否真的要提交。阻止这个事件的默认行为可以取消提交表单。

```js
let form = document.getElementById("myForm");

form.addEventListener("submit", (event) => {
	// 阻止表单提交
	event.preventDefault();
});
```

解决这个问题主要有两种方式：在表单提交后禁用提交按钮，或者通过 onsubmit 事件处理程序取消之后的表单提交。

#### 19.1.2 重置表单 ####

用户单击重置按钮可以重置表单。重置按钮可以使用 type 属性为 "reset" 的 <input> 或 <button>元素来创建

用户单击重置按钮重置表单会触发 reset 事件。这个事件为取消重置提供了机会。

#### 19.1.3 表单字段 ####

表单元素可以像页面中的其他元素一样使用原生 DOM 方法来访问。此外，所有表单元素都是表单elements 属性（元素集合）中包含的一个值。

这个 elements 集合是一个有序列表，包含对表单中所有字段的引用，包括所有 <input> 、 <textarea> 、 <button> 、 <select> 和 <fieldset> 元素

可以通过索引位置和 name 属性来访问。

**1. 表单字段的公共属性**

- disabled ：布尔值，表示表单字段是否禁用。
- form ：指针，指向表单字段所属的表单。这个属性是只读的。
- name ：字符串，这个字段的名字。
- readOnly ：布尔值，表示这个字段是否只读。
- tabIndex ：数值，表示这个字段在按 Tab 键时的切换顺序。
- type ：字符串，表示字段类型，如 "checkbox" 、 "radio" 等。
- value ：要提交给服务器的字段值。

这种动态修改表单字段属性的能力为任何时候以任何方式修改表单提供了方便。

**2. 表单字段的公共方法**

- focus()  方法把浏览器焦点设置到表单字段，这意味着该字段会变成活动字段并可以响应键盘事件。
- blur()

### 19.2 文本框编程 ###

#### 19.2.4 约束验证API ####

**1. 必填字段**

第一个条件是给表单字段添加 required 属性

```html
<input type="text" name="username" required>
```

**4. 输入模式**

HTML5 为文本字段新增了 pattern 属性。这个属性用于指定一个正则表达式，用户输入的文本必须与之匹配。

```html
<input type="text" pattern="\d+" name="count">
```

**5. 检测有效性**

使用 checkValidity() 方法可以检测表单中任意给定字段是否有效。

checkValidity() 方法只会告诉我们字段是否有效，而 validity 属性会告诉我们字段为什么有效或无效。

**6. 禁用验证**

通过指定 novalidate 属性可以禁止对表单进行任何验证：

```html
<form method="post" action="/signup" novalidate>

</form>
```

### 19.3 选择框编程 ###

选择框是使用 <select> 和 <option> 元素创建的.  HTMLSelectElement

- add(newOption, relOption) ：在 relOption 之前向控件中添加新的 <option>
- multiple ：布尔值，表示是否允许多选，等价于 HTML 的 multiple 属性
- options ：控件中所有 <option> 元素的 HTMLCollection, Node.
- remove(index) ：移除给定位置的选项
- selectedIndex ：选中项基于 0 的索引值，如果没有选中项则为–1。
- size ：选择框中可见的行数，等价于 HTML 的 size 属性
- type: 可能是 "select-one" 或 "select-multiple"
- value: 

```html
<select name="location" id="selLocation">
	<option value="Sunnyvale, CA">Sunnyvale</option>
	<option value="Los Angeles, CA">Los Angeles</option>
	<option value="Mountain View, CA">Mountain View</option>
	<option value="">China</option>
	<option>Australia</option>
</select>
```

每个 <option> 元素在 DOM 中都由一个 HTMLOptionElement 对象表示.

```python
class HTMLOptionElement(HTMLElement):
    index = None  # 选项在 options 集合中的索引
    label = Node  # 选项的标签，等价于 HTML 的 label 属性
    selected = None  # 布尔值，表示是否选中了当前选项。
    text = None  # 选项的文本
    value = None  # 选项的值
```

#### 19.3.1 选项处理 ####

对于只允许选择一项的选择框，获取选项最简单的方式是使用选择框的 selectedIndex 属性。

- 操作select的selectedIndex
- 操作option的selected

与 selectedIndex 不同，设置选项的 selected 属性不会在多选时移除其他选项，从而可以动态选择任意多个选项。

#### 19.3.2 添加选项 ####

```js
let newOption = document.createElement("option");
newOption.appendChild(document.createTextNode("Option text"));
newOption.setAttribute("value", "Option value");
selectbox.appendChild(newOption);
```

也可以使用 Option 构造函数创建新选项.

```js
let newOption = new Option("Option text", "Option value");
selectbox.appendChild(newOption); 
selectbox.add(newOption, undefined);
```

#### 19.3.3 移除选项 ####

- 使用DOM的removeChild
- 使用select的remove方法

### 19.4 表单序列化 ###

如何确定在提交表单时要把什么发送到服务器

- 字段名和值是 URL 编码的并以和号（ & ）分隔
- 禁用字段不会发送
- 复选框或单选按钮只在被选中时才发送
- 类型为 "reset" 或 "button" 的按钮不会发送
- 多选字段的每个选中项都有一个值
- 通过点击提交按钮提交表单时，会发送该提交按钮
- select 元素的值是被选中 <option> 元素的 value 属性

## 20 JavaScript API ##

### 20.1 Atomics & SharedArrayBuffer ###

#### 20.1.1 SharedArrayBuffer ####

### 20.3 Encoding API ###

Encoding API 主要用于实现字符串与定型数组之间的转换.

TextEncoder 、 TextEncoderStream 、 TextDecoder 和 TextDecoderStream

#### 20.3.1 文本编码 ####

Encoding API 提供了两种将字符串转换为定型数组二进制格式的方法：批量编码和流编码。把字符串转换为定型数组时，编码器始终使用 UTF-8。

```js
const textEn = new TextEncoder();
let v = 'foo';
let d = textEn.encode(v)
// Uint8Array(3) [102, 111, 111]
```

编码器实例还有一个 encodeInto() 方法，该方法接收一个字符串和目标 Unit8Array ，返回一个字典，该字典包含 read 和 written 属性。

#### 20.3.2 文本解码 ####

### 20.4 File API & Blob API ###

当用户在文件字段中选择一个或多个文件时，这个 files集合中会包含一组 File 对象，表示被选中的文件。

每个File对象都有一些只读属性：

- name: 本地系统中的文件名
- size: 以字节计的文件大小
- type: 包含文件 MIME 类型的字符串
- lastModifiedDate: 表示文件最后修改时间的字符串

#### 20.4.2 FileReader 类型 ####

FileReader 类型表示一种异步文件读取机制。

- readAsText(file, encoding) ：从文件中读取纯文本内容并保存在 result 属性中。第二个参数表示编码，是可选的。
- readAsDataURL(file) ：读取文件并将内容的数据 URI 保存在 result 属性中
- readAsBinaryString(file) ：读取文件并将每个字符的二进制数据保存在 result 属性中
- readAsArrayBuffer(file) ：读取文件并将文件内容以 ArrayBuffer 形式保存在 result 属性

因为这些读取方法是异步的，所以每个 FileReader 会发布几个事件，其中 3 个最有用的事件是 progress 、 error 和 load ，分别表示还有更多数据、发生了错误和读取完成。

其中 progress 事件每50ms就会触发一次，该事件有：lengthComputable 、 loaded 和 total 。此外，在 progress 事件中可以读取 FileReader 的 result 属性，即使其中尚未包含全部数据。

error 事件会在由于某种原因无法读取文件时触发。触发 error 事件时， FileReader 的 error属性会包含错误信息。这个属性是一个对象，只包含一个属性： code 。这个错误码的值可能是 1（未找到文件）、2（安全错误）、3（读取被中断）、4（文件不可读）或 5（编码错误）。

```js
let fileslist = document.getelementbyid("ff");
fileslist.addeventlistener("change", (event) => {
    let info = "",
        output = document.getelementbyid("output"),
        progress = document.getelementbyid("progress"),
        files = event.target.files,
        type = "default",
        reader = new filereader();

    if (/image/.test(files[0].type)) {
        reader.readasdataurl(files[0]);
        type = "image";
    } else {
        reader.readastext(files[0]);
        type = "text";
    }

    reader.onerror = function () {
        output.innerhtml = "could not read file, error code is " +
            reader.error.code;
    };

    reader.onprogress = function (event) {
        if (event.lengthcomputable) {
            progress.innerhtml = `${event.loaded}/${event.total}`;
        }
    };

    reader.onload = function () {
        let html = "";

        switch (type) {
            case "image":
                html = `<img src="${reader.result}">`;
                break;
            case "text":
                html = reader.result;
                break;
        }
        output.innerhtml = html;
    };
});
```

#### 20.4.3 FileReaderSync 类型 ####

 FileReaderSync 类型就是 FileReader 的同步版本.

#### 20.4.4 Blob与部分读取 ####

File 对象提供了一个名为 slice()的方法。 slice() 方法接收两个参数：起始字节和要读取的字节数。这个方法返回一个 Blob 的实例，而 Blob 实际上是 File 的超类。

Blob构造函数可以接收一个 options 参数，并在其中指定 MIME 类型。

Blob 对象有一个 size 属性和一个 type 属性，还有一个 slice() 方法用于进一步切分数据。另外也可以使用 FileReader 从 Blob 中读取数据。

#### 20.4.5 对象URL与Blob ####

对象 URL 有时候也称作 Blob URL，是指引用存储在 File 或 Blob 中数据的 URL。

要创建对象 URL，可以使用 window.URL.createObjectURL() 方法并传入 File 或 Blob 对象。

这个函数返回的值是一个指向内存中地址的字符串。因为这个字符串是 URL，所以可以在 DOM 中直接使用。

### 20.7 Notifications API ###

Notifications API 在 Service Worker 中非常有用。渐进 Web 应用（PWA，Progressive Web Application）通过触发通知可以在页面不活跃时向用户显示消息，看起来就像原生应用。

#### 20.7.1 通知权限 ####

用户授权显示通知是通过浏览器内部的一个对话框完成的。

```js
Notification.requestPermission()
.then((permission) => {
console.log('User responded to permission request:', permission);
});
```

#### 20.7.2 显示和隐藏通知 ####

显示一个简单的通知：

```js
new Notification('Title text!');
```

### 20.8 Page Visibility API ###

如果页面被最小化或隐藏在其他标签页后面，那么轮询服务器或更新动画等功能可能就没有必要了。Page Visibility API 旨在为开发者提供页面对用户是否可见的信息。

- document.visibilityState
  - 页面在后台标签页或浏览器中最小化了
  - 页面在前台标签页中
  - 实际页面隐藏了，但对页面的预览是可见的
  - 页面在屏外预渲染
- visibilitychange: 该事件会在文档从隐藏变可见（或反之）时触发
- document.hidden 布尔值，表示页面是否隐藏。

### 20.10 计时API ###

Performance 接口通过 JavaScript API 暴露了浏览器内部的度量指标，允许开发者直接访问这些信息并基于这些信息实现自己想要的功能。`window.performance`

#### 20.10.1 High Resolution Time API ####

必须使用不同的计时 API 来精确且准确地度量时间的流逝: `window.performance.now()`

performance.timeOrigin 属性返回计时器初始化时全局系统时钟的值
