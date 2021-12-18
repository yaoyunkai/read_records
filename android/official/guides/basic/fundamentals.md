# 应用基础知识 #

一个 APK 文件包含 Android 应用的所有内容，它也是 Android 设备用来安装应用的文件。

每个 Android 应用都处于各自的安全沙盒中，并受以下 Android 安全功能的保护：

- Android 操作系统是一种多用户 Linux 系统，其中的每个应用都是一个不同的用户；
- 默认情况下，系统会为每个应用分配一个唯一的 Linux 用户 ID（该 ID 仅由系统使用，应用并不知晓）。系统会为应用中的所有文件设置权限，使得只有分配给该应用的用户 ID 才能访问这些文件；
- 每个进程都拥有自己的虚拟机 (VM)，因此应用代码独立于其他应用而运行。
- 默认情况下，每个应用都在其自己的 Linux 进程内运行。Android 系统会在需要执行任何应用组件时启动该进程，然后当不再需要该进程或系统必须为其他应用恢复内存时，其便会关闭该进程。

Android 系统实现了*最小权限原则*。换言之，默认情况下，每个应用只能访问执行其工作所需的组件，而不能访问其他组件。应用仍可通过一些途径与其他应用共享数据以及访问系统服务：

- 可以安排两个应用共享同一 Linux 用户 ID，在此情况下，二者便能访问彼此的文件。为节省系统资源，也可安排拥有相同用户 ID 的应用在同一 Linux 进程中运行，并共享同一 VM。应用还必须使用相同的证书进行签名。
- 应用可以请求访问设备数据（如用户的联系人、短信消息、可装载存储装置（SD 卡）、相机、蓝牙等）的权限。用户必须明确授予这些权限。如需了解详细信息，请参阅[使用系统权限](https://developer.android.google.cn/training/permissions)。

## 应用组件 ##

应用组件是 Android 应用的基本构建块。每个组件都是一个入口点，系统或用户可通过该入口点进入您的应用。有些组件会依赖于其他组件。

共有四种不同的应用组件类型：

- [Activity](https://developer.android.google.cn/reference/android/app/Activity)
- [Service](https://developer.android.google.cn/reference/android/app/Service)
- [BroadcastReceiver](https://developer.android.google.cn/reference/android/content/BroadcastReceiver)
- [ContentProvider](https://developer.android.google.cn/reference/android/content/ContentProvider)

每种类型都有不同的用途和生命周期，后者会定义如何创建和销毁组件。

**Activity**

Activity 是与用户交互的入口点。它表示拥有界面的单个屏幕。Activity 有助于完成系统和应用程序之间的以下重要交互：

- 追踪用户当前关心的内容（屏幕上显示的内容），以确保系统继续运行托管 Activity 的进程。
- 了解先前使用的进程包含用户可能返回的内容（已停止的 Activity），从而更优先保留这些进程。
- 帮助应用处理终止其进程的情况，以便用户可以返回已恢复其先前状态的 Activity。
- 提供一种途径，让应用实现彼此之间的用户流，并让系统协调这些用户流。（此处最经典的示例是共享。）

请参阅 [Activity](https://developer.android.google.cn/guide/components/activities) 开发者指南。

**Service**

服务是一个通用入口点，用于因各种原因使应用在后台保持运行状态。

如需了解有关 [Service](https://developer.android.google.cn/reference/android/app/Service) 类的更多信息，请参阅[服务](https://developer.android.google.cn/guide/components/services)开发者指南。

>如果您的应用面向 Android 5.0（API 级别 21）或更高版本，请使用 `JobScheduler` 类来调度操作。JobScheduler 的优势在于，它能通过优化作业调度来降低功耗，以及使用 [Doze](https://developer.android.google.cn/training/monitoring-device-state/doze-standby) API，从而达到省电目的。如需了解有关使用此类的更多信息，请参阅 [`JobScheduler`](https://developer.android.google.cn/reference/android/app/job/JobScheduler) 参考文档。

**BroadcastReceiver**

借助广播接收器组件，系统能够在常规用户流之外向应用传递事件，从而允许应用响应系统范围内的广播通知。

广播接收器不会显示界面，但其可以[创建状态栏通知](https://developer.android.google.cn/guide/topics/ui/notifiers/notifications)，在发生广播事件时提醒用户。

**ContentProvider**

内容提供程序管理一组共享的应用数据，您可以将这些数据存储在文件系统、SQLite 数据库、网络中或者您的应用可访问的任何其他持久化存储位置。

内容提供程序作为 `ContentProvider` 的子类实现，并且其必须实现一组标准 API，以便其他应用能够执行事务。如需了解详细信息，请参阅[内容提供程序](https://developer.android.google.cn/guide/topics/providers/content-providers)开发者指南。

### 启动组件 ###

在四种组件类型中，有三种（Activity、服务和广播接收器）均通过异步消息 *Intent* 进行启动。Intent 会在运行时对各个组件进行互相绑定。您可以将 Intent 视为从其他组件（无论该组件是属于您的应用还是其他应用）请求操作的信使。

使用 `Intent` 对象创建 Intent，该对象通过定义消息来启动特定组件（显式 Intent）或特定的组件*类型*（隐式 Intent）。

ContentProvider并非由 Intent 启动。相反，它们会在成为 `ContentResolver` 的请求目标时启动。

每种组件都有不同的启动方法：

- 启动 Activity，您可以向 `startActivity()` 或 `startActivityForResult()` 传递 `Intent`（当您想让 Activity 返回结果时），或者为其安排新任务。
- 在 Android 5.0（API 级别 21）及更高版本中，您可以使用 `JobScheduler` 类来调度操作。对于早期 Android 版本，您可以通过向 `startService()` 传递 `Intent` 来启动服务（或对执行中的服务下达新指令）。您也可通过向将 `bindService()` 传递 `Intent` 来绑定到该服务。
- 您可以通过向 `sendBroadcast()`、`sendOrderedBroadcast()` 或 `sendStickyBroadcast()` 等方法传递 `Intent` 来发起广播。
- 您可以通过在 `ContentResolver` 上调用 `query()`，对内容提供程序执行查询。

如需了解有关 Intent 用法的详细信息，请参阅 [Intent 和 Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters)文档。

## 清单文件 ##

在 Android 系统启动应用组件之前，系统必须通过读取应用的*清单*文件 (`AndroidManifest.xml`) 确认组件存在。您的应用必须在此文件中声明其所有组件，该文件必须位于应用项目目录的根目录中。

## 其他资源 ##

- [Intent 和 Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters): 如何使用 `Intent` API 来启动应用组件（如 Activity 和服务），以及如何使您的应用组件可供其他应用使用。

- [Activity](https://developer.android.google.cn/guide/components/activities)如何创建 `Activity` 类的实例，该类可在您的应用内提供具有界面的独立屏幕。

- [提供资源](https://developer.android.google.cn/guide/topics/resources/providing-resources)如何通过构建 Android 应用将应用资源与应用代码分离，包括如何针对特定设备配置提供备用资源。

- [设备兼容性](https://developer.android.google.cn/guide/practices/compatibility)Android 如何在不同类型的设备上运行，并介绍如何针对不同设备优化应用，或如何限制应用在不同设备上的可用性。

- [系统权限](https://developer.android.google.cn/guide/topics/permissions)Android 如何通过权限系统来限制应用访问某些 API，该系统要求应用必须先征得用户同意，才能使用这些 API。


