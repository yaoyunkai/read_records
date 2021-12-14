# 官方指南 #

## 应用基础知识 ##

### 构建首个应用 ###

。。。。

### 应用基础知识 ###

每个 Android 应用都处于各自的安全沙盒中，并受以下 Android 安全功能的保护：

- Android 操作系统是一种多用户 Linux 系统，其中的每个应用都是一个不同的用户；
- 默认情况下，系统会为每个应用分配一个唯一的 Linux 用户 ID（该 ID 仅由系统使用，应用并不知晓）。系统会为应用中的所有文件设置权限，使得只有分配给该应用的用户 ID 才能访问这些文件；
- 每个进程都拥有自己的虚拟机 (VM)，因此应用代码独立于其他应用而运行。
- 默认情况下，每个应用都在其自己的 Linux 进程内运行。Android 系统会在需要执行任何应用组件时启动该进程，然后当不再需要该进程或系统必须为其他应用恢复内存时，其便会关闭该进程。

Android 系统实现了*最小权限原则*。换言之，默认情况下，每个应用只能访问执行其工作所需的组件，而不能访问其他组件。这样便能创建非常安全的环境，在此环境中，应用无法访问其未获得权限的系统部分。不过，应用仍可通过一些途径与其他应用共享数据以及访问系统服务：

- 可以安排两个应用共享同一 Linux 用户 ID，在此情况下，二者便能访问彼此的文件。为节省系统资源，也可安排拥有相同用户 ID 的应用在同一 Linux 进程中运行，并共享同一 VM。应用还必须使用相同的证书进行签名。
- 应用可以请求访问设备数据（如用户的联系人、短信消息、可装载存储装置（SD 卡）、相机、蓝牙等）的权限。用户必须明确授予这些权限。如需了解详细信息，请参阅[使用系统权限](https://developer.android.google.cn/training/permissions)。

#### 应用组件 ####

共有四种不同的应用组件类型：

- Activity
- 服务
- 广播接收器
- 内容提供程序

每种类型都有不同的用途和生命周期，后者会定义如何创建和销毁组件。以下部分将介绍应用组件的四种类型。

**Activity**

*Activity* 是与用户交互的入口点。它表示拥有界面的单个屏幕。Activity 有助于完成系统和应用程序之间的以下重要交互：

- 追踪用户当前关心的内容（屏幕上显示的内容），以确保系统继续运行托管 Activity 的进程。
- 了解先前使用的进程包含用户可能返回的内容（已停止的 Activity），从而更优先保留这些进程。
- 帮助应用处理终止其进程的情况，以便用户可以返回已恢复其先前状态的 Activity。
- 提供一种途径，让应用实现彼此之间的用户流，并让系统协调这些用户流。（此处最经典的示例是共享。）

**Service**

*服务*是一个通用入口点，用于因各种原因使应用在后台保持运行状态。它是一种在后台运行的组件，用于执行长时间运行的操作或为远程进程执行作业。服务不提供界面。

事实上，有两种截然不同的语义服务可以告知系统如何管理应用：已启动服务会告知系统使其运行至工作完毕。此类工作可以是在后台同步一些数据，或者在用户离开应用后继续播放音乐。在后台同步数据或播放音乐也代表了两种不同类型的已启动服务，而这些服务可以修改系统处理它们的方式：

- 音乐播放是用户可直接感知的服务，因此，应用会向用户发送通知，表明其希望成为前台，从而告诉系统此消息；在此情况下，系统明白它应尽全力维持该服务进程运行，因为进程消失会令用户感到不快。
- 通常，用户不会意识到常规后台服务正处于运行状态，因此系统可以更自由地管理其进程。如果系统需要使用 RAM 来处理用户更迫切关注的内容，则其可能允许终止服务（然后在稍后的某个时刻重启服务）。

**BroadcastReceiver**

借助*广播接收器*组件，系统能够在常规用户流之外向应用传递事件，从而允许应用响应系统范围内的广播通知。由于广播接收器是另一个明确定义的应用入口，因此系统甚至可以向当前未运行的应用传递广播。

许多广播均由系统发起，例如，通知屏幕已关闭、电池电量不足或已拍摄照片的广播。应用也可发起广播，例如，通知其他应用某些数据已下载至设备，并且可供其使用。

**ContentProvider**

*内容提供程序*管理一组共享的应用数据，您可以将这些数据存储在文件系统、SQLite 数据库、网络中或者您的应用可访问的任何其他持久化存储位置。其他应用可通过内容提供程序查询或修改数据（如果内容提供程序允许）。

我们很容易将内容提供程序看作数据库上的抽象，因为其内置的大量 API 和支持时常适用于这一情况。但从系统设计的角度看，二者的核心目的不同。对系统而言，内容提供程序是应用的入口点，用于发布由 URI 架构识别的已命名数据项。因此，应用可以决定如何将其包含的数据映射到 URI 命名空间，进而将这些 URI 分发给其他实体。反之，这些实体也可使用分发的 URI 来访问数据。在管理应用的过程中，系统可以执行以下特殊操作：

- 分配 URI 无需应用保持运行状态，因此 URI 可在其所属的应用退出后继续保留。当系统必须从相应的 URI 检索应用数据时，系统只需确保所属应用仍处于运行状态。
- 这些 URI 还会提供重要的细粒度安全模型。例如，应用可将其所拥有图像的 URI 放到剪贴板上，但将其内容提供程序锁定，以便其他应用程序无法随意访问它。当第二个应用尝试访问剪贴板上的 URI 时，系统可允许该应用通过临时的 *URI 授权*来访问数据，这样便只能访问 URI 后面的数据，而非第二个应用中的其他任何内容。

内容提供程序也适用于读取和写入您的应用不共享的私有数据。

当系统启动某个组件时，它会启动该应用的进程（如果尚未运行），并实例化该组件所需的类。例如，如果您的应用启动相机应用中拍摄照片的 Activity，则该 Activity 会在属于相机应用的进程（而非您的应用进程）中运行。因此，与大多数其他系统上的应用不同，Android 应用并没有单个入口点（即没有 `main()` 函数）。

##### 启动组件 #####

在四种组件类型中，有三种（Activity、Service和BroadcastReceiver）均通过异步消息 *Intent* 进行启动。

对于acitivity和service，Intent 会定义要执行的操作（例如，*查看*或*发送*某内容），并且可指定待操作数据的 URI，以及正在启动的组件可能需要了解的信息。

对于广播接收器，Intent 只会定义待广播的通知。例如，指示设备电池电量不足的广播只包含指示*“电池电量不足”*的已知操作字符串。

ContentProvider并非由 Intent 启动，它们会在成为 `ContentResolver` 的请求目标时启动。

每种组件都有不同的启动方法：

- Activity： `startActivity()` 或 `startActivityForResult()` 
- JobScheduler / startService bindService
- 您可以通过向 `sendBroadcast()`、`sendOrderedBroadcast()` 或 `sendStickyBroadcast()` 等方法传递 `Intent` 来发起广播。
- 您可以通过在 `ContentResolver` 上调用 `query()`，对ContentProvider执行查询。

#### 清单文件 ####

在 Android 系统启动应用组件之前，系统必须通过读取应用的*清单*文件 (`AndroidManifest.xml`) 确认组件存在。

除了声明应用的组件外，清单文件还有许多其他作用，如：

- 确定应用需要的任何用户权限，如互联网访问权限或对用户联系人的读取权限。
- 根据应用使用的 API，声明应用所需的最低 [API 级别](https://developer.android.google.cn/guide/topics/manifest/uses-sdk-element#ApiLevels)。
- 声明应用使用或需要的硬件和软件功能，如相机、蓝牙服务或多点触摸屏幕。
- 声明应用需要链接的 API 库（Android 框架 API 除外），如 [Google 地图库](http://code.google.com/android/add-ons/google-apis/maps-overview.html)。

##### 声明组件 #####

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest ... >
    <application android:icon="@drawable/app_icon.png" ... >
        <activity android:name="com.example.project.ExampleActivity"
                  android:label="@string/example_label" ... >
        </activity>
        ...
    </application>
</manifest>
```

application:

- `android:icon` 属性指向标识应用的图标所对应的资源。

activity:

- `android:name` 属性指定 `Activity` 子类的完全限定类名
- `android:label` 属性指定用作 Activity 的用户可见标签的字符串。

您必须使用以下元素声明所有应用组件：

- Activity 的 `<activity>` 元素。
- 服务的 `<service>` 元素。
- 广播接收器的 `<receiver>` 元素。
- 内容提供程序的 `<provider>` 元素。

如果未在清单文件中声明源代码中包含的 Activity、服务和内容提供程序，则这些组件对系统不可见，因此也永远不会运行。

##### 声明组件功能 #####

在应用的清单文件中声明 Activity 时，您可以选择性地加入声明 Activity 功能的 Intent 过滤器，以便响应来自其他应用的 Intent。您可以将 [`<intent-filter>`](https://developer.android.google.cn/guide/topics/manifest/intent-filter-element) 元素作为组件声明元素的子项进行添加，从而为您的组件声明 Intent 过滤器。

```xml
<manifest ... >
    ...
    <application ... >
        <activity android:name="com.example.project.ComposeEmailActivity">
            <intent-filter>
                <action android:name="android.intent.action.SEND" />
                <data android:type="*/*" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

##### 声明应用要求 #####

```xml
<manifest ... >
    <uses-feature android:name="android.hardware.camera.any"
                  android:required="true" />
    <uses-sdk android:minSdkVersion="7" android:targetSdkVersion="19" />
    ...
</manifest>
```

#### 应用资源 ####

对于您在 Android 项目中加入的每一项资源，SDK 构建工具均会定义唯一的整型 ID，您可以利用此 ID 来引用资源，这些资源或来自应用代码，或来自 XML 中定义的其他资源。例如，如果您的应用包含名为 `logo.png` 的图像文件（保存在 `res/drawable/` 目录中），则 SDK 工具会生成名为 `R.drawable.logo` 的资源 ID。此 ID 映射到应用特定的整型数，您可以利用它来引用该图像，并将其插入您的界面。

#### 其他资源 ####

请继续阅读以下内容：

- [Intent 和 Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters)

  如何使用 `Intent` API 来启动应用组件（如 Activity 和服务），以及如何使您的应用组件可供其他应用使用。

- [Activity](https://developer.android.google.cn/guide/components/activities)

  如何创建 `Activity` 类的实例，该类可在您的应用内提供具有界面的独立屏幕。

- [提供资源](https://developer.android.google.cn/guide/topics/resources/providing-resources)

  如何通过构建 Android 应用将应用资源与应用代码分离，包括如何针对特定设备配置提供备用资源。

- [设备兼容性](https://developer.android.google.cn/guide/practices/compatibility)

  Android 如何在不同类型的设备上运行，并介绍如何针对不同设备优化应用，或如何限制应用在不同设备上的可用性。

- [系统权限](https://developer.android.google.cn/guide/topics/permissions)

  Android 如何通过权限系统来限制应用访问某些 API，该系统要求应用必须先征得用户同意，才能使用这些 API。

### 应用资源 ###

资源是指代码使用的附加文件和静态内容，例如位图、布局定义、界面字符串、动画说明等。

外部化应用资源后，您便可使用在项目 `R` 类中生成的资源 ID 来访问这些资源。

#### 分组资源类型 ####

应将各类资源放入项目 `res/` 目录的特定子目录中。

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

> 如需了解有关使用 mipmap 文件夹的详细信息，请参阅[管理项目概览](https://developer.android.google.cn/tools/projects#mipmap)。

项目 `res/` 目录中支持的资源目录。

| 目录        | 资源类型                                                     |
| :---------- | :----------------------------------------------------------- |
| `animator/` | 用于定义[属性动画](https://developer.android.google.cn/guide/topics/graphics/prop-animation)的 XML 文件。 |
| `anim/`     | 用于定义[渐变动画](https://developer.android.google.cn/guide/topics/graphics/view-animation#tween-animation)的 XML 文件。（属性动画也可保存在此目录中，但为了区分这两种类型，属性动画首选 `animator/` 目录。） |
| `color/`    | 用于定义颜色状态列表的 XML 文件。请参阅[颜色状态列表资源](https://developer.android.google.cn/guide/topics/resources/color-list-resource) |
| `drawable/` | 位图文件（`.png`、`.9.png`、`.jpg`、`.gif`）或编译为以下可绘制对象资源子类型的 XML 文件：<br />位图文件<br />九宫格（可调整大小的位图）<br />状态列表<br />形状<br />动画可绘制对象<br />其他可绘制对象<br />请参阅 [Drawable 资源](https://developer.android.google.cn/guide/topics/resources/drawable-resource)。 |
| `mipmap/`   | 适用于不同启动器图标密度的可绘制对象文件。如需了解有关使用 `mipmap/` 文件夹管理启动器图标的详细信息，请参阅[管理项目概览](https://developer.android.google.cn/tools/projects#mipmap)。 |
| `layout/`   | 用于定义用户界面布局的 XML 文件。请参阅[布局资源](https://developer.android.google.cn/guide/topics/resources/layout-resource)。 |
| `menu/`     | 用于定义应用菜单（如选项菜单、上下文菜单或子菜单）的 XML 文件。请参阅[菜单资源](https://developer.android.google.cn/guide/topics/resources/menu-resource)。 |
| `raw/`      | 需以原始形式保存的任意文件。如要使用原始 `InputStream` 打开这些资源，请使用资源 ID（即 `R.raw.filename`）调用 `Resources.openRawResource()`。<br /><br />但是，如需访问原始文件名和文件层次结构，则可以考虑将某些资源保存在 `assets/` 目录（而非 `res/raw/`）下。`assets/` 中的文件没有资源 ID，因此您只能使用 `AssetManager` 读取这些文件。 |
| `values/`   | 包含字符串、整型数和颜色等简单值的 XML 文件。<br /><br />其他 `res/` 子目录中的 XML 资源文件会根据 XML 文件名定义单个资源，而 `values/` 目录中的文件可描述多个资源。对于此目录中的文件，`<resources>` 元素的每个子元素均会定义一个资源。例如，`<string>` 元素会创建 `R.string` 资源，`<color>` 元素会创建 `R.color` 资源。<br /><br />由于每个资源均使用自己的 XML 元素进行定义，因此您可以随意命名文件，并在某个文件中放入不同的资源类型。但是，您可能需要将独特的资源类型放在不同的文件中，使其一目了然。例如，对于可在此目录中创建的资源，下面给出了相应的文件名约定：<br /><br />arrays.xml：资源数组（[类型数组](https://developer.android.google.cn/guide/topics/resources/more-resources#TypedArray)）。<br />colors.xml：[颜色值](https://developer.android.google.cn/guide/topics/resources/more-resources#Color)。<br />dimens.xml：[尺寸值](https://developer.android.google.cn/guide/topics/resources/more-resources#Dimension)。<br />strings.xml：[字符串值](https://developer.android.google.cn/guide/topics/resources/string-resource)。<br />styles.xml：[样式](https://developer.android.google.cn/guide/topics/resources/style-resource)。<br /><br />请参阅[字符串资源](https://developer.android.google.cn/guide/topics/resources/string-resource)、[样式资源](https://developer.android.google.cn/guide/topics/resources/style-resource)和[更多资源类型](https://developer.android.google.cn/guide/topics/resources/more-resources)。 |
| `xml/`      | 可在运行时通过调用 `Resources.getXML()` 读取的任意 XML 文件。各种 XML 配置文件（如[可搜索配置](https://developer.android.google.cn/guide/topics/search/searchable-config)）都必须保存在此处。 |
| `font/`     | 带有扩展名的字体文件（如 `.ttf`、`.otf` 或 `.ttc`），或包含 `<font-family>` 元素的 XML 文件。如需详细了解作为资源的字体，请参阅 [XML 中的字体](https://developer.android.google.cn/preview/features/fonts-in-xml)。 |

> 切勿将资源文件直接保存在 `res/` 目录内，因为这样会造成编译错误。

如需了解有关特定资源类型的详细信息，请参阅[资源类型](https://developer.android.google.cn/guide/topics/resources/available-resources)文档。

#### 提供备用资源 ####

