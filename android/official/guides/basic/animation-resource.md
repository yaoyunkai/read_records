# 动画资源 #

一个动画资源可以定义以下两种动画类型之一：

**属性动画**：

通过使用 [`Animator`](https://developer.android.google.cn/reference/android/animation/Animator) 在设定的时间段内修改对象的属性值来创建动画。

**视图动画**：

使用视图动画框架可以创建两种类型的动画：

- [补间动画](https://developer.android.google.cn/guide/topics/resources/animation-resource#Tween)：通过使用 [`Animation`](https://developer.android.google.cn/reference/android/view/animation/Animation) 对单张图片执行一系列转换来创建动画
- [帧动画](https://developer.android.google.cn/guide/topics/resources/animation-resource#Frame)：通过使用 [`AnimationDrawable`](https://developer.android.google.cn/reference/android/graphics/drawable/AnimationDrawable) 按顺序显示一系列图片来创建动画。

## 属性动画 ##

在 XML 中定义的动画，用于在设定的一段时间内修改目标对象的属性，例如背景颜色或 Alpha 值。

**文件位置**

`res/animator/filename.xml` 该文件名将用作资源 ID。

**编译后的资源数据类型：**

指向 `ValueAnimator`、`ObjectAnimator` 或 `AnimatorSet` 的资源指针。

**语法：**

```xml
<set
     android:ordering=["together" | "sequentially"]>

    <objectAnimator
                    android:propertyName="string"
                    android:duration="int"
                    android:valueFrom="float | int | color"
                    android:valueTo="float | int | color"
                    android:startOffset="int"
                    android:repeatCount="int"
                    android:repeatMode=["repeat" | "reverse"]
                    android:valueType=["intType" | "floatType"]/>

    <animator
              android:duration="int"
              android:valueFrom="float | int | color"
              android:valueTo="float | int | color"
              android:startOffset="int"
              android:repeatCount="int"
              android:repeatMode=["repeat" | "reverse"]
              android:valueType=["intType" | "floatType"]/>

    <set>
        ...
    </set>
</set>
```

该文件必须具有一个根元素，可以是 `<set>`、`<objectAnimator>` 或 `<valueAnimator>`。您可以将动画元素（包括其他 `<set>` 元素）组合到 `<set>` 元素中。

**元素：**

- `<set>`

  容纳其他动画元素（`<objectAnimator>`、`<valueAnimator>` 或其他 `<set>` 元素）的容器。代表 `AnimatorSet`。您可以指定嵌套的 `<set>` 标记来将动画进一步组合在一起。每个 `<set>` 都可以定义自己的 `ordering` 属性。

- `android:ordering`关键字。指定此集合中动画的播放顺序。

- `<objectAnimator>` 在特定的一段时间内为对象的特定属性创建动画。代表 `ObjectAnimator`。

- `android:propertyName` 字符串。必需。要添加动画的对象属性，通过其名称引用。

- `android:valueTo` 动画属性的结束值。

- `android:valueFrom` 动画属性的开始值。

- `android:duration` 动画的时间，以毫秒为单位。

- `android:startOffset` 调用 `start()` 后动画延迟的毫秒数。

- `android:repeatCount` 动画的重复次数。

- `android:repeatMode` 动画播放到结尾处的行为。

- `android:valueType` 

  | 值                  | 说明               |
  | :------------------ | :----------------- |
  | `intType`           | 指定动画值为整数   |
  | `floatType`（默认） | 指定动画值为浮点数 |

- `<animator>` 在指定的时间段内执行动画。代表 `ValueAnimator`。

另请参阅：

- [属性动画](https://developer.android.google.cn/guide/topics/graphics/prop-animation)
- 有关如何使用属性动画系统的示例，请参阅 [API 演示](https://developer.android.google.cn/resources/samples/ApiDemos/src/com/example/android/apis/animation)。

## 视图动画 ##

视图动画框架可支持补间动画和逐帧动画，两者都可以在 XML 中声明。

### 补间动画 ###

在 XML 中定义的动画，用于对图形执行旋转、淡出、移动和拉伸等转换。

**文件位置**

`res/anim/filename.xml`

**编译后的资源数据类型：**

指向 `Animation` 的资源指针。

**语法：**

```xml
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
     android:interpolator="@[package:]anim/interpolator_resource"
     android:shareInterpolator=["true" | "false"] >
    <alpha
           android:fromAlpha="float"
           android:toAlpha="float" />
    <scale
           android:fromXScale="float"
           android:toXScale="float"
           android:fromYScale="float"
           android:toYScale="float"
           android:pivotX="float"
           android:pivotY="float" />
    <translate
               android:fromXDelta="float"
               android:toXDelta="float"
               android:fromYDelta="float"
               android:toYDelta="float" />
    <rotate
            android:fromDegrees="float"
            android:toDegrees="float"
            android:pivotX="float"
            android:pivotY="float" />
    <set>
        ...
    </set>
</set>
```

该文件必须具有一个根元素，可以是 `<alpha>`、`<scale>`、`<translate>`、`<rotate>` 或包含一组（或多组）其他动画元素（甚至是嵌套的 `<set>` 元素）的 `<set>` 元素。

**元素：**

`<set>` : 容纳其他动画元素（`<alpha>`、`<scale>`、`<translate>`、`<rotate>`）或其他 `<set>` 元素的容器。代表 `AnimationSet`。

- `android:interpolator` : 插值器资源。 要应用于动画的 `Interpolator`。
- `android:shareInterpolator` 布尔值。如果要在所有子元素中共用同一插值器，则为“true”。

`<alpha>` 淡入或淡出动画。代表 `AlphaAnimation`。

- `android:fromAlpha` 浮点数。起始不透明度偏移，0.0 表示透明，1.0 表示不透明。
- `android:toAlpha` *浮点数*。结束不透明度偏移，0.0 表示透明，1.0 表示不透明。

`<scale>` 大小调整动画。您可以通过指定 `pivotX` 和 `pivotY`，来指定图片向外（或向内）扩展的中心点。例如，如果这两个值为 0、0（左上角），则所有扩展均向右下方向进行。代表 `ScaleAnimation`。

- `android:fromXScale`  浮点数。起始 X 尺寸偏移，其中 1.0 表示不变。
- `android:toXScale` 浮点数。结束 X 尺寸偏移，其中 1.0 表示不变。
- `android:fromYScale` 浮点数。起始 Y 尺寸偏移，其中 1.0 表示不变。
- `android:toYScale` 浮点数。结束 Y 尺寸偏移，其中 1.0 表示不变。
- `android:pivotX` 浮点数。在对象缩放时要保持不变的 X 坐标。
- `android:pivotY` 浮点数。在对象缩放时要保持不变的 Y 坐标。

`<translate>` 垂直和/或水平移动。支持采用以下三种格式之一的以下属性：从 -100 到 100 的以“％”结尾的值，表示相对于自身的百分比；从 -100 到 100 的以“％p”结尾的值，表示相对于其父项的百分比；不带后缀的浮点值，表示绝对值。代表 `TranslateAnimation`。

- `android:fromXDelta `浮动数或百分比。起始 X 偏移。
- `android:toXDelta` 浮动数或百分比。结束 X 偏移。
- `android:fromYDelta` 浮动数或百分比。起始 Y 偏移。
- `android:toYDelta` 浮动数或百分比。结束 Y 偏移。

`<rotate>`

旋转动画。代表 `RotateAnimation`。

- `android:fromDegrees` 浮点数。起始角度位置，以度为单位。
- `android:toDegrees` 浮点数。结束角度位置，以度为单位。
- `android:pivotX` 浮动数或百分比。旋转中心的 X 坐标。
- `android:pivotY` 浮点数或百分比。旋转中心的 Y 坐标。

#### 插值器 ####

插值器是在 XML 中定义的动画修改器，它会影响动画的变化率。插值器可对现有的动画效果执行加速、减速、重复、退回等。

插值器通过 `android:interpolator` 属性应用于动画元素，该属性的值是对插值器资源的引用。

| 插值器类                           | 资源 ID                                            |
| :--------------------------------- | :------------------------------------------------- |
| `AccelerateDecelerateInterpolator` | `@android:anim/accelerate_decelerate_interpolator` |
| `AccelerateInterpolator`           | `@android:anim/accelerate_interpolator`            |
| `AnticipateInterpolator`           | `@android:anim/anticipate_interpolator`            |
| `AnticipateOvershootInterpolator`  | `@android:anim/anticipate_overshoot_interpolator`  |
| `BounceInterpolator`               | `@android:anim/bounce_interpolator`                |
| `CycleInterpolator`                | `@android:anim/cycle_interpolator`                 |
| `DecelerateInterpolator`           | `@android:anim/decelerate_interpolator`            |
| `LinearInterpolator`               | `@android:anim/linear_interpolator`                |
| `OvershootInterpolator`            | `@android:anim/overshoot_interpolator`             |

### 帧动画 ###

在 XML 中定义的按顺序显示一系列图片的动画（如电影）。

**文件位置**

`res/drawable/filename.xml`

**编译后的资源数据类型：**

指向 `AnimationDrawable` 的资源指针。

**语法：**

```xml
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
                android:oneshot=["true" | "false"] >
    <item
          android:drawable="@[package:]drawable/drawable_resource_name"
          android:duration="integer" />
</animation-list>
```

**元素：**

`<animation-list>` 此元素必须是根元素。包含一个或多个 `<item>` 元素。

- `android:oneshot` 布尔值。如果您想要执行一次动画，则为“true”；如果要循环播放动画，则为“false”。

`<item>` 单帧动画。必须是 `<animation-list>` 元素的子元素。

- `android:drawable` 可绘制资源。要用于此帧的可绘制对象。
- `android:duration` 整数。显示此帧的持续时间，以毫秒为单位。

