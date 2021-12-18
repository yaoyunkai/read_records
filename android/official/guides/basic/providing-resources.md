# 应用资源概览 #

资源是指代码使用的附加文件和静态内容，例如位图、布局定义、界面字符串、动画说明等。

您应始终外部化应用资源（例如图像和代码中的字符串），以便单独对其进行维护。

## 分组资源类型 ##

您应将各类资源放入项目 `res/` 目录的特定子目录中。

```
MyProject/
    src/
        MyActivity.java
    res/
        drawable/
            graphic.png
        layout/
            main.xml
            info.xml
        mipmap/
            icon.png
        values/
            strings.xml
```

> **请注意：**如需了解有关使用 mipmap 文件夹的详细信息，请参阅[管理项目概览](https://developer.android.google.cn/tools/projects#mipmap)。

| 目录        | 资源类型                                                     |
| :---------- | :----------------------------------------------------------- |
| `animator/` | 用于定义[属性动画](https://developer.android.google.cn/guide/topics/graphics/prop-animation)的 XML 文件。 |
| `anim/`     | 用于定义[渐变动画](https://developer.android.google.cn/guide/topics/graphics/view-animation#tween-animation)的 XML 文件。（属性动画也可保存在此目录中，但为了区分这两种类型，属性动画首选 `animator/` 目录。） |
| `color/`    | 用于定义颜色状态列表的 XML 文件。请参阅[颜色状态列表资源](https://developer.android.google.cn/guide/topics/resources/color-list-resource) |
| `drawable/` | 位图文件（`.png`、`.9.png`、`.jpg`、`.gif`）或编译为以下可绘制对象资源子类型的 XML 文件。<br />请参阅 [Drawable 资源](https://developer.android.google.cn/guide/topics/resources/drawable-resource)。 |
| `mipmap/`   | 适用于不同启动器图标密度的可绘制对象文件。如需了解有关使用 `mipmap/` 文件夹管理启动器图标的详细信息，请参阅[管理项目概览](https://developer.android.google.cn/tools/projects#mipmap)。 |
| `layout/`   | 用于定义用户界面布局的 XML 文件。请参阅[布局资源](https://developer.android.google.cn/guide/topics/resources/layout-resource)。 |
| `menu/`     | 用于定义应用菜单（如选项菜单、上下文菜单或子菜单）的 XML 文件。请参阅[菜单资源](https://developer.android.google.cn/guide/topics/resources/menu-resource)。 |
| `raw/`      | 需以原始形式保存的任意文件。                                 |
| `values/`   | 包含字符串、整型数和颜色等简单值的 XML 文件。<br /><br />其他 `res/` 子目录中的 XML 资源文件会根据 XML 文件名定义单个资源，而 `values/` 目录中的文件可描述多个资源。对于此目录中的文件，`<resources>` 元素的每个子元素均会定义一个资源。例如，`<string>` 元素会创建 `R.string` 资源，`<color>` 元素会创建 `R.color` 资源。 |
| `xml/`      | 可在运行时通过调用 `Resources.getXML()` 读取的任意 XML 文件。各种 XML 配置文件（如[可搜索配置](https://developer.android.google.cn/guide/topics/search/searchable-config)）都必须保存在此处。 |
| `font/`     | 带有扩展名的字体文件（如 `.ttf`、`.otf` 或 `.ttc`），或包含 `<font-family>` 元素的 XML 文件。如需详细了解作为资源的字体，请参阅 [XML 中的字体](https://developer.android.google.cn/preview/features/fonts-in-xml)。 |

## 提供备用资源 ##

几乎每个应用都应提供备用资源，以便支持特定的设备配置。

![img](.assets/resource_devices_diagram2.png)

为一组资源指定配置特定的备用资源：

1. 在 `res/` 中创建以 `<resources_name>-<config_qualifier>` 形式命名的新目录。
1. 将相应的备用资源保存在此新目录下。这些资源文件必须与默认资源文件完全同名。

| 配置                 | 限定符值                                                     | 描述                                                         |
| :------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| MCC 和 MNC           | 示例：<br />mcc310<br />mcc310-mnc004<br />mcc208-mnc00      | 移动设备国家代码 (MCC)<br /><br />另请参阅配置字段 `mcc` 和 `mnc`，二者分别表示当前的移动设备国家代码和移动设备网络代码。 |
| 语言和区域           | 示例：<br />en<br />fr<br />en-rUs<br />fr-fFR<br />fr-rCA   | 语言通过由两个字母组成的 [ISO 639-1](http://www.loc.gov/standards/iso639-2/php/code_list.php) 语言代码进行定义，可以选择后跟两个字母组成的 [ISO 3166-1-alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) 区域码（前缀用小写字母 `r`）。 |
| 布局方向             | ldrtl<br />ldltr                                             | 应用的布局方向。`ldrtl` 是指“布局方向从右到左”。`ldltr` 是指“布局方向从左到右”（默认的隐式值）。 |
| smallestWidth        | `sw<N>dp`<br /><br />示例：<br />sw320dp<br />sw600dp<br />sw720dp | 屏幕的基本尺寸，由可用屏幕区域的最小尺寸指定。<br />另请参阅 [`android:requiresSmallestWidthDp`](https://developer.android.google.cn/guide/topics/manifest/supports-screens-element#requiresSmallest) 属性（声明与应用兼容的最小 smallestWidth）和 `smallestScreenWidthDp` 配置字段（存放设备的 smallestWidth 值）。 |
| 可用宽度             | `w<N>dp`<br /><br />示例:<br />w720dp<br />w1024dp           | 指定资源应使用的最小可用屏幕宽度（以 `dp` 为单位，由 `<N>` 值定义）。当屏幕方向在横向和纵向之间切换时，此配置值也会随之变化，以匹配当前的实际宽度。<br />另请参阅 `screenWidthDp` 配置字段，该字段存放当前屏幕宽度。 |
| 可用高度             | `h<N>dp`<br /><br />示例：<br />h720dp<br />h1024dp          | 指定资源应使用的最小可用屏幕高度（以“dp”为单位，由 `<N>` 值定义）。当屏幕方向在横向和纵向之间切换时，此配置值也会随之变化，以匹配当前的实际高度。<br />另请参阅 `screenHeightDp` 配置字段，该字段存放当前屏幕宽度。 |
| 屏幕尺寸             | small<br />normal<br />large<br />xlarge                     | 另请参阅 `screenLayout` 配置字段，该字段指示屏幕是小尺寸、标准尺寸还是大尺寸。 |
| 屏幕纵横比           | long<br />notlong                                            | 另请参阅 `screenLayout` 配置字段，该字段指示屏幕是否为宽屏。 |
| 圆形屏幕             | round<br />notround                                          | 另请参阅 `isScreenRound()` 配置方法，该方法指示屏幕是否为圆形屏幕。 |
| 广色域               | widecg<br />nowidecg                                         | 另请参阅 `isScreenWideColorGamut()` 配置方法，该方法指示屏幕是否具有广色域。 |
| 高动态范围           | highdr<br />lowdr                                            | 另请参阅 `isScreenHdr()` 配置方法，该方法指示屏幕是否具有 HDR 功能。 |
| 屏幕方向             | port<br />land                                               | 如果用户旋转屏幕，此配置可能会在应用生命周期中发生变化。如需了解这会在运行时期间给应用带来哪些影响，请参阅[处理运行时变更](https://developer.android.google.cn/guide/topics/resources/runtime-changes)。<br />另请参阅 `orientation` 配置字段，该字段指示当前的设备方向。 |
| 界面模式             | car<br />desk<br />television<br />appliance<br />watch<br />vrheadset |                                                              |
| 夜间模式             | night<br />notnight                                          | 如果夜间模式停留在自动模式（默认），此配置可能会在应用生命周期中发生变化。在此情况下，该模式会根据当天的时间进行调整。您可以使用 `UiModeManager` 启用或禁用此模式。 |
| 屏幕像素密度(dpi)    | ldpi<br />mdpi<br />hdpi<br />xhdpi<br />xxhdpi<br />xxxhdpi<br />nodpi<br />tvdpi<br />anydpi<br />*nnn*dpi |                                                              |
| 触摸屏类型           | notouch<br />finger                                          | 另请参阅 `touchscreen` 配置字段，该字段指示设备上的触摸屏类型。 |
| 键盘可用性           | keysexposed<br />keyshidden<br />keyssoft                    | 另请参阅配置字段 `hardKeyboardHidden` 和 `keyboardHidden`，二者分别指示硬键盘的可见性和任一键盘（包括软键盘）的可见性。 |
| 主要的文本输入法     | nokeys<br />qwerty<br />12key                                | 另请参阅 `keyboard` 配置字段，该字段指示可用的主要文本输入法。 |
| 导航键可用性         | navexposed<br />navhidden                                    | 另请参阅 `navigationHidden` 配置字段，该字段指示导航键是否处于隐藏状态。 |
| 主要的非触摸导航方式 | nonav<br />dpad<br />trackball<br />wheel                    | 另请参阅 `navigation` 配置字段，该字段指示可用的导航方法类型。 |
| 平台版本             | 示例：<br />v3<br />v4<br />v7                               | 如需了解有关这些值的详细信息，请参阅 [Android API 级别](https://developer.android.google.cn/guide/topics/manifest/uses-sdk-element#ApiLevels)文档。 |

### 限定符命名规则 ###

- 可以为单组资源指定多个限定符，并使用短划线分隔。
- 限定符必须遵循表 2 中列出的顺序。
- 不能嵌套备用资源目录。
- 值不区分大小写。在处理之前，资源编译器会将目录名称转换为小写，以免不区分大小写的文件系统出现问题。名称中使用的所有大写字母只是为了便于认读。
- 每种限定符类型仅支持一个值。

在将备用资源保存到以这些限定符命名的目录中后，Android 会根据当前设备配置在应用中自动应用这些资源。

### 创建别名资源 ###

如果您想将某一资源用于多种设备配置（但不想以默认资源的形式提供该资源），则无需将同一资源放入多个备用资源目录中。相反，您可以（在某些情况下）创建备用资源，充当默认资源目录中所保存资源的别名。

例如，假设您有一个应用图标 `icon.png`，并且需要用于不同语言区域的独特版本。但是，加拿大英语和加拿大法语这两种语言区域需使用同一版本。您可能会认为，需要将相同图像复制到加拿大英语和加拿大法语所对应的资源目录中，但事实并非如此。相反，您可以将用于二者的图像保存为 `icon_ca.png`（除 `icon.png` 以外的任何名称），并将其放入默认的 `res/drawable/` 目录中。然后，在 `res/drawable-en-rCA/` 和 `res/drawable-fr-rCA/` 中创建 `icon.xml` 文件，使用 `<bitmap>` 元素引用 `icon_ca.png` 资源。这样，您只需存储 PNG 文件的一个版本和两个指向该版本的小型 XML 文件。

## 访问应用资源 ##

在应用中提供资源后，您可通过引用其资源 ID 来应用该资源。所有资源 ID 都在您项目的 `R` 类中进行定义，该类由 `aapt` 工具自动生成。

编译应用时，`aapt` 会生成 `R` 类，其中包含 `res/` 目录中所有资源的资源 ID。每个资源类型都有对应的 `R` 子类（例如，`R.drawable` 对应所有可绘制对象资源），而该类型的每个资源都有对应的静态整型数（例如，`R.drawable.icon`）。该整型数就是可用来检索资源的资源 ID。

资源 ID 始终由以下部分组成：

- *资源类型*：每个资源都被分到一个“类型”组中，例如 `string`、`drawable` 和 `layout`。
- *资源名称*，它是不包括扩展名的文件名；或是 XML `android:name` 属性中的值（如资源是字符串等简单值）。

### 在代码中访问资源 ###

您可以以方法参数的形式传递资源 ID，进而在代码中使用资源。

```java
ImageView imageView = (ImageView) findViewById(R.id.myimageview);
imageView.setImageResource(R.drawable.myimage);
```

**语法**

以下是在代码中引用资源的语法：

```
[<package_name>.]R.<resource_type>.<resource_name>
```

- `<package_name>` 是资源所在包的名称（如果引用的资源来自您自己的资源包，则不需要）。
- `<resource_type>` 是资源类型的 `R` 子类。
- `<resource_name>` 是不带扩展名的资源文件名，或 XML 元素中的 `android:name` 属性值（若资源是简单值）。

### 在XML中访问资源 ###

可以使用对现有资源的引用，为某些 XML 属性和元素定义值。创建布局文件时，为给您的微件提供字符串和图像，您会经常这样做。

```xml
<Button
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:text="@string/submit" />
```

**语法**

以下是在 XML 资源中引用资源的语法：

```xml
@[<package_name>:]<resource_type>/<resource_name>
```

- `<package_name>` 是资源所在包的名称（如果引用的资源来自相同资源包，则不需要）
- `<resource_type>` 是资源类型的 `R` 子类
- `<resource_name>` 是不带扩展名的资源文件名，或 XML 元素中的 `android:name` 属性值（若资源是简单值）。

### 访问原始文件 ###

如果确有需要，则将文件保存在 `res/` 中并没有用，因为从 `res/` 读取资源的唯一方法是使用资源 ID。您可以改为将资源保存在 `assets/` 目录中。

保存在 `assets/` 目录中的文件*没有*资源 ID，因此您无法通过 `R` 类或在 XML 资源中引用它们。您可以改为采用类似普通文件系统的方式查询 `assets/` 目录中的文件，并利用 `AssetManager` 读取原始数据。

### 访问平台资源 ###

Android 包含许多标准资源，例如样式、主题背景和布局。如要访问这些资源，请通过 `android` 包名称限定您的资源引用。

```java
setListAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, myarray));
```

## 利用资源提供最佳设备兼容性 ##

为使应用支持多种设备配置，请务必为应用使用的每种资源类型提供默认资源，这一点非常重要。

## Android 如何查找最佳匹配资源 ##

https://developer.android.google.cn/guide/topics/resources/providing-resources#BestMatch

