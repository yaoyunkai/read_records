# Started for Android #

## 1. build first app ##

### 1.1 my first Android app ###

**Gradle files**

**app code**

**Layout files**

To view and edit a layout file, expand the `res` folder and the `layout` folder to see the layout file. 

**Resource files** : in `res` folder

- drawable
- layout
- mipmap
- values:
  - colors.xml
  - dimens.xml
  - strings.xml
  - styles.xml

**Android manifest**

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.helloworld">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
               <action android:name="android.intent.action.MAIN" />

               <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

1，attr: package 在app发布后不应该更改。

2，自动备份： `android:allowBackup="true"`

3，`<uses-sdk android:minSdkVersion="14" android:targetSdkVersion="19" />` uses-sdk表示的含义。

### 1.2 layouts & resources ###

#### Views ####

UI由一个称为视图的对象层次结构组成——屏幕上的每个元素都是一个View

View类表示所有UI组件的基本构建块，以及提供交互式UI组件(如按钮、复选框和文本输入字段)的类的基类。

- TextView
- EditText
- Button
- ScrollView RecyclerView
- ImageView
- ConstraintLayout LinearLayout

##### ViewGroup groups #####

Common items:

- ConstraintLayout
- SrollView
- RecyclerView

一些ViewGroup组被指定为布局，因为它们以特定的方式组织子View元素，通常用作根ViewGroup。一些布局的例子是:

- ConstraintLayout: 一组子视图元素，使用约束、边和指南来控制元素在布局中相对于其他元素的位置。ConstraintLayout的设计是为了方便在布局编辑器中单击和拖动View元素。
- LinearLayout: 一组水平或垂直定位和对齐的子View元素。
- RelativeLayout:一组子视图元素，其中每个元素相对于ViewGroup中的其他元素进行定位和对齐。换句话说，子View元素的位置可以相互描述，也可以与父ViewGroup相关联。
- TableLayout:一组按行和列排列的子视图元素。
- FrameLayout:一组在堆栈中的子视图元素。FrameLayout的设计是为了在屏幕上挡住一个区域来显示一个视图。子视图元素在一个堆栈中绘制，最近添加的子元素在顶部。FrameLayout的大小就是它最大的子视图元素的大小。
- GridLayout

#### The layout editor ####

**1, 使用ConstraintLayout**

约束是与另一个UI元素、父布局或不可见的指导方针的连接或对齐。每个约束显示为从一个循环句柄延伸出来的一行。在Component Tree窗格中选择一个UI元素或在布局编辑器中单击它后，该元素在每个角上显示一个调整大小的句柄，在每个边的中间显示一个圆形约束句柄。

![ The constraint and resizing handles on Views](.assets/as_layout_constraint_2_handles_annot.png)

约束和大小调整句柄：

1. **Resizing handle**.
2. **Constraint line and handle**. In the figure, the constraint aligns the left side of the **Toast** `Button` to the left side of the layout.
3. **Constraint handle** without a constraint line.
4. **Baseline handle**. The baseline handle aligns the text baseline of an element to the text baseline of another element.

-- 在设计窗口中调整或者在XML file中直接更改对应的属性。

-- using a baseline constraint

-- 使用属性窗口：

ConstraintLayout的 `layout_height`  `layout_width`有以下的属性：

- match_constraint
- warp_content
- specify a fixed size

#### Edting XML directly ####

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginLeft="8dp"
        android:layout_marginTop="8dp"
        android:layout_marginRight="8dp"
        android:layout_marginBottom="8dp"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

  </androidx.constraintlayout.widget.ConstraintLayout>
```

**XML的属性**

视图的属性定义了视图在屏幕上出现的位置、它的大小、视图与其他视图的关系以及它如何响应用户输入。在XML中或在布局编辑器的Attributes窗格中定义视图时，属性被称为属性。

属性通常采用以下形式:

`android:attribute_name="value"`

如果值是一种资源，比如一种颜色，@符号指定了哪种资源：

`android:background="@color/myBackgroundColor"`

**定义一个View**

要唯一地标识视图并从代码中引用它，必须给它一个id。android:id属性允许你指定一个唯一的id 一个视图的资源标识符。

`android:id="@+id/button_count"`

该属性的`@+id/button_count`部分为Button (View的子类)创建了一个名为`button_count`的id。您使用加号(+)符号表示您正在创建一个新id。

引用现有资源标识符:

`android:layout_toLeftOf="@id/show_count"`

**Positioning a View**

1, LinearLayout定位

- android:layout_width

- android:layout_height

- android:orientation
- android:layout_gravity

`android:layout_width`和`android:layout_height`属性可以采用以下三个值之一:

- match_parent
- wrap_content
- a fixed number of dp

The `android:orientation` can be:

- horizontal
- vertical

填充是UI元素的边缘和元素内容之间的空间，以密度无关的像素度量，

- `android:padding`: Sets the padding of all four edges.
- `android:paddingTop`: Sets the padding of the top edge.
- `android:paddingBottom`: Sets the padding of the bottom edge.
- `android:paddingLeft`: Sets the padding of the left edge.
- `android:paddingRight`: Sets the padding of the right edge.
- `android:paddingStart`: Sets the padding of the start of the view, in pixels. Used in place of the padding attributes listed above, especially with views that are long and narrow.
- `android:paddingEnd`: Sets the padding of the end edge of the view, in pixels. Used along with `android:paddingStart`.

2, RelativeLayout Positioning

另一个有用的布局视图组是RelativeLayout，你可以用它来相对地定位子视图元素或父视图元素。RelativeLayout可以使用的属性包括:

- `android:layout_toLeftOf`: Positions the right edge of this View to the left of another View (identified by its ID).
- `android:layout_toRightOf`: Positions the left edge of this View to the right of another View (identified by its ID).
- `android:layout_centerHorizontal`: Centers this View horizontally within its parent.
- `android:layout_centerVertical`: Centers this View vertically within its parent.
- `android:layout_alignParentTop`: Positions the top edge of this View to match the top edge of the parent.
- `android:layout_alignParentBottom`: Positions the bottom edge of this View to match the bottom edge of the parent.

**Style-related attributes**

您可以指定样式属性来定制视图的外观。一个没有样式属性的视图，如android:textColor, android:textSize，和android:background，采用应用程序的主题中定义的样式。

- `android:background`: Specifies a color or drawable resource to use as the background.
- `android:text`: Specifies text to display in the view.
- `android:textColor`: Specifies the text color.
- `android:textSize`: Specifies the text size.
- `android:textStyle`: Specifies the text style, such as `bold`.

#### Resource files ####

资源文件是一种将静态值从代码中分离出来的方法，这样您就不必通过更改代码本身来更改值。您可以将所有字符串、布局、尺寸、颜色、样式和菜单文本分别存储在资源文件中。

当查看Project > Android窗格时，资源文件存储在res文件夹中的文件夹中。这些文件夹包括:

- `drawable`: For images and icons
- `layout`: For layout resource files
- `menu`: For menu items
- `mipmap`: For pre-calculated, optimized collections of app icons used by the Launcher
- `values`: For colors, dimensions, strings, and styles (theme attributes)

在XML布局中引用资源的语法如下:

`@package_name:resource_type/resource_name`

- Package_name是资源所在的包的名称。当您引用存储在项目的res文件夹中的资源时，不需要包名，因为这些资源来自同一个包。
- resource_type是资源类型的R子类 See [Resource Types](https://developer.android.com/guide/topics/resources/available-resources.html)
- resource_name是没有扩展名的资源文件名，或者是XML元素中的android:name属性值。

下面列出demo:

`android:text="@string/button_label_toast"`

`android:background="@color/colorPrimary"`

`android:textColor="@android:color/white"`

#### View clicks ####

- Write a Java method that performs the specific action you want the app to do when this event occurs. This method is typically referred to as an *event handler*.
- Associate this event-handler method to the `View`, so that the method executes when the event occurs.

```xml
<Button
    android:id="@+id/button_toast"
    android:onClick="showToast"
```

