# 可绘制对象资源 #

可绘制对象资源是图形的一般概念，是指可在屏幕上绘制的图形，以及可使用 `getDrawable(int)` 等 API 检索，或应用到拥有 `android:drawable` 和 `android:icon` 等属性的其他 XML 资源的图形。

## 位图 ##

位图图像。Android 支持以下三种格式的位图文件：`.png`（首选）、`.jpg`（可接受）、`.gif`（不建议）。

### 位图文件 ###

位图文件是 `.png`、`.jpg` 或 `.gif` 文件。当您将任一位图文件保存到 `res/drawable/` 目录中时，Android 会为其创建 `Drawable` 资源。

**文件位置：**

`res/drawable/filename.png`

**编译资源的数据类型**：

指向 `BitmapDrawable` 的资源指针。

### XML位图 ###

XML 位图是在 XML 文件中定义的资源，指向位图文件。实际上是原始位图文件的别名。XML 可以指定位图的其他属性，例如抖动和层叠。

**文件位置：**

`res/drawable/filename.xml`

**编译资源的数据类型**：

指向 `BitmapDrawable` 的资源指针。

**语法：**

```xml
<?xml version="1.0" encoding="utf-8"?>
<bitmap
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:src="@[package:]drawable/drawable_resource"
    android:antialias=["true" | "false"]
    android:dither=["true" | "false"]
    android:filter=["true" | "false"]
    android:gravity=["top" | "bottom" | "left" | "right" | "center_vertical" |
                      "fill_vertical" | "center_horizontal" | "fill_horizontal" |
                      "center" | "fill" | "clip_vertical" | "clip_horizontal"]
    android:mipMap=["true" | "false"]
    android:tileMode=["disabled" | "clamp" | "repeat" | "mirror"] />
```

**元素：**

`<bitmap>` 定义位图来源及其属性:

- `android:src` *可绘制对象资源*。**必备**。引用可绘制对象资源。

- `android:antialias` *布尔值*。启用或停用抗锯齿。

- `android:dither` *布尔值*。当位图的像素配置与屏幕不同时（例如：ARGB 8888 位图和 RGB 565 屏幕），启用或停用位图抖动。

- `android:filter` *布尔值*。启用或停用位图过滤。当位图收缩或拉伸以使其外观平滑时使用过滤。

- `android:gravity` *关键字*。定义位图的重力。重力指示当位图小于容器时，可绘制对象在其容器中放置的位置。

  | 值                  | 说明                                                         |
  | :------------------ | :----------------------------------------------------------- |
  | `top`               | 将对象放在其容器顶部，不改变其大小。                         |
  | `bottom`            | 将对象放在其容器底部，不改变其大小。                         |
  | `left`              | 将对象放在其容器左边缘，不改变其大小。                       |
  | `right`             | 将对象放在其容器右边缘，不改变其大小。                       |
  | `center_vertical`   | 将对象放在其容器的垂直中心，不改变其大小。                   |
  | `fill_vertical`     | 按需要扩展对象的垂直大小，使其完全适应其容器。               |
  | `center_horizontal` | 将对象放在其容器的水平中心，不改变其大小。                   |
  | `fill_horizontal`   | 按需要扩展对象的水平大小，使其完全适应其容器。               |
  | `center`            | 将对象放在其容器的水平和垂直轴中心，不改变其大小。           |
  | `fill`              | 按需要扩展对象的垂直大小，使其完全适应其容器。这是默认值。   |
  | `clip_vertical`     | 可设置为让子元素的上边缘和/或下边缘裁剪至其容器边界的附加选项。裁剪基于垂直重力：顶部重力裁剪上边缘，底部重力裁剪下边缘，任一重力不会同时裁剪两边。 |
  | `clip_horizontal`   | 可设置为让子元素的左边和/或右边裁剪至其容器边界的附加选项。裁剪基于水平重力：左边重力裁剪右边缘，右边重力裁剪左边缘，任一重力不会同时裁剪两边。 |

- `android:mipMap` *布尔值*。启用或停用 mipmap 提示。
- `android:tileMode` *关键字*。定义平铺模式。当平铺模式启用时，位图会重复。重力在平铺模式启用时将被忽略。

## 九宫格 ##

[`NinePatch`](https://developer.android.google.cn/reference/android/graphics/NinePatch) 是一种 PNG 图像，您可在其中定义可伸缩区域，以便 Android 在视图中的内容超出正常图像边界时进行缩放。此类图像通常指定为至少有一个尺寸设置为 `"wrap_content"` 的视图背景，而且当视图通过扩展来适应内容时，九宫格图像也会通过扩展来匹配视图的大小。



