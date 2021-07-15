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

