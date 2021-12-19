# Fragment #

[`Fragment`](https://developer.android.google.cn/reference/androidx/fragment/app/Fragment) 表示应用界面中可重复使用的一部分。Fragment 定义和管理自己的布局，具有自己的生命周期，并且可以处理自己的输入事件。Fragment 不能独立存在，而是必须由 Activity 或另一个 Fragment 托管。Fragment 的视图层次结构会成为宿主的视图层次结构的一部分，或附加到宿主的视图层次结构。

## 模块化 ##

Fragment 允许您将界面划分为离散的区块，从而将模块化和可重用性引入 Activity 的界面。Activity 是围绕应用的界面放置全局元素（如抽屉式导航栏）的理想位置。相反，Fragment 更适合定义和管理单个屏幕或部分屏幕的界面。

![同一屏幕的采用不同屏幕尺寸的两个版本。](.assets/fragment-screen-sizes.png)

将界面划分为 Fragment 可让您更轻松地在运行时修改 Activity 的外观。当 Activity 处于 `STARTED` [生命周期状态](https://developer.android.google.cn/guide/components/activities/activity-lifecycle)或更高的状态时，可以添加、替换或移除 Fragment。您可以将这些更改的记录保留在由 Activity 管理的返回堆栈中，从而允许撤消这些更改。

您可以在同一 Activity 或多个 Activity 中使用同一 Fragment 类的多个实例，甚至可以将其用作另一个 Fragment 的子级。考虑到这一点，您应只为 Fragment 提供管理它自己的界面所需的逻辑。您应避免让一个 Fragment 依赖于另一个 Fragment 或从一个 Fragment 操控另一个 Fragment。

## Next ##

### 开始使用 ###

[创建Fragment](./fragments-create.md)

### 更深入的主题 ###

