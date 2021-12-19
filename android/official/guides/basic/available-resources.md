# 资源类型概览 #

本部分中的每个页面介绍了一种您可以在项目资源目录 (`res/`) 中提供的[应用资源](https://developer.android.google.cn/guide/topics/resources/providing-resources)的用法、格式和语法。

以下是对每个页面的简要说明：

- [动画资源](./animation-resource.md)
  定义预先确定的动画。
  补间动画保存在 res/anim/ 中并通过 R.anim 类访问。
  帧动画保存在 res/drawable/ 中并通过 R.drawable 类访问。
- [颜色状态列表资源](./color-list-resource.md)
  定义根据 View 状态而变化的颜色资源。
  保存在 res/color/ 中并通过 R.color 类访问。
- [可绘制资源](./drawable-resource.md)
  使用位图或 XML 定义各种图形。
  保存在 res/drawable/ 中并通过 R.drawable 类访问。
- 布局资源
  定义应用界面的布局。
  保存在 res/layout/ 中并通过 R.layout 类访问。
- [菜单资源](./menu-resource.md)
  定义应用菜单的内容。
  保存在 res/menu/ 中并通过 R.menu 类访问。
- [字符串资源](./string-resource.md)
  定义字符串、字符串数组和复数形式（并包括字符串格式和样式）。
  保存在 res/values/ 中，并通过 R.string、R.array 和 R.plurals 类访问。
- 样式资源
  定义界面元素的外观和格式。
  保存在 res/values/ 中并通过 R.style 类访问。
- 字体资源
  在 XML 中定义字体系列并包含自定义字体。
  保存在 res/font/ 中并通过 R.font 类访问。
- 更多资源类型
  将其他原始值定义为静态资源，具体包括：
  - Bool
    包含布尔值的 XML 资源。
  - 颜色
    包含颜色值（十六进制颜色）的 XML 资源。
  - 维度
    包含维度值（及度量单位）的 XML 资源。
  - ID
    为应用资源和组件提供唯一标识符的 XML 资源。
  - 整数
    包含整数值的 XML 资源。
  - 整数数组
    提供整数数组的 XML 资源。
  - 类型化数组
    提供 TypedArray（可用于可绘制对象数组）的 XML 资源。

-----

