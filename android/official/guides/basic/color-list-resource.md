# 颜色状态列表资源 #

[`ColorStateList` ](https://developer.android.google.cn/reference/android/content/res/ColorStateList)是一个您可以在 XML 中定义的对象，您可以将其作为颜色来应用，但它实际上会更改颜色，具体取决于其应用到的 `View` 对象的状态。

您可以在 XML 文件中描述状态列表。每种颜色都在单个 `<selector>` 元素内的 `<item>` 元素中定义。每个 `<item>` 使用不同的属性描述其应在什么状态下使用。

在每次状态更改期间，系统将从上到下遍历状态列表，并且将使用与当前状态匹配的第一项。系统的选择并非基于“最佳匹配”，而仅仅是基于符合状态的最低标准的第一项。

**文件位置：**

`res/color/filename.xml`

**编译后的资源数据类型：**

指向 `ColorStateList` 的资源指针。

**语法：**

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android" >
    <item
          android:color="hex_color"
          android:state_pressed=["true" | "false"]
          android:state_focused=["true" | "false"]
          android:state_selected=["true" | "false"]
          android:state_checkable=["true" | "false"]
          android:state_checked=["true" | "false"]
          android:state_enabled=["true" | "false"]
          android:state_window_focused=["true" | "false"] />
</selector>
```

**元素：**

`<selector>` **必需。**该元素必须是根元素。包含一个或多个 `<item>` 元素。

- `xmlns:android` 字符串。**必需。**定义 XML 命名空间，该命名空间必须为 `"http://schemas.android.com/apk/res/android"`

`<item>` 定义在某些状态下使用的颜色，状态通过其属性来描述。必须是 `<selector>` 元素的子元素。

- `android:color` 十六进制颜色。**必需**。颜色通过 RGB 值和可选的 Alpha 通道指定。
- `android:state_pressed` 布尔值。如果此项应在按下对象时（例如轻触/点按了按钮时）使用
- `android:state_focused` 布尔值。如果此项应在聚焦对象时（例如使用轨迹球/方向键突出显示按钮时）使用
- `android:state_selected` 布尔值。如果此项应在选择对象时（例如打开标签页时）使用，则为“true”；如果此项应在未选择对象时使用，则为“false”。
- `android:state_checkable` 布尔值。如果此项应在对象可勾选时使用，则为“true”；
- `android:state_checked` 布尔值。如果此项应在勾选对象时使用，则为“true”；如果应在取消勾选对象时使用，则为“false”。
- `android:state_enabled` 布尔值。如果此项应在启用对象（能够接收轻触/点按事件）时使用，则为“true”；如果应在停用对象时使用，则为“false”。
- `android:state_window_focused` 布尔值。如果此项应在应用窗口具有焦点（应用位于前台）时使用，则为“true”；

