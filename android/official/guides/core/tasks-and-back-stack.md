# 了解任务和返回堆栈 #

任务是用户在执行某项工作时与之互动的一系列 Activity 的集合。这些 Activity 按照每个 Activity 打开的顺序排列在一个返回堆栈中。

当用户轻触应用启动器中的图标（或主屏幕上的快捷方式）时，该应用的任务就会转到前台运行。如果该应用没有任务存在（应用最近没有使用过），则会创建一个新的任务，并且该应用的“主”Activity 将会作为堆栈的根 Activity 打开。

在当前 Activity 启动另一个 Activity 时，新的 Activity 将被推送到堆栈顶部并获得焦点。上一个 Activity 仍保留在堆栈中，但会停止。当 Activity 停止时，系统会保留其界面的当前状态。当用户按**返回**按钮时，当前 Activity 会从堆栈顶部退出（该 Activity 销毁），上一个 Activity 会恢复（界面会恢复到上一个状态）。堆栈中的 Activity 永远不会重新排列，只会被送入和退出，在当前 Activity 启动时被送入堆栈，在用户使用**返回**按钮离开时从堆栈中退出。

![img](.assets/diagram_backstack.png)

如果用户继续按**返回**，则堆栈中的 Activity 会逐个退出，以显示前一个 Activity，直到用户返回到主屏幕（或任务开始时运行的 Activity）。移除堆栈中的所有 Activity 后，该任务将不复存在。

任务是一个整体单元，当用户开始一个新任务或通过主屏幕按钮进入主屏幕时，任务可移至“后台”。在后台时，任务中的所有 Activity 都会停止，但任务的返回堆栈会保持不变，当其他任务启动时，当前任务只是失去了焦点，

由于返回堆栈中的 Activity 不会被重新排列，如果您的应用允许用户从多个 Activity 启动特定的 Activity，系统便会创建该 Activity 的新实例并将其推送到堆栈中（而不是将该 Activity 的某个先前的实例移至堆栈顶部）。这样一来，应用中的一个 Activity 就可能被多次实例化（甚至是从其他任务对其进行实例化），如图 3 所示。因此，如果用户使用**返回**按钮向后导航，Activity 的每个实例将按照它们被打开的顺序显示出来（每个实例都有自己的界面状态）。不过，如果您不希望某个 Activity 被实例化多次，可以修改此行为。有关如何实现此操作，将在后面的[管理任务](https://developer.android.google.cn/guide/components/activities/tasks-and-back-stack#ManagingTasks)部分中讨论。

Activity 和任务的默认行为总结如下：

- 当 Activity A 启动 Activity B 时，Activity A 会停止，但系统会保留其状态（例如滚动位置和输入到表单中的文本）。如果用户在 Activity B 中按**返回**按钮，系统会恢复 Activity A 及其状态。
- 当用户通过按主屏幕按钮离开任务时，当前 Activity 会停止，其任务会转到后台。系统会保留任务中每个 Activity 的状态。如果用户稍后通过点按该任务的启动器图标来恢复该任务，该任务会进入前台并恢复堆栈顶部的 Activity。
- 如果用户按**返回**按钮，当前 Activity 将从堆栈中退出并销毁。堆栈中的上一个 Activity 将恢复。Activity 被销毁后，系统不会保留该 Activity 的状态。
- Activity 可以多次实例化，甚至是从其他任务对其进行实例化。

## 管理任务 ##

Android 管理任务和返回堆栈的方式是将所有接连启动的 Activity 放到同一任务和一个“后进先出”堆栈中，

或许您希望应用中的某个 Activity 在启动时开启一个新的任务（而不是被放入当前的任务中），或者当您启动某个 Activity 时，您希望调用它的一个现有实例（而不是在返回堆栈顶部创建一个新实例），或者您希望在用户离开任务时清除返回堆栈中除根 Activity 以外的所有 Activity。

可以借助 `<activity>` 清单元素中的属性以及您传递给 startActivity() 的 intent 中的标记来实现上述目的。

在这方面，您可以使用的主要 `<activity>` 属性包括：

- [`taskAffinity`](https://developer.android.google.cn/guide/topics/manifest/activity-element#aff)
- [`launchMode`](https://developer.android.google.cn/guide/topics/manifest/activity-element#lmode)
- [`allowTaskReparenting`](https://developer.android.google.cn/guide/topics/manifest/activity-element#reparent)
- [`clearTaskOnLaunch`](https://developer.android.google.cn/guide/topics/manifest/activity-element#clear)
- [`alwaysRetainTaskState`](https://developer.android.google.cn/guide/topics/manifest/activity-element#always)
- [`finishOnTaskLaunch`](https://developer.android.google.cn/guide/topics/manifest/activity-element#finish)

您可以使用的主要 intent 标记包括：

- `FLAG_ACTIVITY_NEW_TASK`
- `FLAG_ACTIVITY_CLEAR_TOP`
- `FLAG_ACTIVITY_SINGLE_TOP`

### 定义启动模式 ###

您可以通过启动模式定义 Activity 的新实例如何与当前任务关联。您可以通过两种方式定义不同的启动模式：

- 使用清单文件

  当您在清单文件中声明 Activity 时，您可以指定该 Activity 在启动时如何与任务关联。

- 使用 Intent 标记

  当您调用 `startActivity()` 时，可以在 `Intent` 中添加一个标记，用于声明新 Activity 如何（或是否）与当前任务相关联。

因此，如果 Activity A 启动 Activity B，Activity B 可在其清单中定义如何与当前任务相关联（如果关联的话），Activity A 也可以请求 Activity B 应该如何与当前任务关联。如果两个 Activity 都定义了 Activity B 应如何与任务关联，将优先遵循 Activity A 的请求（在 intent 中定义），而不是 Activity B 的请求（在清单中定义）。

### 使用清单文件 ###

在清单文件中声明 Activity 时，可以使用 `<activity>` 元素的 `launchMode` 属性指定 Activity 应该如何与任务关联。

[`launchMode`](https://developer.android.google.cn/guide/topics/manifest/activity-element#lmode) 属性说明了 Activity 应如何启动到任务中。您可以为 `launchMode` 属性指定 4 种不同的启动模式：

- standard : 默认值。系统在启动该 Activity 的任务中创建 Activity 的新实例，并将 intent 传送给该实例。Activity 可以多次实例化，每个实例可以属于不同的任务，一个任务可以拥有多个实例。

- singleTop (栈顶复用模式) : 如果当前任务的顶部已存在 Activity 的实例，则系统会通过调用其 `onNewIntent()` 方法来将 intent 转送给该实例，而不是创建 Activity 的新实例。Activity 可以多次实例化，每个实例可以属于不同的任务，一个任务可以拥有多个实例（但前提是返回堆栈顶部的 Activity 不是该 Activity 的现有实例）。

- singleTask (栈内复用模式) : 系统会创建新任务，并实例化新任务的根 Activity。但是，如果另外的任务中已存在该 Activity 的实例，则系统会通过调用其 `onNewIntent()` 方法将 intent 转送到该现有实例，而不是创建新实例。Activity 一次只能有一个实例存在。

  在复用的时候，首先会根据taskAffinity去找对应的任务栈：
  1、如果不存在指定的任务栈，系统会新建对应的任务栈，并新建Activity实例压入栈中。
  2、如果存在指定的任务栈，则会查找该任务栈中是否存在该Activity实例
        a、如果不存在该实例，则会在该任务栈中新建Activity实例。
        b、如果存在该实例，则会直接引用，并且回调该实例的onNewIntent()方法。并且任务栈中该实例之上的Activity会被全部销毁。

- singleInstance : 与 `"singleTask"` 相似，唯一不同的是系统不会将任何其他 Activity 启动到包含该实例的任务中。该 Activity 始终是其任务唯一的成员；由该 Activity 启动的任何 Activity 都会在其他的任务中打开。

  单实例模式，顾名思义，只有一个实例。该模式具备singleTask模式的所有特性外，与它的区别就是，这种模式下的Activity会单独占用一个Task栈，具有全局唯一性，即整个系统中就这么一个实例，由于栈内复用的特性，后续的请求均不会创建新的Activity实例，除非这个特殊的任务栈被销毁了。

再举个例子，Android 浏览器应用在 `<activity>` 元素中指定 singleTask 启动模式，由此声明网络浏览器 Activity 应始终在它自己的任务中打开。

### 使用Intent标记 ###

启动 Activity 时，您可以在传送给 `startActivity()` 的 intent 中添加相应的标记来修改 Activity 与其任务的默认关联。您可以使用以下标记来修改默认行为：

- `FLAG_ACTIVITY_NEW_TASK` 

  在新任务中启动 Activity。如果您现在启动的 Activity 已经有任务在运行，则系统会将该任务转到前台并恢复其最后的状态，而 Activity 将在 `onNewIntent()` 中收到新的 intent。

  这与上一节中介绍的 `"singleTask"` [`launchMode`](https://developer.android.google.cn/guide/topics/manifest/activity-element#lmode) 值产生的行为相同。

- `FLAG_ACTIVITY_SINGLE_TOP`

  如果要启动的 Activity 是当前 Activity（即位于返回堆栈顶部的 Activity），则现有实例会收到对 `onNewIntent()` 的调用，而不会创建 Activity 的新实例。

  这与上一节中介绍的 `"singleTop"` [`launchMode`](https://developer.android.google.cn/guide/topics/manifest/activity-element#lmode) 值产生的行为相同。

- `FLAG_ACTIVITY_CLEAR_TOP`

  如果要启动的 Activity 已经在当前任务中运行，则不会启动该 Activity 的新实例，而是会销毁位于它之上的所有其他 Activity，并通过 `onNewIntent()` 将此 intent 传送给它的已恢复实例（现在位于堆栈顶部）。

### 处理亲和性 ###

“亲和性”表示 Activity 倾向于属于哪个任务。默认情况下，同一应用中的所有 Activity 彼此具有亲和性。因此，在默认情况下，同一应用中的所有 Activity 都倾向于位于同一任务。不过，您可以修改 Activity 的默认亲和性。在不同应用中定义的 Activity 可以具有相同的亲和性，或者在同一应用中定义的 Activity 也可以被指定不同的任务亲和性。

您可以使用 `<activity>` 元素的 `taskAffinity` 属性修改任何给定 Activity 的亲和性。

### 清除返回堆栈 ###

如果用户离开任务较长时间，系统会清除任务中除根 Activity 以外的所有 Activity。当用户再次返回到该任务时，只有根 Activity 会恢复。系统之所以采取这种行为方式是因为，经过一段时间后，用户可能已经放弃了之前执行的操作，现在返回任务是为了开始某项新的操作。

您可以使用一些 Activity 属性来修改此行为：

- alwaysRetainTaskState

  如果在任务的根 Activity 中将该属性设为 `"true"`，则不会发生上述默认行为。即使经过很长一段时间后，任务仍会在其堆栈中保留所有 Activity。

- clearTaskOnLaunch

  如果在任务的根 Activity 中将该属性设为 `"true"`，那么只要用户离开任务再返回，堆栈就会被清除到只剩根 Activity。也就是说，它与 [`alwaysRetainTaskState`](https://developer.android.google.cn/guide/topics/manifest/activity-element#always) 正好相反。用户始终会返回到任务的初始状态，即便只是短暂离开任务也是如此。

- finishOnTaskLaunch

  该属性与 [`clearTaskOnLaunch`](https://developer.android.google.cn/guide/topics/manifest/activity-element#clear) 类似，但它只会作用于单个 Activity 而非整个任务。它还可导致任何 Activity 消失，包括根 Activity。如果将该属性设为 `"true"`，则 Activity 仅在当前会话中归属于任务。如果用户离开任务再返回，则该任务将不再存在。

### 启动任务 ###

您可以设置一个 Activity 作为任务的入口点，方法是为该 Activity 提供一个 intent 过滤器，并将 `"android.intent.action.MAIN"` 作为指定操作，将 `"android.intent.category.LAUNCHER"` 作为指定类别。

```xml
<activity ... >
    <intent-filter ... >
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    ...
</activity>
```

这种 intent 过滤器可在应用启动器中显示 Activity 的图标和标签，让用户可以启动 Activity 并在启动后随时返回到该 Activity 创建的任务。

第二个作用非常重要：用户必须能够离开任务，之后再使用此 Activity 启动器返回到该任务。因此，只有当 Activity 具有 `ACTION_MAIN` 和 `CATEGORY_LAUNCHER` 过滤器时，才应使用 `"singleTask"` 和 `"singleInstance"` 这两种启动模式，它们会将 Activity 标记为始终启动任务。

