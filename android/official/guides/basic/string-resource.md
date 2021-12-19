# 字符串资源 #

字符串资源为您的应用提供具有可选文本样式和格式设置的文本字符串。共有三种类型的资源可为您的应用提供字符串：

## String ##

可从应用或其他资源文件（如 XML 布局）引用的单个字符串。

**文件位置**：

```
res/values/filename.xml
```

**编译资源的数据类型**：

指向 `String` 的资源指针。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string
        name="string_name"
        >text_string</string>
</resources>
```

## String Array ##

可从应用引用的字符串数组。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array
        name="string_array_name">
        <item
            >text_string</item>
    </string-array>
</resources>
```

## Quantity Strings (Plurals) ##

针对语法数量的一致性，不同语言有不同规则。

Android 支持以下完整集合：`zero`、`one`、`two`、`few`、`many` 和 `other`。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <plurals
        name="plural_name">
        <item
            quantity=["zero" | "one" | "two" | "few" | "many" | "other"]
            >text_string</item>
    </plurals>
</resources>
```

## 格式和样式 ##

