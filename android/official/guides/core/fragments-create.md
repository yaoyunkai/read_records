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

Fragment库还提供了更专门化的Fragment基类:

[`DialogFragment`](https://developer.android.google.cn/reference/androidx/fragment/app/DialogFragment)

[`PreferenceFragmentCompat`](https://developer.android.google.cn/reference/androidx/preference/PreferenceFragmentCompat)

## Add a fragment to an activity ##

通常，你的片段必须嵌入在一个AndroidX FragmentActivity贡献一部分UI到该活动的布局。

FragmentActivity是appcompactactivity的基类，所以如果你已经子类化了appcompactactivity以在你的应用程序中提供向后兼容，那么你不需要改变你的activity基类。

你可以通过在你的activity的布局文件中定义片段或通过在你的activity的布局文件中定义一个fragment container，然后以编程方式从你的活动中添加fragment，将你的片段添加到活动的视图层次结构中。

 In either case, you need to add a [`FragmentContainerView`](https://developer.android.google.cn/reference/androidx/fragment/app/FragmentContainerView) that defines the location where the fragment should be placed within the activity's view hierarchy. It is strongly recommended to always use a `FragmentContainerView` as the container for fragments, as `FragmentContainerView` includes fixes specific to fragments that other view groups such as `FrameLayout` do not provide.

### add a fragment via XML ###

To declaratively add a fragment to your activity layout's XML, use a `FragmentContainerView` element.

```xml
<!-- res/layout/example_activity.xml -->
<androidx.fragment.app.FragmentContainerView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/fragment_container_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:name="com.example.ExampleFragment" />
```

The `android:name` attribute specifies the class name of the `Fragment` to instantiate. When the activity's layout is inflated, the specified fragment is instantiated, [`onInflate()`](https://developer.android.google.cn/reference/androidx/fragment/app/Fragment#onInflate(android.content.Context,%20android.util.AttributeSet,%20android.os.Bundle)) is called on the newly instantiated fragment, and a `FragmentTransaction` is created to add the fragment to the `FragmentManager`.

- android:name 指定要初始化的Fragment class

### add a fragment programmatically ###

要编程地添加一个片段到你的activity的布局，布局应该包括一个FragmentContainerView作为一个片段容器，如下所示:

```xml
<!-- res/layout/example_activity.xml -->
<androidx.fragment.app.FragmentContainerView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/fragment_container_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

不像XML的方法，android:name属性在FragmentContainerView这里没有使用，所以没有特定的片段被自动实例化。相反，一个FragmentTransaction被用来实例化一个片段，并将其添加到Activity的布局中。

当您的activity正在运行时，您可以进行片段事务，例如添加、删除或替换片段。在你的FragmentActivity，你可以得到一个FragmentManager的实例，它可以用来创建一个FragmentTransaction。然后，你可以在activity的onCreate()方法中使用FragmentTransaction.add()实例化你的片段，在你的布局中传递容器的ViewGroup ID和你想要添加的片段类，然后提交事务，如下所示:

```java
public class ExampleActivity extends AppCompatActivity {
    public ExampleActivity() {
        super(R.layout.example_activity);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState == null) {
            getSupportFragmentManager().beginTransaction()
                .setReorderingAllowed(true)
                .add(R.id.fragment_container_view, ExampleFragment.class, null)
                .commit();
        }
    }
}
```

在前面的例子中，注意片段事务只在savedInstanceState为空时创建。这是为了确保片段只添加一次，当activity第一次创建时。当配置发生变化并重新创建活动时，savedInstanceState不再为空，并且片段不需要第二次添加，因为片段会自动从savedInstanceState恢复。

如果你的片段需要一些初始数据，参数可以通过在调用FragmentTransaction.add()中提供一个Bundle传递给你的片段，如下所示:

```java
public class ExampleActivity extends AppCompatActivity {
    public ExampleActivity() {
        super(R.layout.example_activity);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState == null) {
            Bundle bundle = new Bundle();
            bundle.putInt("some_int", 0);

            getSupportFragmentManager().beginTransaction()
                .setReorderingAllowed(true)
                .add(R.id.fragment_container_view, ExampleFragment.class, bundle)
                .commit();
        }
    }
}
```

```java
class ExampleFragment extends Fragment {
    public ExampleFragment() {
        super(R.layout.example_fragment);
    }

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        int someInt = requireArguments().getInt("some_int");
        ...
    }
}
```

