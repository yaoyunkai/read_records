# Activity 简介 #

`Activity` 类是 Android 应用的关键组件，而 Activity 的启动和组合方式则是该平台应用模型的基本组成部分。

在编程范式中，应用是通过 `main()` 方法启动的，而 Android 系统与此不同，它会调用与其生命周期特定阶段相对应的特定回调方法来启动 `Activity` 实例中的代码。

要详细了解有关设计应用架构的最佳做法，请参阅[应用架构指南](https://developer.android.google.cn/topic/libraries/architecture/guide)。

## Acitvity的概念 ##

## 配置清单 ##

要使应用能够使用 Activity，您必须在清单中声明 Activity 及其特定属性。

### 声明Activity ###

```xml
<manifest ... >
    <application ... >
        <activity android:name=".ExampleActivity" />
        ...
    </application ... >
    ...
</manifest >
```

> 发布应用后，就不应再更改 Activity 名称，否则可能会破坏某些功能，例如应用快捷方式。

### 声明intent过滤器 ###

[Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters)是 Android 平台的一项非常强大的功能。

```xml
<activity android:name=".ExampleActivity" android:icon="@drawable/app_icon">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
</activity>
```

在此示例中，`<action>` 元素指定该 Activity 会发送数据。将 `<category>` 元素声明为 DEFAULT 可使 Activity 能够接收启动请求。`<data>` 元素指定此 Activity 可以发送的数据类型。

以下代码段展示了如何调用上述 Activity：

```java
// Create the text message with a string
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.setType("text/plain");
sendIntent.putExtra(Intent.EXTRA_TEXT, textMessage);
// Start the activity
startActivity(sendIntent);
```

### 声明权限 ###

例如，假设您的应用想要使用一个名为 SocialApp 的应用在社交媒体上分享文章，则 SocialApp 本身必须定义调用它的应用所需具备的权限：

```xml
<manifest>
    <activity android:name="...."
              android:permission=”com.google.socialapp.permission.SHARE_POST”

              />
```

然后，为了能够调用 SocialApp，您的应用必须匹配 SocialApp 清单中设置的权限：

```xml
<manifest>
    <uses-permission android:name="com.google.socialapp.permission.SHARE_POST" />
</manifest>
```

## 管理Activity生命周期 ##

[Activity 生命周期](./activity-lifecycle.md)

