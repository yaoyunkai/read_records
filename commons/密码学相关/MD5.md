# MD5

## 目录

-   [算法](#算法)
-   [伪代码](#伪代码)
-   [MD5散列](#MD5散列)

**MD5消息摘要算法**（英语：MD5 Message-Digest Algorithm），一种被广泛使用的[密码散列函数](https://zh.wikipedia.org/wiki/密碼雜湊函數 "密码散列函数")，可以产生出一个128位（16个字符(BYTES)）的散列值（hash value），用于确保信息传输完整一致。MD5由美国密码学家[罗纳德·李维斯特](https://zh.wikipedia.org/wiki/罗纳德·李维斯特 "罗纳德·李维斯特")（Ronald Linn Rivest）设计，于1992年公开，用以取代[MD4](https://zh.wikipedia.org/wiki/MD4 "MD4")算法。这套算法的程序在 [RFC 1321](https://tools.ietf.org/html/rfc1321 "RFC 1321") 中被加以规范。

## 算法

MD5是输入不定长度信息，输出固定长度128-bits的算法。经过程序流程，生成四个32位数据，最后联合起来成为一个128-bits[散列](https://zh.wikipedia.org/wiki/散列 "散列")。基本方式为，求余、取余、调整长度、与链接变量进行循环运算。得出结果。

$$
F(X,Y,Z) = (X\wedge{Y}) \vee (\neg{X} \wedge{Z}) \\
G(X,Y,Z) = (X\wedge{Z}) \vee (Y \wedge \neg{Z})  \\
H(X,Y,Z) = X \oplus Y \oplus Z \\
I(X,Y,Z) = Y \oplus (X \vee \neg{Z}) \\
$$

$\oplus, \wedge, \vee, \neg$ 是 `XOR`, `AND`, `OR` , `NOT` 的符号。

## 伪代码

```pascal
//Note: All variables are unsigned 32 bits and wrap modulo 2^32 when calculating
var int[64] r, k

//r specifies the per-round shift amounts
r[ 0..15]：= {7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22} 
r[16..31]：= {5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20}
r[32..47]：= {4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23}
r[48..63]：= {6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21}

//Use binary integer part of the sines of integers as constants:
for i from 0 to 63
    k[i] := floor(abs(sin(i + 1)) × 2^32)

//Initialize variables:
var int h0 := 0x67452301
var int h1 := 0xEFCDAB89
var int h2 := 0x98BADCFE
var int h3 := 0x10325476

//Pre-processing:
append "1" bit to message
append "0" bits until message length in bits ≡ 448 (mod 512)
append bit length of message as 64-bit little-endian integer to message

//Process the message in successive 512-bit chunks:
for each 512-bit chunk of message
    break chunk into sixteen 32-bit little-endian words w[i], 0 ≤ i ≤ 15

    //Initialize hash value for this chunk:
    var int a := h0
    var int b := h1
    var int c := h2
    var int d := h3

    //Main loop:
    for i from 0 to 63
        if 0 ≤ i ≤ 15 then
            f := (b and c) or ((not b) and d)
            g := i
        else if 16 ≤ i ≤ 31
            f := (d and b) or ((not d) and c)
            g := (5×i + 1) mod 16
        else if 32 ≤ i ≤ 47
            f := b xor c xor d
            g := (3×i + 5) mod 16
        else if 48 ≤ i ≤ 63
            f := c xor (b or (not d))
            g := (7×i) mod 16
 
        temp := d
        d := c
        c := b
        b := leftrotate((a + f + k[i] + w[g]),r[i]) + b
        a := temp
    Next i
    //Add this chunk's hash to result so far:
    h0 := h0 + a
    h1 := h1 + b 
    h2 := h2 + c
    h3 := h3 + d
End ForEach
var int digest := h0 append h1 append h2 append h3 //(expressed as little-endian)
```

## MD5散列

一般128位的MD5散列被表示为32位[十六进制](https://zh.wikipedia.org/wiki/十六进制 "十六进制")数字。以下是一个43位长的仅[ASCII](https://zh.wikipedia.org/wiki/ASCII "ASCII")字母列的MD5散列：

```text
MD5("The quick brown fox jumps over the lazy dog")
= 9e107d9d372bb6826bd81d3542a419d6
```

即使在原文中作一个小变化（比如用c取代d）其散列也会发生巨大的变化：

```纯文本
MD5("The quick brown fox jumps over the lazy cog")
= 1055d3e698d289f2af8663725127bd4b
```

空文的散列为：

```纯文本
MD5("")
= d41d8cd98f00b204e9800998ecf8427e
```
