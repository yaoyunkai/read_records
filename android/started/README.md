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

### 1.3 Text and scrolling views ###

本章描述应用程序中最常用的View子类之一:TextView，它在屏幕上显示文本内容。TextView可以用来显示一条消息，一个来自数据库的响应，甚至是整个杂志风格的文章，用户可以滚动。本章还展示了如何创建文本和其他元素的滚动视图。

#### TextView ####

您可以通过使用它的资源id在您的Java代码中引用一个TextView，以便从您的代码中更新文本或其属性。如果你想让用户编辑文本，使用EditText，一个允许文本输入和编辑的TextView的子类。你学习关于EditText在另一课。

**TextView的attributes**

您可以使用TextView的XML属性来控制：

- TextView在布局中的位置(像任何其他视图一样)
- TextView本身如何显示，比如使用背景颜色
- 文本在TextView中是什么样子的，比如初始文本及其样式、大小和颜色

最常用的属性与TextView是以下:

- `android:text`
- `android:textColor` 设置文本的颜色。您可以将该属性设置为颜色值、预定义资源或主题。颜色资源和主题将在其他章节中描述。
- `android:textAppearance` 文本的外观，包括颜色、字体、样式和大小。将此属性设置为预定义的样式资源或主题，这些资源或主题已经定义了这些值。
- `android:textSize` 设置文本大小,Use `sp` (scaled-pixel) sizes such as `20sp` or `14.5sp`, or set the attribute to a predefined resource or theme.
- `android:textStyle` Use `normal`, `bold`, `italic`, or `bold`|`italic`.
- `android:typeface` Use `normal`, `sans`, `serif`, or `monospace`.
- `android:lineSpacingExtra` 在文本行之间设置额外的间距。使用sp(缩放像素)或dp(设备无关像素)大小，或将属性设置为预定义的资源或主题。
- `android:autoLink` 控制url和电子邮件地址等链接是否自动找到并转换为可点击(可触摸)链接。
  - none
  - web
  - email
  - phone
  - map
  - all

**在文本中使用嵌入标签 Using embedded tags in text**

在这两种情况下，文本都可能包含嵌入的HTML标记或其他文本格式化代码。为了在文本视图中正确显示，文本必须按照以下规则进行格式化:

- 输入\n表示行尾，输入另一个\n表示空行。您需要添加行尾字符，以防止段落相互冲突。
- 如果你的文本中有撇号(')，你必须在它前面加一个反斜杠(\')来转义它。如果文本中有双引号，也必须转义它(\")。
- Enter the HTML and **</b>** tags around words that should be in bold.
- Enter the HTML and **</i>** tags around words that should be in italics.

**在代码中引用TextView**

1. You use the [`findViewById()`](https://developer.android.com/reference/android/view/View.html#findViewById(int)) method of the `View` class, and refer to the view you want to find using this format
2. After retrieving the `View` as a `TextView` member variable, you can then set the text to new text (in this case, `mCount_text`) using the [`setText()`](https://developer.android.com/reference/android/widget/TextView.html#setText(java.lang.CharSequence)) method of the `TextView` class

#### Scrolling views ####

The [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView.html) class provides the layout for a vertical scrolling view. (For horizontal scrolling, you would use [`HorizontalScrollView`](https://developer.android.com/reference/android/widget/HorizontalScrollView.html).) `ScrollView` is a subclass of [`FrameLayout`](https://developer.android.com/reference/android/widget/FrameLayout.html), which means that you can place only *one* `View` as a child within it; that child contains the entire contents to scroll.

即使你只能在一个ScrollView中放置一个子视图，子视图也可以是一个ViewGroup，它具有子视图元素的层次结构，比如LinearLayout。对于ScrollView中的视图来说，一个很好的选择是LinearLayout，它是按照垂直方向排列的。

**性能**

ScrollView的所有内容(例如带有View元素的ViewGroup)占用内存和视图层次结构，即使部分内容没有显示在屏幕上。

Consider using flatter layouts such as [`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout.html) or [`GridLayout`](https://developer.android.com/reference/android/widget/GridLayout.html) to improve performance.

To display long lists of items, or images, consider using a [`RecyclerView`](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html), which is covered in another lesson.

*RelativeLayout* *GridLayout* *RecyclerView*

**ScrollView with a TextView**

要在屏幕上显示可滚动的杂志文章，您可以使用RelativeLayout，其中包括用于文章标题的单独TextView、用于文章副标题的另一个TextView和用于滚动文章文本的第三个TextView(见下图)，这些都是在ScrollView中设置的。屏幕上唯一可以滚动的部分是带有文章文本的ScrollView。

![ The layout with a ScrollView](.assets/dg_layout_diagram1.png)

**ScrollView with a LinearLayout**

一个ScrollView只能包含一个子视图;然而，这个视图可以是一个ViewGroup，它包含几个视图元素，比如LinearLayout。你可以在ScrollView中嵌套一个ViewGroup，比如LinearLayout，从而滚动LinearLayout中的所有内容。

![ A LinearLayout Inside the ScrollView](.assets/dg_layout_diagram2.png)

对于LinearLayout：

- android:layout_width : match_parent
- android:layout_height: wrap_content

因为ScrollView只支持垂直滚动 你必须设置LinearLayout orientation属性为 vertical

## 2. Activities & intents ##

### 2.1 Activities and intents ###

#### About activities ####

acivity代表应用程序中带有用户可以交互的界面的单个屏幕.

通常，应用程序中的一个activity被指定为“主”活动，例如MainActivity。用户在第一次启动应用程序时看到主活动。每个活动可以启动其他活动来执行不同的操作。

每当一个新的活动启动时，前一个活动就会停止，但系统会将该活动保留在一个堆栈中(“back stack”)。当用户完成当前活动并按下Back按钮时，该活动将从堆栈中弹出并销毁，前一个活动将继续。

当一个活动因为一个新的活动开始而停止时，第一个活动通过活动生命周期回调方法被通知。

#### 创建activity ####

**Create the Activity**

the [`AppCompatActivity`](https://developer.android.com/reference/android/support/v7/app/AppCompatActivity.html) class类可以让你使用最新的Android应用功能，比如应用栏和材质设计，同时还可以让你的应用与运行旧版本Android的设备兼容。

```java
public class MainActivity extends AppCompatActivity {
   @Override
   protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       setContentView(R.layout.activity_main);
   }
}
```

了解activity的lifecycle

**Declare the Activity in AndroidManifest.xml**

Each `Activity` in your app must be declared in the `AndroidManifest.xml` file

The <activity> element includes a number of attributes to define properties of the Activity such as its label, icon, or theme. The only required attribute is android:name, which specifies the class name for the Activity (such as MainActivity). 

The <activity> element can also include declarations for Intent filters. The Intent filters specify the kind of Intent your Activity will accept.

`Intent` filters must include at least one `<action>` element, and can also include a `<category>` and optional `<data>`.

#### intent介绍 ####

Each activity is started or activated with an [`Intent`](https://developer.android.com/reference/android/content/Intent.html), which is a message object that makes a request to the Android runtime to start an activity or other app component in your app or in some other app.

当你的应用程序第一次从设备主屏幕启动时，Android运行时发送一个Intent给你的应用程序来启动你的应用程序的主活动(在AndroidManifest.xml文件中用main动作和LAUNCHER类别定义的那个)。要在你的应用程序中启动另一个活动，或者请求设备上其他可用的活动执行一个动作，你构建自己的意图并调用startActivity()方法来发送意图。

除了启动一个活动，意图还可以用于在一个活动和另一个活动之间传递数据。当您创建一个意图来启动一个新活动时，您可以包含关于您希望新活动操作的数据的信息。例如，一个显示消息列表的email Activity可以向显示该消息的Activity发送一个Intent。显示活动需要关于要显示的消息的数据，您可以在意图中包含该数据。

**intent types**

- 显式意图:使用活动的完全限定类名指定接收活动(或其他组件)。您可以使用显式意图在自己的应用程序中启动组件(例如，在UI中在屏幕之间移动)，因为您已经知道该组件的包和类名。
- 隐式意图:你不指定一个特定的活动或其他组件来接收意图。相反，您声明一个通用的操作来执行，Android系统将您的请求匹配到一个活动或其他可以处理请求的操作的组件。您将在另一个实践中了解更多关于使用隐式意图的内容。

**Intent objects and fields**

对于一个显式意图，关键字段包括以下内容:

- Activity类(针对显式Intent)。这是应该接收Intent的Activity或其他组件的类名;使用Intent构造函数或setComponent()、setComponentName()或setClassName()方法来指定类。
- Intent data。Intent数据字段包含了你想要接收Activity作为Uri对象操作的数据的引用
- intent extras. 这些键值对携带接收activity完成请求操作所需的信息。
- intent flgas. These are additional bits of metadata, defined by the `Intent` class.这些标志可能会指示Android系统如何启动一个Activity或者在Activity启动后如何处理它。

#### Starting an Activity with an explicit Intent ####

```java
Intent messageIntent = new Intent(this, ShowMessageActivity.class);
startActivity(messageIntent);
```

The intent constructor takes two arguments for an explicit `Intent`:

- An application context. In this example, the `Activity` class provides the context (`this`).
- The specific component to start (`ShowMessageActivity.class`).

已启动的活动保持在屏幕上，直到用户点击设备上的后退按钮，此时该活动关闭并被系统回收，而原来的活动恢复。

 You can also manually close the started `Activity` in response to a user action (such as a `Button` click) with the [`finish()`](https://developer.android.com/reference/android/app/Activity.html#finish()) method:

```java
public void closeActivity (View view) {
    finish();
}
```

#### Passing data from one Activity to another ####

除了简单地从另一个活动启动一个活动之外，你还可以使用Intent将信息从一个活动传递到另一个活动。你用来启动一个Activity的Intent对象可以包含Intent数据(一个要操作的对象的URI)，或者Intent额外数据，这些都是Activity可能需要的额外数据。

In the first (sending) `Activity`, you:

1. Create the `Intent` object.
2. Put data or extras into that `Intent`.
3. Start the new `Activity` with `startActivity()`.

In the second (receiving) `Activity`, you:

1. Get the `Intent` object the `Activity` was started with.
2. Retrieve the data or extras from the `Intent` object.

**When to use Intent data or Intent extras**

数据和额外数据之间有几个关键的区别，这些区别决定了您应该使用哪一个。

intent data 只能保存一条信息:表示要操作的数据位置的URI。

- 当您只有一条信息需要发送到已启动的活动。
- 当该信息是可以用URI表示的数据位置时。

intent extra: 您想要传递给已启动的活动的任何其他任意数据。`Intent` extras are stored in a [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html) object as key and value pairs.value can be any primitive or object type (objects must implement the [`Parcelable`](https://developer.android.com/reference/android/os/Parcelable.html) interface).  putExtra & putExtras

- 如果您想要传递多个信息到已启动的活动。
- 如果您想传递的任何信息不能通过URI表示。

**Add data to the Intent**

*<u>setData</u>*

```java
Intent messageIntent = new Intent(this, ShowMessageActivity.class);

// A web page URL
messageIntent.setData(Uri.parse("http://www.google.com")); 
// a Sample file URI
messageIntent.setData(Uri.fromFile(new File("/sdcard/sample.jpg")));
// A sample content: URI for your app's data model
messageIntent.setData(Uri.parse("content://mysample.provider/data")); 
// Custom URI 
messageIntent.setData(Uri.parse("custom:" + dataID + buttonId));
```

**Add extras to the Intent**

从原始activity中向显式的Intent添加额外的Intent:

- 确定要用于将信息放入额外组件的键，或者定义自己的键。每条信息都需要它自己唯一的密钥。
- 使用putExtra()方法将你的键/值对添加到Intent附加项中。你可以选择创建一个Bundle对象，将你的数据添加到Bundle中，然后将Bundle添加到Intent中。

Intent类包含了你可以使用的额外键，它们被定义为以单词EXTRA_开头的常量。

你也可以定义你自己的Intent额外的键。按照惯例，你将Intent额外键定义为以EXTRA_开头的静态变量。为了保证键是唯一的，键本身的字符串值应该以应用程序的完全限定类名作为前缀。

```java
public final static String EXTRA_POSITION_X = "com.example.mysampleapp.X";
public final static String EXTRA_POSITION_Y = "com.example.mysampleapp.Y";

// first way
messageIntent.putExtra(EXTRA_MESSAGE, "this is my message");
messageIntent.putExtra(EXTRA_POSITION_X, 100);
messageIntent.putExtra(EXTRA_POSITION_Y, 500);

// second way
Bundle extras = new Bundle();
extras.putString(EXTRA_MESSAGE, "this is my message");
extras.putInt(EXTRA_POSITION_X, 100);
extras.putInt(EXTRA_POSITION_Y, 500);
messageIntent.putExtras(extras);
```

**Retrieve the data from the Intent in the started Activity**

当你用Intent启动一个Activity时，启动的Activity可以访问Intent和它包含的数据。

要获取Activity(或其他组件)启动时的Intent，使用getIntent()方法:

```java
Intent intent = getIntent();

// get the URI
Uri locationUri = intent.getData();

// get the extra data
String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE); 
int positionX = intent.getIntExtra(MainActivity.EXTRA_POSITION_X);
int positionY = intent.getIntExtra(MainActivity.EXTRA_POSITION_Y);

Bundle extras = intent.getExtras();
String message = extras.getString(MainActivity.EXTRA_MESSAGE);
```

#### Getting data back from an Activity ####

