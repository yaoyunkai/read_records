# 菜单资源 #

菜单资源定义可通过 [`MenuInflater`](https://developer.android.google.cn/reference/android/view/MenuInflater) 进行扩充的应用菜单，包括选项菜单、上下文菜单和子菜单。

有关使用菜单的指南，请参阅[菜单](https://developer.android.google.cn/guide/topics/ui/menus)开发者指南。

**文件位置：**

`res/menu/filename.xml`

**编译后的资源数据类型**：

指向 `Menu`（或其子类）资源的资源指针。

**语法：**

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@[+][package:]id/resource_name"
          android:title="string"
          android:titleCondensed="string"
          android:icon="@[package:]drawable/drawable_resource_name"
          android:onClick="method name"
          android:showAsAction=["ifRoom" | "never" | "withText" | "always" | "collapseActionView"]
          android:actionLayout="@[package:]layout/layout_resource_name"
          android:actionViewClass="class name"
          android:actionProviderClass="class name"
          android:alphabeticShortcut="string"
          android:alphabeticModifiers=["META" | "CTRL" | "ALT" | "SHIFT" | "SYM" | "FUNCTION"]
          android:numericShortcut="string"
          android:numericModifiers=["META" | "CTRL" | "ALT" | "SHIFT" | "SYM" | "FUNCTION"]
          android:checkable=["true" | "false"]
          android:visible=["true" | "false"]
          android:enabled=["true" | "false"]
          android:menuCategory=["container" | "system" | "secondary" | "alternative"]
          android:orderInCategory="integer" />
    <group android:id="@[+][package:]id/resource name"
           android:checkableBehavior=["none" | "all" | "single"]
           android:visible=["true" | "false"]
           android:enabled=["true" | "false"]
           android:menuCategory=["container" | "system" | "secondary" | "alternative"]
           android:orderInCategory="integer" >
        <item />
    </group>
    <item >
        <menu>
            <item />
        </menu>
    </item>
</menu>
```

**元素：**

`<menu>` **必需**。该元素必须是根节点。包含 `<item>` 和/或 `<group>` 元素。

`<item>` 菜单项。可能包含 `<menu>` 元素（用于子菜单）。必须是 `<menu>` 或 `<group>` 元素的子元素。

属性：

- `android:id` 资源 ID。唯一资源 ID。要为此项创建新的资源 ID，请使用以下形式：`"@+id/*name*"`。加号表示应将其创建为新 ID。

- `android:title` 字符串资源。字符串资源或原始字符串形式的菜单标题。

- `android:titleCondensed` 字符串资源。字符串资源或原始字符串形式的压缩标题。此标题在正常标题过长的情况下使用。

- `android:icon` 可绘制资源。用作菜单项图标的图片。

- `android:onClick` 方法名称。点击此菜单项时调用的方法。

- `android:showAsAction` 关键字。指示此项应在应用栏中显示为操作项的时机和方式。菜单项只有在 Activity 包含应用栏时才能显示为操作项。

  | 值                   | 说明                                                         |
  | :------------------- | :----------------------------------------------------------- |
  | `ifRoom`             | 只有在应用栏中有空间的情况下，才将此项放置其中。如果没有足够的空间来容纳标记为 `"ifRoom"` 的所有项，则 `orderInCategory` 值最低的项会显示为操作，其余项将显示在溢出菜单中。 |
  | `withText`           | 此外，还会随操作项添加标题文本（由 `android:title` 定义）。您可以将此值与某个其他值一起作为标记集添加，用竖线 `|` 分隔。 |
  | `never`              | 不得将此项放在应用栏中，而应将其列在应用栏的溢出菜单中。     |
  | `always`             | 始终将此项放在应用栏中。除非此项必须始终显示在操作栏中，否则请勿使用该值。将多个项设置为始终显示为操作项，会导致它们与应用栏中的其他界面重叠。 |
  | `collapseActionView` | 与此操作项相关联的操作视图（由 `android:actionLayout` 或 `android:actionViewClass` 声明）是可收起的。 在 API 级别 14 中引入。 |

- `android:actionLayout` 布局资源。用作操作视图的布局。

- `android:actionViewClass` 类名称。要用作操作视图的 `View` 的完全限定类名称。

- `android:actionProviderClass` 类名称。要用于代替操作项的 `ActionProvider` 的完全限定类名称。

- `android:alphabeticShortcut` 字符。字母快捷键的字符。

- `android:numericShortcut` 整数。数字快捷键的数字。

- `android:alphabeticModifiers`

- `android:numericModifiers`

- `android:checkable` 布尔值。如果该项可勾选，则为“true”。

- `android:checked` 布尔值。如果默认情况下该项为勾选状态，则为“true”。

- `android:visible`  布尔值。如果默认情况下该项可见，则为“true”。

- `android:enabled` 布尔值。如果默认情况下该项为启用状态，则为“true”。

- `android:menuCategory` 关键字。对应于 `Menu` `CATEGORY_*` 常量的值，这些常量用于定义项的优先级。

- `android:orderInCategory` 整数。项在组内的“重要性”顺序。

`<group>` 一个菜单组，用于创建一组具有相同特征（例如是否可见、是否启用或是否可勾选）的项。包含一个或多个 `<item>` 元素。必须是 `<menu>` 元素的子元素。

