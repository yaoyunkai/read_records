"""
The code created by Liberty on 2021/7/23

"""


class Node:
    """
    base node

    """
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12

    nodeType = None
    nodeName = None
    nodeValue = None

    childNodes = None
    parentNode = None
    previousSibling = None
    nextSibling = None
    firstChild = None
    lastChild = None
    ownerDocument = None

    def hasChildNodes(self, node):
        pass

    def appendChild(self, node):
        pass

    def insertBefore(self, newNode, beforeNode):
        pass

    def replaceChild(self, newNode, beforeNode):
        pass

    def removeChild(self, node):
        pass

    def cloneNode(self, deepClone):
        pass

    def normalize(self):
        pass


class Document(Node):
    nodeType = Node.DOCUMENT_NODE
    nodeName = '#document'
    ownerDocument = None

    documentElement = None  # html element
    body = None  # body element
    doctype = None  # DocumentType

    def getElementById(self, elementId):
        pass

    def getElementsByTagName(self, tagName):
        """

        :param tagName:
        :return: NodeList
        """
        pass

    def createElement(self, tagName):
        pass

    def createTextNode(self, text):
        return Text()

    def createDocumentFragment(self):
        return DocumentFragment()

    def createAttribute(self, attrName):
        return Attr()

    def querySelector(self, pattern):
        return Element()

    def querySelectorAll(self, pattern):
        pass

    def matches(self, pattern):
        pass

    def getElementsByClassName(self, className):
        """
        return NodeList

        :param className:
        :return:
        """
        pass


class HTMLDocument(Document):
    title = None  # document title
    URL = None  # URL 包含当前页面的完整 URL
    domain = None  # domain 包含页面的域名
    referrer = None  # referrer 包含链接到当前页面的那个页面的 URL

    anchors = None  # 包含文档中所有带 name 属性的 <a> 元素
    applets = None
    forms = None  # 可以获取页面上所有的表单元素
    images = None
    links = None

    implementation = None  # 查看实现了哪些特性 ????

    readyState = None  # loading or complete
    compatMode = None  # 检测页面渲染模式
    characterSet = None  # 表示文档实际使用的字符集
    dataset = None  # DOMStringMap 自定义属性

    styleSheets = None  # 表示文档中可用的样式表集合

    @property
    def sheet(self):
        return CSSStyleSheet()

    def getElementsByTagName(self, tagName):
        """
        HTMLCollection
            namedItem(name)

        :param tagName:
        :return: HTMLCollection
        """
        pass

    def getElementsByName(self, name):
        """

        :param name:
        :return: HTMLCollection
        """
        pass

    def write(self, text):
        pass

    def writeln(self, text):
        pass

    def open(self):
        pass

    def close(self):
        pass


class NamedNodeMap:

    def getNamedItem(self, name):
        # element.attributes["id"].nodeValue = "someOtherId";
        return Attr()

    def removeNamedItem(self, name):
        pass

    def setNamedItem(self, node):
        pass

    def item(self, pos):
        return Attr()


class Element(Node):
    nodeType = Node.ELEMENT_NODE
    nodeName = '<p>'
    nodeValue = None

    tagName = '<p>'
    attributes = NamedNodeMap()


class DOMTokenList:
    length = None

    def add(self, value):
        pass

    def contains(self, value):
        pass

    def remove(self, value):
        pass

    def toggle(self, value):
        pass


class CSSStyleDeclaration:
    backgroundImage = 'green'
    color = 'red'
    display = None
    fontFamily = None

    cssText = None  # 包含 style 属性中的 CSS 代码
    length = None  # 应用给元素的 CSS 属性数量
    parentRule = None  # 表示 CSS 信息的 CSSRule 对象

    def getPropertyCSSValue(self, propertyName):
        pass

    def getPropertyPriority(self, propertyName):
        pass

    def getPropertyValue(self, propertyName):
        pass

    def item(self, index):
        pass

    def removeProperty(self, propertyName):
        pass

    def setProperty(self, propertyName, value, priority):
        pass


class HTMLElement(Element):
    id = None
    title = None  # 包含元素的额外信息，通常以提示条形式展示
    lang = None
    dir = None  # 语言的书写方向  "ltr" 表示从左到右， "rtl" 表示从右到左
    className = None  # class 属性
    classList = DOMTokenList()
    innerHTML = None
    outerHTML = None
    innerText = None
    outerText = None

    style = CSSStyleDeclaration()  # 不包含通过层叠机制从文档样式和外部样式中继承来的样式

    def getAttribute(self, attrName):
        """

        :param attrName:
        :return: string for give attr
        """
        pass

    def setAttribute(self, attrName, attrValue):
        pass

    def removeAttribute(self, attrName):
        pass

    def setAttributeNode(self, attrNode):
        pass

    def getAttributeNode(self, attrName):
        return Attr()


class HTMLFormElement(HTMLElement):
    acceptCharset = None  # 服务器可以接收的字符集
    action = None  # 请求的 URL
    elements = None  # 表单中所有控件的 HTMLCollection
    enctype = None  # 请求的编码类型，等价于 HTML 的 enctype 属性
    length = None  # 表单中控件的数量
    method = None  # HTTP 请求的方法类型
    name = None  # 表单的名字
    target = None  # 用于发送请求和接收响应的窗口的名字

    def reset(self):
        pass

    def submit(self):
        pass


class HTMLSelectElement(HTMLElement):
    multiple = True  # 布尔值，表示是否允许多选，等价于 HTML 的 multiple 属性
    options = None  # 控件中所有 <option> 元素的 HTMLCollection
    selectedIndex = None  # 选中项基于 0 的索引值，如果没有选中项则为–1
    size = None  # 选择框中可见的行数，等价于 HTML 的 size 属性
    type = None  # 选择框的 type 属性可能是 "select-one" 或 "select-multiple"
    value = None

    def add(self, newOption, relOption):
        # 在 relOption 之前向控件中添加新的 <option>
        pass

    def remove(self, index):
        # 移除给定位置的选项
        pass


class HTMLOptionElement(HTMLElement):
    index = None  # 选项在 options 集合中的索引
    label = Node  # 选项的标签，等价于 HTML 的 label 属性
    selected = None  # 布尔值，表示是否选中了当前选项。
    text = None  # 选项的文本
    value = None  # 选项的值


class CSSStyleSheet:
    disabled = None
    href = None
    media = None  # 样式表支持的媒体类型集合
    ownerNode = HTMLElement()
    parentStyleSheet = None
    title = ownerNode.title  # ownerNode.title
    type = 'text/css'
    cssRules = None
    ownerRules = None

    def deleteRule(self, index):
        # 在指定位置删除 cssRules 中的规则
        pass

    def insertRule(self, rule, index):
        # 在指定位置向 cssRules 中插入规则
        pass


class CSSRule:
    cssText = None
    parentRule = None
    parentStyleSheet = CSSStyleSheet()
    selectorText = ''  # 返回规则的选择符文本
    style = CSSStyleDeclaration()  # 返回 CSSStyleDeclaration 对象，可以设置和获取当前规则中的样式
    type = 1  # 表示规则类型


class CharacterData(Node):
    data = 'nodeValue'

    def appendData(self, text):
        pass

    def deleteData(self, offset, count):
        pass

    def insertData(self, offset, text):
        pass

    def replaceData(self, offset, count, text):
        pass

    def substringData(self, offset, count):
        pass


class Text(CharacterData):
    nodeType = Node.TEXT_NODE
    nodeName = '#text'
    nodeValue = 'this is a text'  # Text 节点中包含的文本可以通过 nodeValue 属性访问

    length = len(nodeValue)

    def splitText(self, offset):
        pass


class Comment(CharacterData):
    nodeType = Node.COMMENT_NODE
    nodeName = '#comment'
    nodeValue = 'comment content'


class CDATASection(Node):
    nodeType = Node.CDATA_SECTION_NODE
    nodeName = '#cdata-section'
    nodeValue = 'CDATA content'


class DocumentType(Node):
    nodeType = Node.DOCUMENT_TYPE_NODE
    nodeName = 'html'
    nodeValue = None

    name = 'doctype'
    entities = NamedNodeMap()
    notations = NamedNodeMap()


class DocumentFragment(Node):
    nodeType = Node.DOCUMENT_FRAGMENT_NODE
    nodeName = '#document-fragment'
    nodeValue = None


class Attr(Node):
    nodeType = Node.ATTRIBUTE_NODE
    nodeName = 'color'
    nodeValue = 'red'

    name = 'color'
    value = 'red'
    specified = False
