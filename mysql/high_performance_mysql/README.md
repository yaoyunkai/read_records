# 高性能MySQL #

## 1. MySQL架构与历史 ##

### 1.4 MVCC ###

innodb的MVCC是通过在每行记录后面保存两个隐藏的列来实现的。一个保存了行的创建时间，一个保存了行的过期时间(删除时间)。

每开始一个新的事务，系统版本号都会自动递增。事务开始时刻的系统版本号会作为事务的版本号，用来和查询到每行记录的版本号进行比较。

## 2. MySQL基准测试 ##

## 3. 服务器性能剖析 ##

## 4. Schema与数据类型优化 ##

### 4.1 选择优化的数据类型 ###

- 更小的通常更好
- 简单就好
- 尽量避免 NULL，如果计划在列上建索引，应该避免设计成为可为NULL的列

#### 4.1.1 整数类型 ####

两种类型的数字：整数 和 实数。

整数有如下类型,取值范围为：$-2^{(N-1)}$ 到 $2^{(N-1)}-1$ , 其中N表示位数

| 类型      | 存储大小(bytes) |
| --------- | --------------- |
| TINYINT   | 1               |
| SMALLINT  | 2               |
| MEDIUMINT | 3               |
| INT       | 4               |
| BIGINT    | 8               |

整数有可选的 unsigned 属性，表示不允许负值。

整数的计算一般使用64位的BIGINT整数。

#### 4.1.2 实数类型 ####

FLOAT 和 DOUBLE 类型支持使用标准的浮点运算进行近似计算。

DECIMAL类型用于存储精确的小数，可以指定小数点前后所允许的最大位数。

有多种方法可以指定浮点列所需要的精度，但会使MySQL悄悄选择不同的数据类型或者在存储时对值进行取舍，所以建议只指定数据类型，不指定精度。

| 类型    | 存储大小(bytes) |
| ------- | --------------- |
| FLOAT   | 4               |
| DOUBLE  | 8               |
| DECIMAL |                 |

mysql 在内部使用double作为内部浮点计算的类型

#### 4.1.3 字符串类型 ####

**varchar**

varchar需要一或者二字节记录字符串的长度。

适用情况：字符串的最大长度比平均长度大很多；列的更新很少。

**char**

适合存储很短的字符串，或者所有值都接近同一个长度。

**BINARY VARBINARY**

存储的是二进制字符串，也就是说存储的是字节码。

**BLOB TEXT**

为了存储很大的数据而设计，分别采用二进制和字符方式存储。

他们属于不同的数据类型家族：

字符类型: TINYTEXT SMALLTEXT TEXT MEDIUMTEXT LONGTEXT

二进制类型: TINYBLOB SMALLBLOB BLOB MEDIUMBLOB LONGBLOB

**ENUM**

mysql在内部会将每个值在列表中的位置保存位整数，并且在frm文件中保存 数字-字符串的映射关系。

枚举字段是按照内部存储的整数而不是定义的字符串进行排序的。

#### 4.1.4 日期和时间类型 ####

**datetime**

与时区无关，使用8个字节的存储空间。

**timestamp**

保存了从1970-01-01 00:00:00 以来的秒数，使用4个字节存储。

`from_unixtime()` 将timestamp转换位日期。

`unix_timestamp()` 将日期转换为unix时间戳。

timestamp显示的值依赖于时区。mysql server，op system，client 都有时区设置。

#### 4.1.5 位数据类型 ####

#### 4.1.6 选择标识符 ####

#### 4.1.7 特殊类型数据 ####

应该使用无符整数存储IP地址，而且MySQL提供了 INET_ATON 和 INET_NTOA 函数在这两种表示方法之间转换。

### 4.2 mysql schema 设计中的陷阱 ###

- 太多的列

- 太多的关联

- 全能的枚举

  ```mysql
  create table ... (country enum('','0','1',...,'31'))
  ```

  这种应该用整数作为外键关联到字典表来查找具体值。

- 变相的枚举

### 4.3 范式和反范式 ###

在范式化的数据库中，每个事实数据会出现并且只出现一次。相反，在反范式化的数据库中，信息是冗余的 (用一张表保存所有的数据)。

#### 4.3.1 范式的优点和缺点 ####

- 范式化的更新操作通常比反范式要快
- 当数据较好的范式化时，就只有很少或者没有重复数据，所以需要修改更少的数据
- 范式化的表通常更小

范式化设计的schema的缺点是通常需要关联。

#### 4.3.2 反范式的优缺点 ####

因为所有数据都在一张表中，可以很好地避免关联。

单独的表也能更有效的使用索引策略。

#### 4.3.3 混用范式化和反范式化 ####

一方面是索引带来的便利性

另一方面是更新操作代价的提高

### 4.4 缓存表和汇总表 ###

缓冲表来表示存储哪些可以比较简单地从schema其他表获取数据的表。

汇总表，保存的是使用 group by 语句聚合数据的表。

如果有一个需求要获取过去24小时准确的消息发送数量，可以设计一个每小时的汇总表，把前23个完整的小时的统计表中的拘束全部加起来，最后再加上开始阶段和结束阶段不完整的小时内的计数。

```mysql
select sum(cnt) from msg_per_hr where hr between 
	concat(left(now(), 14), '00:00') - interval 23 hour 
	and concat(left(now(), 14), '00:00') - interval 1 hour;
select count(*) from message where posted >= now() - interval 23 hour;
select count(*) from message where posted >= concat(left(now(), 14), '00:00');
```

#### 4.4.1 物化视图 ####

Flexviews

- 变更数据抓取，读取服务器的二进制日志。
- 一系列可以帮助创建和管理视图的定义的存储过程。

#### 4.4.2 计数器表 ####

假如有个计数器表，只有一行数据，记录网站的点击次数:

```mysql
create table hit_counter (cnt int unsigned not null) engine=innodb;
```

每次点击都会对计数器更新:

```mysql
update hit_counter set cnt=cnt+1;
```

对于更新操作来说，这条记录上都有一个全局的互斥锁 mutex.

可以将计数器保存在多个行中，每次随机选择一行更新:

```mysql
create table hit_counter (
	slot tinyint unsigned not null primary key,
    cnt int unsigned not null
);

update hit_counter set cnt=cnt+1 where slot = rand() * 100;
select sum(cnt) from hit_counter;
```

### 4.5 加快 alter table 操作速度 ###

## 5. 创建高性能的索引 ##

### 5.1 索引基础 ###
