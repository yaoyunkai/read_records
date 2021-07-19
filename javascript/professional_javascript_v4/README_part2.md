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

