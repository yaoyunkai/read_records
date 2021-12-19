# Parcelable 和 Bundle #

`Parcelable` 和 `Bundle` 对象可跨进程边界使用，例如与 IPC/Binder 事务之间，带有 intent 的 Activity 之间等，还可以用来存储跨配置更改的瞬时状态。

## 在 Activity 之间发送数据 ##

```java
Intent intent = new Intent(this, MyActivity.class);
intent.putExtra("media_id", "a1b2c3");
// ...
startActivity(intent);
```

操作系统会将 intent 的基础 `Bundle` 打包。然后，操作系统会创建新的 Activity，将数据拆包，并将 intent 传递给新的 Activity。

我们建议您使用 `Bundle` 类为 `Intent` 对象设置操作系统已知的基元。`Bundle` 类针对使用 parcel 进行编组和解组进行了高度优化。

## 在进程之间发送数据 ##

在进程之间发送数据与在 Activity 之间发送数据类似。不过，在进程之间发送时，我们建议您不要使用自定义 Parcelable。如果您将一个自定义 `Parcelable` 对象从一个应用发送到另一个应用，则需要确保发送和接收的应用上都存在版本完全相同的自定义类。通常情况下，这可能是在两个应用中都会使用的通用库。如果您的应用尝试向系统发送自定义 Parblelable，则可能会发生错误，因为系统无法对其不了解的类进行解组。

