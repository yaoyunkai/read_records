# 动画资源 #

一个动画资源可以定义以下两种动画类型之一：

**属性动画**：

通过使用 `Animator` 在设定的时间段内修改对象的属性值来创建动画。

**视图动画**：

使用视图动画框架可以创建两种类型的动画：

- [补间动画](https://developer.android.google.cn/guide/topics/resources/animation-resource#Tween)：通过使用 `Animation` 对单张图片执行一系列转换来创建动画
- [帧动画](https://developer.android.google.cn/guide/topics/resources/animation-resource#Frame)：通过使用 `AnimationDrawable` 按顺序显示一系列图片来创建动画。

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

