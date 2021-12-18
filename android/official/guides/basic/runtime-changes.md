# 处理配置变更 #

某些设备配置可能会在运行时发生变化.

发生这种变化时，Android 会重启正在运行的 [`Activity`](https://developer.android.google.cn/reference/android/app/Activity)（先后调用 [`onDestroy()`](https://developer.android.google.cn/reference/android/app/Activity#ondestroy) 和 [`onCreate()`](https://developer.android.google.cn/reference/android/app/Activity#onCreate(android.os.Bundle))）。重启行为旨在通过利用与新设备配置相匹配的备用资源来自动重新加载您的应用，从而帮助它适应新配置。

如要测试应用能否在保持完好状态的情况下自行重启，您应在执行应用内的各类任务时主动更改配置（例如，改变屏幕方向）。您的应用应能够在不丢失用户数据或状态的情况下随时重启，以便处理如下事件：配置发生变化，或者用户收到来电并在应用进程被销毁很久之后返回应用。

然而，您可能会遇到这种情况：重启应用并恢复大量数据不仅成本高昂，而且会造成糟糕的用户体验。在此情况下，您还有两个选择：

1. 在配置变更期间保留对象
1. 自行处理配置变更

## 在配置变更期间保留对象 ##

在此情况下，您可通过使用 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel) 对象来减轻重新初始化 Activity 的负担。系统会在配置变更时保留 ViewModel，使其成为保存界面数据的理想场所，让您无需再次查询这些数据。如需详细了解如何在应用中使用 ViewModel，请阅读 [ViewModel 指南](https://developer.android.google.cn/topic/libraries/architecture/viewmodel)。

## 自行处理配置变更 ##

如果应用在特定配置变更期间无需更新资源，*并且*因性能限制您需要尽量避免 Activity 重启，则可声明 Activity 自行处理配置变更，从而阻止系统重启 Activity。

如要声明由 Activity 处理配置变更，请在清单文件中编辑相应的 `<activity>` 元素，以包含 `android:configChanges` 属性，该属性的值表示要处理的配置。

```xml
<activity android:name=".MyActivity"
          android:configChanges="orientation|keyboardHidden"
          android:label="@string/app_name">
```

现在，即便其中某个配置发生变化，MyActivity 也不会重启。但 MyActivity 会接收到对 `onConfigurationChanged()` 的调用消息。此方法会收到传递的 Configuration 对象，从而指定新设备配置。您可以通过读取 Configuration 中的字段确定新配置，然后通过更新界面所用资源进行适当的更改。调用此方法时，Activity 的 Resources 对象会相应地进行更新，并根据新配置返回资源，以便您在系统不重启 Activity 的情况下轻松重置界面元素。

```java
@Override
public void onConfigurationChanged(Configuration newConfig) {
    super.onConfigurationChanged(newConfig);

    // Checks the orientation of the screen
    if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
        Toast.makeText(this, "landscape", Toast.LENGTH_SHORT).show();
    } else if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT){
        Toast.makeText(this, "portrait", Toast.LENGTH_SHORT).show();
    }
}
```

[`Configuration`](https://developer.android.google.cn/reference/android/content/res/Configuration) 对象代表所有当前配置，而不仅仅是已变更的配置。

