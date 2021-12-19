# 应用清单概览 #

每个应用项目必须在[项目源设置](https://developer.android.google.cn/studio/build#sourcesets)的根目录中加入 `AndroidManifest.xml` 文件（且必须使用此名称）。 清单文件会向 Android 构建工具、Android 操作系统和 Google Play 描述应用的基本信息。

重点是，清单文件需声明以下内容：

- 应用的软件包名称，其通常与代码的命名空间相匹配。 构建项目时，Android 构建工具会使用此信息来确定代码实体的位置。 打包应用时，构建工具会使用 Gradle 构建文件中的应用 ID 来替换此值，而此 ID 则用作系统和 Google Play 上的唯一应用标识符。[了解关于软件包名称和应用 ID 的更多内容](https://developer.android.google.cn/guide/topics/manifest/manifest-intro#package-name)。
- 应用的组件，包括所有 Activity、服务、广播接收器和内容提供程序。 每个组件都必须定义基本属性，例如其 Kotlin 或 Java 类的名称。 清单文件还能声明一些功能，例如其所能处理的设备配置，以及描述组件如何启动的 Intent 过滤器。[了解关于应用组件的更多内容](https://developer.android.google.cn/guide/topics/manifest/manifest-intro#components)。
- 应用为访问系统或其他应用的受保护部分所需的权限。 如果其他应用想要访问此应用的内容，则清单文件还会声明其必须拥有的权限。 [了解关于权限的更多内容](https://developer.android.google.cn/guide/topics/manifest/manifest-intro#perms)。
- 应用需要的硬件和软件功能，这些功能会影响哪些设备能够从 Google Play 安装应用。[了解关于设备兼容性的更多内容](https://developer.android.google.cn/guide/topics/manifest/manifest-intro#compatibility)。

## 文件功能 ##

### 软件包名称和应用 ID ###

清单文件的根元素需包含应用软件包名称（通常与项目目录结构，即 Java 命名空间相匹配）的属性。

在将应用构建为最终的应用软件包 (APK) 时，Android 构建工具会使用 `package` 属性完成两件事情：

- 它会将此名称用作应用所生成 `R.java` 类（用于访问[应用资源](https://developer.android.google.cn/guide/topics/resources/overview)）的命名空间。
- 它会使用此名称解析清单文件中声明的任何相关类名称。

因此，清单 `package` 属性中的名称应始终与项目中保存 Activity 和其他应用代码的基础软件包的名称相匹配。 当然，您可以在项目中加入其他子软件包，但此类文件必须使用 `package` 属性的命名空间导入 `R.java` 类。

但请注意，APK 编译完成后，`package` 属性还可表示应用的通用唯一应用 ID。 当构建工具根据 `package` 名称执行上述任务后，它们会将 `package` 值替换为项目 `build.gradle` 文件（用于 Android Studio 项目）中赋予 `applicationId` 属性的值。 `package` 属性的这一最终值必须是通用唯一值，因为这是能确保在系统和 Google Play 中识别应用的唯一方式。

### 应用组件 ###

对于在应用中创建的每个[应用组件](https://developer.android.google.cn/guide/components/fundamentals#Components)，您必须在清单文件中声明相应的 XML 元素：

- `<activity>` 用于 `Activity` 的每个子类。
- `<service>` 用于 `Service` 的每个子类。
- `<receiver>` 用于 `BroadcastReceiver` 的每个子类。
- `<provider>` 用于 `ContentProvider` 的每个子类。

### Intent过滤器 ###

应用的 Activity、服务和广播接收器均由 *Intent* 激活。 Intent 是由 `Intent` 对象定义的消息，用于描述要执行的操作，其中包括要执行操作的数据、应执行操作的组件类别以及其他相关说明。

应用组件可包含任意数量的 Intent 过滤器（通过 `<intent-filter>` 元素定义），每个过滤器描述该组件的不同功能。

如需了解更多信息，请参阅 [Intent 和 Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters)文档。

### 图标和标签 ###

许多清单元素拥有 `icon` 和 `label` 属性，二者分别用于向对应应用组件的用户显示小图标和文本标签。

### 权限 ###

如要访问敏感用户数据（如联系人和短信）或某些系统功能（如相机和互联网访问），则 Android 应用必须请求相关权限。 每个权限均由唯一标签标识。 例如，如果应用需要发送短信，则必须在清单中添加以下代码行：

```xml
<manifest ... >
    <uses-permission android:name="android.permission.SEND_SMS"/>
    ...
</manifest>
```

### 设备兼容性 ###

清单文件也可用于声明应用所需的硬件或软件功能类型，以及应用兼容的设备类型。 Google Play 商店不允许在未提供应用所需功能或系统版本的设备上安装应用。

**`<uses-feature>`**

`<uses-feature>` 元素允许您声明应用所需的硬件和软件功能。

**`<uses-sdk>`** 

每个后续平台版本往往都会新增先前版本未提供的 API。 如要指明与应用兼容的最低版本，您的清单必须包含 `<uses-sdk>` 标签及其 minSdkVersion 属性。

## 文件约定 ##

**元素：**

只有 `<manifest>` 和 `<application>` 元素是必需的， 二者必须且只能出现一次。 大多数其他元素可以不出现或多次出现。 但是，必须提供某些元素才能使清单文件发挥作用。

**属性：**

严格来说，所有属性都是可选的。 但是，必须指定某些属性才可让元素实现其目的。 对于真正可选的属性，[参考文档](https://developer.android.google.cn/guide/topics/manifest/manifest-intro#reference)会指定默认值。

**多个值：**

如果可以指定多个值，则几乎总是在重复元素，而非列出单个元素内的多个值。

## 清单元素参考 ##

下表提供 `AndroidManifest.xml` 文件中所有有效元素的参考文档链接。

|                            |                                                              |
| -------------------------- | ------------------------------------------------------------ |
| `<action>`                 | 向 Intent 过滤器添加操作。                                   |
| `<activity>`               | 声明 Activity 组件。                                         |
| `<activity-alias>`         | 声明 Activity 的别名。                                       |
| `<application>`            | 应用的声明。                                                 |
| `<category>`               | 向 Intent 过滤器添加类别名称。                               |
| `<compatible-screens>`     | 指定与应用兼容的每个屏幕配置。                               |
| `<data>`                   | 向 Intent 过滤器添加数据规范。                               |
| `<grant-uri-permission>`   | 指定父级内容提供程序有权访问的应用数据的子集。               |
| `<instrumentation>`        | 声明支持您监控应用与系统进行交互的 `Instrumentation` 类。    |
| `<intent-filter>`          | 指定 Activity、服务或广播接收器可以响应的 Intent 类型。      |
| `<manifest>`               | AndroidManifest.xml 文件的根元素。                           |
| `<meta-data>`              | 可以提供给父级组件的其他任意数据项的名称-值对。              |
| `<path-permission>`        | 定义内容提供程序中特定数据子集的路径和所需权限。             |
| `<permission>`             | 声明安全权限，可用于限制对此应用或其他应用的特定组件或功能的访问。 |
| `<permission-group>`       | 为相关权限的逻辑分组声明名称。                               |
| `<permission-tree>`        | 声明权限树的基本名称。                                       |
| `<provider>`               | 声明内容提供程序组件。                                       |
| `<receiver>`               | 声明广播接收器组件。                                         |
| `<service>`                | 声明服务组件。                                               |
| `<supports-gl-texture>`    | 声明应用支持的一种 GL 纹理压缩格式。                         |
| `<supports-screens>`       | 声明应用支持的屏幕尺寸，并为大于此尺寸的屏幕启用屏幕兼容模式。 |
| `<uses-configuration>`     | 指明应用要求的特定输入功能。                                 |
| `<uses-feature>`           | 声明应用使用的单个硬件或软件功能。                           |
| `<uses-library>`           | 指定应用必须链接到的共享库。                                 |
| `<uses-permission>`        | 指定为使应用正常运行，用户必须授予的系统权限。               |
| `<uses-permission-sdk-23>` | 指明应用需要特定权限，但仅当应用在运行 Android 6.0（API 级别 23）或更高版本的设备上安装时才需要。 |
| `<uses-sdk>`               | 您可以通过整数形式的 API 级别，表示应用与一个或多个版本的 Android 平台的兼容性。 |

