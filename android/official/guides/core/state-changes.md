# 处理 Activity 状态更改 #

用户触发和系统触发的不同事件会导致 `Activity` 从一个状态转换到另一个状态。本文档介绍了发生此类转换的一些常见情况，以及如何处理这些转换。

有关 Activity 状态的详情，请参阅[了解 Activity 生命周期](https://developer.android.google.cn/guide/components/activities/activity-lifecycle)。要了解如何借助 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel) 类来管理 Activity 生命周期，请参阅 [了解 ViewModel 类](https://developer.android.google.cn/topic/libraries/architecture/viewmodel)。

## 配置发生了更改 ##

有很多事件会触发配置更改。最显著的例子或许是横屏和竖屏之间的屏幕方向变化。

当配置发生更改时，Activity 会被销毁并重新创建。原始 Activity 实例将触发 `onPause()`、`onStop()` 和 `onDestroy()` 回调。系统将创建新的 Activity 实例，并触发 `onCreate()`、`onStart()` 和 `onResume()` 回调。

## Activity或对话框显示在前台 ##

如果有新的 Activity 或对话框出现在前台，并且局部覆盖了正在进行的 Activity，则被覆盖的 Activity 会失去焦点并进入“已暂停”状态。然后，系统会调用 `onPause()`。

当被覆盖的 Activity 返回到前台并重新获得焦点时，会调用 `onResume()`。

如果有新的 Activity 或对话框出现在前台，夺取了焦点且完全覆盖了正在进行的 Activity，则被覆盖的 Activity 会失去焦点并进入“已停止”状态。然后，系统会快速地接连调用 `onPause()` 和 `onStop()`。

当被覆盖的 Activity 的同一实例返回到前台时，系统会对该 Activity 调用 `onRestart()`、`onStart()` 和 `onResume()`。如果被覆盖的 Activity 的新实例进入后台，则系统不会调用 onRestart()，而只会调用 `onStart()` 和 `onResume()`。

## 用户点按“返回”按钮 ##

如果 Activity 位于前台，并且用户点按了**返回**按钮，Activity 将依次经历 `onPause()`、`onStop()` 和 `onDestroy()` 回调。活动不仅会被销毁，还会从返回堆栈中移除。

需要注意的是，在这种情况下，默认不会触发 `onSaveInstanceState()` 回调。此行为基于的假设是，用户点按**返回**按钮时不期望返回 Activity 的同一实例。不过，您可以通过替换 `onBackPressed()` 方法实现某种自定义行为，例如“confirm-quit”对话框。

## 系统终止应用进程 ##

如果某个应用处于后台并且系统需要为前台应用释放额外的内存，则系统可能会终止后台应用以释放更多内存。要详细了解系统如何确定要销毁哪些进程，请阅读 [Activity 状态和从内存中弹出](https://developer.android.google.cn/guide/components/activities/activity-lifecycle#asem)以及[进程和应用生命周期](https://developer.android.google.cn/guide/components/activities/process-lifecycle)。

要了解如何在系统终止您的应用进程时保存 Activity 界面状态，请参阅[保存和恢复 Activity 状态](https://developer.android.google.cn/guide/components/activities/activity-lifecycle#saras)。

