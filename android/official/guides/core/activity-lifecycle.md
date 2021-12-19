# 了解 Activity 生命周期 #

在生命周期回调方法中，您可以声明用户离开和再次进入 Activity 时 Activity 的行为方式。每个回调都支持您执行适合给定状态变更的特定作业。在合适的时间执行正确的作业，并妥善处理转换，这将提升应用的稳健性和性能。例如，良好的生命周期回调实现有助于防止应用出现以下问题：

- 当用户在使用应用时接听来电，或切换至另一应用时崩溃。
- 当用户未主动使用它时，消耗宝贵的系统资源。
- 当用户离开应用并在稍后返回时，丢失用户的进度。
- 当屏幕在横向和纵向之间旋转时，崩溃或丢失用户的进度。

如需了解有关处理生命周期的信息（包括最佳做法的相关指导），请参阅[使用生命周期感知型组件处理生命周期](https://developer.android.google.cn/topic/libraries/architecture/lifecycle)和[保存界面状态](https://developer.android.google.cn/topic/libraries/architecture/saving-states)。如需了解如何将 Activity 与架构组件结合使用，以构建生产质量的稳健应用，请参阅[应用架构指南](https://developer.android.google.cn/topic/libraries/architecture/guide)。

## Activity生命周期概念 ##

为了在 Activity 生命周期的各个阶段之间导航转换，Activity 类提供六个核心回调：`onCreate()`、`onStart()`、`onResume()`、`onPause()`、`onStop()` 和 `onDestroy()`。当 Activity 进入新状态时，系统会调用其中每个回调。

![img](.assets/activity_lifecycle.png)

## 生命周期回调 ##

本部分介绍 Activity 生命周期中所用回调方法的相关概念及实现信息。

某些操作（例如调用 [`setContentView()`](https://developer.android.google.cn/reference/android/app/Activity#setContentView(int))）属于 Activity 生命周期方法本身。不过，用于实现依赖组件操作的代码应放在组件本身内。为此，您必须使依赖组件具有生命周期感知能力。请参阅[使用生命周期感知型组件处理生命周期](https://developer.android.google.cn/topic/libraries/architecture/lifecycle)，了解如何让您的依赖组件获得生命周期感知能力。

### onCreate ###

在系统首次创建 Activity 时触发。Activity 会在创建后进入"已创建"状态。

执行基本应用启动逻辑，该逻辑在 Activity 的整个生命周期中只应发生一次。

如果您有一个生命周期感知型组件与您的 Activity 生命周期相关联，该组件将收到 [`ON_CREATE`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_CREATE) 事件。系统将调用带有 `@OnLifecycleEvent` 注释的方法，以使您的生命周期感知型组件可以执行已创建状态所需的任何设置代码。

您的 Activity 并未处于“已创建”状态。`onCreate()` 方法完成执行后，Activity 进入“已开始”状态，系统会相继调用 `onStart()` 和 `onResume()` 方法。

### onStart ###

当 Activity 进入“已开始”状态时，系统会调用此回调。`onStart()` 调用使 Activity 对用户可见，因为应用会为 Activity 进入前台并支持互动做准备。

当 Activity 进入已开始状态时，与 Activity 生命周期相关联的所有生命周期感知型组件都将收到 [`ON_START`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_START) 事件。

`onStart()` 方法会非常快速地完成，并且与“已创建”状态一样，Activity 不会一直处于“已开始”状态。一旦此回调结束，Activity 便会进入“已恢复”状态，系统将调用 `onResume()` 方法。

### onResume ###

Activity 会在进入“已恢复”状态时来到前台，然后系统调用 `onResume()` 回调。这是应用与用户互动的状态。应用会一直保持这种状态，直到某些事件发生，让焦点远离应用。

当 Activity 进入已恢复状态时，与 Activity 生命周期相关联的所有生命周期感知型组件都将收到 [`ON_RESUME`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_RESUME) 事件。这时，生命周期组件可以启用在组件可见且位于前台时需要运行的任何功能，例如启动相机预览。

当发生中断事件时，Activity 进入“已暂停”状态，系统调用 `onPause()` 回调。

如果 Activity 从“已暂停”状态返回“已恢复”状态，系统将再次调用 `onResume()` 方法。因此，您应实现 `onResume()`，以初始化在 [`onPause()`](https://developer.android.google.cn/reference/android/app/Activity#onPause()) 期间释放的组件，并执行每次 Activity 进入“已恢复”状态时必须完成的任何其他初始化操作。

## onPause ##

系统将此方法视为用户将要离开您的 Activity 的第一个标志（尽管这并不总是意味着 Activity 会被销毁）；此方法表示 Activity 不再位于前台（尽管在用户处于多窗口模式时 Activity 仍然可见）。使用 [`onPause()`](https://developer.android.google.cn/reference/android/app/Activity#onPause()) 方法暂停或调整当 [`Activity`](https://developer.android.google.cn/reference/android/app/Activity) 处于“已暂停”状态时不应继续（或应有节制地继续）的操作，以及您希望很快恢复的操作。

当 Activity 进入已暂停状态时，与 Activity 生命周期相关联的所有生命周期感知型组件都将收到 [`ON_PAUSE`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_PAUSE) 事件。这时，生命周期组件可以停止在组件未位于前台时无需运行的任何功能，例如停止相机预览。

您还可以使用 [`onPause()`](https://developer.android.google.cn/reference/android/app/Activity#onPause()) 方法释放系统资源、传感器（例如 GPS）手柄，或当您的 Activity 暂停且用户不需要它们时仍然可能影响电池续航时间的任何资源。然而，正如上文的 onResume() 部分所述，如果处于多窗口模式，“已暂停”的 Activity 仍完全可见。因此，您应该考虑使用 onStop() 而非 onPause() 来完全释放或调整与界面相关的资源和操作，以便更好地支持多窗口模式。

`onPause()` 执行非常简单，而且不一定要有足够的时间来执行保存操作。因此，您**不**应使用 `onPause()` 来保存应用或用户数据、进行网络调用或执行数据库事务。

`onPause()` 方法的完成并不意味着 Activity 离开“已暂停”状态。相反，Activity 会保持此状态，直到其恢复或变成对用户完全不可见。如果 Activity 恢复，系统将再次调用 `onResume()` 回调。

### onStop ###

如果您的 Activity 不再对用户可见，说明其已进入“已停止”状态，因此系统将调用 `onStop()` 回调。

如果 Activity 已结束运行并即将终止，系统还可以调用 `onStop()`。

当 Activity 进入已停止状态时，与 Activity 生命周期相关联的所有生命周期感知型组件都将收到 [`ON_STOP`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_STOP) 事件。这时，生命周期组件可以停止在组件未显示在屏幕上时无需运行的任何功能。

在 `onStop()` 方法中，应用应释放或调整在应用对用户不可见时的无用资源。

您还应使用 `onStop()` 执行 CPU 相对密集的关闭操作。

当您的 Activity 进入“已停止”状态时，`Activity` 对象会继续驻留在内存中：该对象将维护所有状态和成员信息，但不会附加到窗口管理器。Activity 恢复后，Activity 会重新调用这些信息。您无需重新初始化在任何回调方法导致 Activity 进入“已恢复”状态期间创建的组件。

进入“已停止”状态后，Activity 要么返回与用户互动，要么结束运行并消失。如果 Activity 返回，系统将调用 `onRestart()`。如果 `Activity` 结束运行，系统将调用 `onDestroy()`。

### onDestroy ###

销毁 Ativity 之前，系统会先调用 [`onDestroy()`](https://developer.android.google.cn/reference/android/app/Activity#onDestroy())。系统调用此回调的原因如下：

- Activity 即将结束（由于用户彻底关闭 Activity 或由于系统为 Activity 调用 [`finish()`](https://developer.android.google.cn/reference/android/app/Activity#finish())）
- 由于配置变更（例如设备旋转或多窗口模式），系统暂时销毁 Activity

当 Activity 进入已销毁状态时，与 Activity 生命周期相关联的所有生命周期感知型组件都将收到 [`ON_DESTROY`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle.Event#ON_DESTROY) 事件。这时，生命周期组件可以在 Activity 被销毁之前清理所需的任何数据。

## Activity状态和从内存中弹出 ##

系统会在需要释放 RAM 时终止进程；系统终止给定进程的可能性取决于当时进程的状态。反之，进程状态取决于在进程中运行的 Activity 的状态。

| 系统终止进程的可能性 | 进程状态                   | Activity 状态                    |
| :------------------- | :------------------------- | :------------------------------- |
| 较小                 | 前台（拥有或即将获得焦点） | 已创建 <br />已开始 <br />已恢复 |
| 较大                 | 后台（失去焦点）           | 已暂停                           |
| 最大                 | 后台（不可见）             | 已停止                           |
|                      | 空                         | 已销毁                           |

系统永远不会直接终止 Activity 以释放内存，而是会终止 Activity 所在的进程。系统不仅会销毁 Activity，还会销毁在该进程中运行的所有其他内容。

如需详细了解一般进程，请参阅[进程和线程](https://developer.android.google.cn/guide/components/processes-and-threads)。如需详细了解进程生命周期如何与其中 Activity 的状态相关联，请参阅相应页面的[进程生命周期](https://developer.android.google.cn/guide/components/processes-and-threads#Lifecycle)部分。

## 保存和恢复瞬时界面状态 ##

当 Activity 因系统限制而被销毁时，您应组合使用 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel)、[`onSaveInstanceState()`](https://developer.android.google.cn/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) 和/或本地存储来保留用户的瞬时界面状态。如需详细了解用户期望与系统行为，以及如何在系统启动的 Activity 和进程被终止后最大程度地保留复杂的界面状态数据，请参阅[保存界面状态](https://developer.android.google.cn/topic/libraries/architecture/saving-states)。

如果界面数据简单且轻量，例如原始数据类型或简单对象（比如 String），您可以单独使用 onSaveInstanceState() 使界面状态在配置更改和系统启动的进程被终止时保持不变。但在大多数情况下，您应使用 ViewModel 和 onSaveInstanceState()（如[ 保存界面状态](https://developer.android.google.cn/topic/libraries/architecture/saving-states)中所述），因为 onSaveInstanceState() 会产生序列化/反序列化费用。

### 示例状态 ###

但是，如果系统因系统限制（例如配置变更或内存压力）而销毁 Activity，虽然实际的 [`Activity`](https://developer.android.google.cn/reference/android/app/Activity) 实例会消失，但系统会记住它曾经存在过。如果用户尝试回退到该 Activity，系统将使用一组描述 Activity 销毁时状态的已保存数据新建该 Activity 的实例。

系统用于恢复先前状态的已保存数据称为实例状态，是存储在 [`Bundle`](https://developer.android.google.cn/reference/android/os/Bundle) 对象中的键值对集合。默认情况下，系统使用 [`Bundle`](https://developer.android.google.cn/reference/android/os/Bundle) 实例状态来保存 Activity 布局中每个 [`View`](https://developer.android.google.cn/reference/android/view/View) 对象的相关信息

### 使用 onSaveInstanceState() 保存简单轻量的界面状态 ###

当您的 Activity 开始停止时，系统会调用 [`onSaveInstanceState()`](https://developer.android.google.cn/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) 方法，以便您的 Activity 可以将状态信息保存到实例状态 Bundle 中。此方法的默认实现保存有关 Activity 视图层次结构状态的瞬时信息，

```java
static final String STATE_SCORE = "playerScore";
static final String STATE_LEVEL = "playerLevel";
// ...

@Override
public void onSaveInstanceState(Bundle savedInstanceState) {
    // Save the user's current game state
    savedInstanceState.putInt(STATE_SCORE, currentScore);
    savedInstanceState.putInt(STATE_LEVEL, currentLevel);

    // Always call the superclass so it can save the view hierarchy state
    super.onSaveInstanceState(savedInstanceState);
}
```

> 当用户显式关闭 Activity 时，或者在其他情况下调用 `finish()` 时，系统不会调用 [`onSaveInstanceState()`](https://developer.android.google.cn/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle))。

如需保存持久性数据（例如用户首选项或数据库中的数据），您应在 Activity 位于前台时抓住合适机会。如果没有这样的时机，您应在执行 [`onStop()`](https://developer.android.google.cn/reference/android/app/Activity#onStop()) 方法期间保存此类数据。

### 使用保存的实例状态恢复 Activity 界面状态 ###

无论系统是新建 Activity 实例还是重新创建之前的实例，都会调用 [`onCreate()`](https://developer.android.google.cn/reference/android/app/Activity#onCreate(android.os.Bundle)) 方法，所以在尝试读取之前，您必须检查状态 Bundle 是否为 null。如果为 null，系统将新建 Activity 实例，而不会恢复之前销毁的实例。

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState); // Always call the superclass first

    // Check whether we're recreating a previously destroyed instance
    if (savedInstanceState != null) {
        // Restore value of members from saved state
        currentScore = savedInstanceState.getInt(STATE_SCORE);
        currentLevel = savedInstanceState.getInt(STATE_LEVEL);
    } else {
        // Probably initialize members with default values for a new instance
    }
    // ...
}
```

您可以选择实现系统在 [`onStart()`](https://developer.android.google.cn/reference/android/app/Activity#onStart()) 方法之后调用的 [`onRestoreInstanceState()`](https://developer.android.google.cn/reference/android/app/Activity#onRestoreInstanceState(android.os.Bundle))，而不是在 [`onCreate()`](https://developer.android.google.cn/reference/android/app/Activity#onCreate(android.os.Bundle)) 期间恢复状态。仅当存在要恢复的已保存状态时，系统才会调用 [`onRestoreInstanceState()`](https://developer.android.google.cn/reference/android/app/Activity#onRestoreInstanceState(android.os.Bundle))，因此您无需检查 [`Bundle`](https://developer.android.google.cn/reference/android/os/Bundle) 是否为 null：

```java
public void onRestoreInstanceState(Bundle savedInstanceState) {
    // Always call the superclass so it can restore the view hierarchy
    super.onRestoreInstanceState(savedInstanceState);

    // Restore state members from saved instance
    currentScore = savedInstanceState.getInt(STATE_SCORE);
    currentLevel = savedInstanceState.getInt(STATE_LEVEL);
}
```

## 在Activity之间导航 ##

在应用的生命周期中，应用很可能会多次进入和退出 Activity。

### 从一个 Activity 启动另一个 Activity ###

根据您的 Activity 是否希望从即将启动的新 Activity 中获取返回结果，您可以使用 `startActivity()` 或 `startActivityForResult()` 方法启动新 Activity。这两种方法都需要传入一个 `Intent` 对象。

`Intent` 对象指定您要启动的具体 Activity，或描述您要执行的操作类型（系统为您选择相应的 Activity，该 Activity 甚至可以来自不同应用）。`Intent` 对象还可以携带由已启动的 Activity 使用的少量数据。如需详细了解 `Intent` 类，请参阅 [Intent 和 Intent 过滤器](https://developer.android.google.cn/guide/components/intents-filters)。

### startActivity ###

```java
Intent intent = new Intent(this, SignInActivity.class);
startActivity(intent);
```

您的应用可能还希望使用 Activity 中的数据执行某些操作，例如发送电子邮件、短信或状态更新。在这种情况下，您的应用自身可能不具有执行此类操作所需的 Activity，因此您可以改为利用设备上其他应用提供的 Activity 为您执行这些操作。这便是 intent 的真正价值所在。您可以创建一个 intent，对您想执行的操作进行描述，系统会从其他应用启动相应的 Activity。如果有多个 Activity 可以处理 intent，用户可以选择要使用哪一个。例如，如果您想允许用户发送电子邮件，可以创建以下 intent：

```java
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra(Intent.EXTRA_EMAIL, recipientArray);
startActivity(intent);
```

### startActivityForResult ###

有时，您会希望在 Activity 结束时从 Activity 中获取返回结果。例如，您可以启动一项 Activity，让用户在联系人列表中选择收件人；当 Activity 结束时，系统将返回用户选择的收件人。

为此，您可以调用 `startActivityForResult(Intent, int)` 方法，其中整数参数会标识该调用。此标识符用于消除来自同一 Activity 的多次 `startActivityForResult(Intent, int)` 调用之间的歧义。这不是全局标识符，不存在与其他应用或 Activity 冲突的风险。结果通过 `onActivityResult(int, int, Intent)` 方法返回。

```java
public class MyActivity extends Activity {
     // ...

     static final int PICK_CONTACT_REQUEST = 0;

     public boolean onKeyDown(int keyCode, KeyEvent event) {
         if (keyCode == KeyEvent.KEYCODE_DPAD_CENTER) {
             // When the user center presses, let them pick a contact.
             startActivityForResult(
                 new Intent(Intent.ACTION_PICK,
                 new Uri("content://contacts")),
                 PICK_CONTACT_REQUEST);
            return true;
         }
         return false;
     }

     protected void onActivityResult(int requestCode, int resultCode,
             Intent data) {
         if (requestCode == PICK_CONTACT_REQUEST) {
             if (resultCode == RESULT_OK) {
                 // A contact was picked.  Here we will just display it
                 // to the user.
                 startActivity(new Intent(Intent.ACTION_VIEW, data));
             }
         }
     }
 }
```

### 协调Activity ###

当一个 Activity 启动另一个 Activity 时，它们都会经历生命周期转换。

生命周期回调的顺序已有明确定义，特别是当两个 Activity 在同一个进程（应用）中，并且其中一个要启动另一个时。以下是 Activity A 启动 Activity B 时的操作发生顺序：

1. Activity A 的 `onPause()` 方法执行。
1. Activity B 的 `onCreate()`、`onStart()` 和 `onResume()` 方法依次执行（Activity B 现在具有用户焦点）。
1. 然后，如果 Activity A 在屏幕上不再显示，其 `onStop()` 方法执行。

您可以利用这种可预测的生命周期回调顺序管理从一个 Activity 到另一个 Activity 的信息转换。

