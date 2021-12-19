# Create a Fragment #

片段表示活动中用户界面的模块部分。片段有自己的生命周期，接收自己的输入事件，并且您可以在包含的活动运行时添加或删除片段。

## Setup your environment ##

Fragments require a dependency on the [AndroidX Fragment library](https://developer.android.google.cn/jetpack/androidx/releases/fragment). You need to add the [Google Maven repository](https://developer.android.google.cn/studio/build/dependencies#google-maven) to your project's `build.gradle` file in order to include this dependency.

```groovy
buildscript {
    ...

    repositories {
        google()
        ...
    }
}

allprojects {
    repositories {
        google()
        ...
    }
}
```

To include the AndroidX Fragment library to your project, add the following dependencies in your app's `build.gradle` file:

```groovy
dependencies {
    def fragment_version = "1.4.0"

    // Java language implementation
    implementation "androidx.fragment:fragment:$fragment_version"
    // Kotlin
    implementation "androidx.fragment:fragment-ktx:$fragment_version"
}
```

## Create a fragment class ##

要创建一个片段，扩展AndroidX fragment类，并覆盖其方法来插入您的应用程序逻辑，类似于创建一个Activity类。为了创建一个定义自己布局的最小片段，提供你的片段的布局资源给基构造函数，如下面的例子所示:

```java
class ExampleFragment extends Fragment {
    public ExampleFragment() {
        super(R.layout.example_fragment);
    }
}
```

