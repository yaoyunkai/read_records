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

#### 5.1.1 索引的类型 ####

**B-Tree**

根节点的槽中存放了指向子节点的指针，存储引擎根据这些指针向下查找，通过比较节点页的值和要查找的值可以找到合适的指针进入下层子节点。

可以使用b-tree索引的查询类型，全键值，键值范围，和键前缀查找(根据最左前缀的查找):

假如有如下表：

```mysql
create table people (
	last_name 		varchar(50) 	not null,
    first_name 		varchar(50) 	not null,
    dob         	date 			not null,
    gender      	enum('m', 'f')  not null,
    key `demo_key` (last_name, first_name, dob) 
);
```

- 全值匹配：和索引中的所有列进行匹配，查询 姓名位 Cuba Allen 出生于1960-01-01 的人
- 匹配最左前缀：只使用索引的第一列，查找姓位 allen 的人
- 匹配列前缀: 只使用了索引的第一列，查找所有以J开头的姓的人
- 匹配范围值：只使用了索引的第一列，可用于查找姓在 Allen 和 barry 之间的人。
- 精确匹配某一列并范围匹配另一列：用于查找所有姓为 allen , 并且名字是 K开头的人，即第一列全匹配，第二列范围匹配。
- 只访问索引的查询(覆盖索引):

因为btree中的节点是有序的，所以除了按值查找外，还可以用于查询中的 ORDER BY 操作。

下面是一些关于b-tree索引的限制：

- 必须按照索引的最左列开始查找。

- 不能跳过索引中的列，例如不能用于查找姓为tom并且在某个日期出生的人，如果不指定first name，则MySQL只能使用索引的第一列。

- 如果查询中有某个列的范围查询，则其邮编所有列都无法使用索引优化查找。

  ```mysql
  where last_name = 'Smith' and first_name like 'J%' and dob = '1976-09-23';
  ```

  上面的查询只能使用索引的前两列。

**哈希索引**

只能用于精确匹配索引所有列的查询才有效。

- 哈希索引只包含哈希值和行指针，不能使用索引中的值来避免读取行
- 哈希索引不是按照顺序存储的，无法用于排序
- 不支持部分索引列匹配查找
- 哈希索引只支持等职比较查询 `=` `in()` `<=>` 

### 5.2 索引的优点 ###

### 5.3 高性能的索引策略 ###

#### 5.3.1 独立的列 ####

索引列不能是表达式的一部分，也不能是函数的参数：

```mysql
select actor_id from sakila.actor where actor_id + 1 = 5;
select ... where to_days(current_data) - to_days(date_col) <= 10;
```

#### 5.3.2 前缀索引和索引选择性 ####

可以仅索引列开始的部分字符，这样可以节约索引空间，但是也会降低索引的选择性，值的是不重复的值。

计算合适的前缀长度的另一个方法就是计算完整列的选择性，并使用前缀的选择性接近于完整列的选择性。

```mysql
# 计算完整列的选择性
select count(distinct city) / count(*) from city;
select count(distinct left(city, 3)) / count(*) as sel3;
```

假如找到了合适的前缀长度，那么怎么创建索引呢：

```mysql
alter table city add key `prefix_city` (city(7));
```

#### 5.3.3 多列索引 ####

在多个列上建立独立的单列索引大部分情况下并不能提高MySQL的查询性能。

*如果在explain中看到有索引合并*。

例如：

```mysql
# 在 film_id actor_id 上各有一个单列索引
select film_id, actor_id from film_actor where actor_id = 1 or film_id = 1;
```

or条件的联合，and条件的相交，组合前两种情况的联合及相交。

索引合并策略有时候是一种优化的结果，但实际上更多时候说明了表上的索引建的不完美：

- 当服务器对多个索引做相交操作时，表示需要一个包含所有相关列的多列索引

#### 5.3.4 选择合适的索引顺序 ####

正确的顺序依赖于使用该索引的查询，并且同时需要考虑如何更好满足排序和分组的需要。

通常将选择性最高的列放到索引最前列。

当不需要考虑排序和分组时，将选择性最高的列放在前面通常时很好的。作用只是用于优化where条件的查找。性能不只是依赖于所有索引列的选择性，也是查询条件的具体值有关，和值的分布有关。

#### 5.3.5 聚集索引 ####

primary key

#### 5.3.6 覆盖索引 ####

innodb的二级索引在叶子节点中保存了行的主键值，所以如果二级主键能够覆盖查询，则可以避免对主键索引的二次查询。

explain: extra: using index

#### 5.3.7 使用索引扫描排序 ####

如果explain出来的type列的值为 index，则说明mysql使用了索引扫描来做排序。

如果索引不能覆盖查询所需的全部列，那就不得每扫描一条记录就都回表查询一次对应的行，这基本都是随机IO。因此按索引顺序读取数据的速度通常要比顺序地全表扫描慢。

只有当索引的列顺序和 ORDER BY 子句的顺序 完全一致，并且所有列的排序方向都一样时，MySQL才能使用索引来对结果做排序。

还有一种情况下 ORDER BY 子句可以不满足索引的最左前缀的要求，就是前导为常量的时候。

```mysql
# rental_data, inventory_id, customer_id --> index
select rental_id, staff_id, from rental where rental_date = '2005-05-25' order by  inventory_id, customer_id;
```

#### 5.3.9 冗余和重复索引 ####

重复索引是指在相同的列上按照相同的顺序创建的相同类型的索引。

#### 5.3.11 索引和锁 ####

### 5.4 索引案例学习 ###

#### 5.4.1 支持多种过滤条件 ####

#### 5.4.2 避免多个范围条件 ####

#### 5.4.3 优化排序 ####

### 5.5 维护索引和表 ###

## 6. 查询性能优化 ##

### 6.2 慢查询基础：优化数据访问 ###

1. 确认应用程序是否在检索大量超过需要的数据。
2. 确认MySQL服务器层是否在分析大量超过需要的数据行。

#### 6.2.1 是否向数据库请求了不需要的数据 ####

- 查询不需要的记录
- 多表关联时返回全部列
- 总是取出全部列
- 重复查询相同的数据

#### 6.2.2 MySQL是否在扫描额外的记录 ####

- 响应时间
- 扫描的行数
- 返回的行数

**响应时间**

了解这个查询需要哪些索引以及它的执行计划是什么，然后计算大概需要多少个顺序和随机IO, 再用其乘以在具体硬件条件下 一次IO的消耗时间。

**扫描的行数和返回的行数**

**扫描的行数和访问类型**

在explain语句中的type列反应了访问类型。其中有扫描表，扫描索引，范围访问和单值访问的概念。

一般MySQL能够使用如下三种方式应用 where 条件，从好到坏依次为：

- 在索引中使用where条件来过滤不匹配的记录，在存储引擎层完成。
- 使用索引覆盖扫描(在extra列中出现了using index)来返回记录，直接从索引中过滤不需要的记录并返回命中的结果，在mysql层完成。
- 从数据表中返回数据，然后过滤不满足条件的记录(在 extra列中出现using where)，在mysql层完成。

### 6.3 重构查询的方式 ###

#### 6.3.2 切分查询 ####

删除旧的数据就是一个很好的例子。

```mysql
row_affected = 0
do {
	rows_affected = do_query('delete from messages where created < data_sub(now(), interval 3 month)' limit 10000)
} while rows_affected > 0
```

#### 6.3.3 分解关联查询 ####

如下的优势：

- 让缓存的效率更高。
- 将查询分解后，执行单个查询可以减少锁的争用
- 在应用层关联

### 6.4 查询执行基础 ###

#### 6.4.1 MySQL客户端/服务器通信协议 ####

**查询状态**

使用 `show full precesslist` 查看当前的状态

- sleep: wait clent send request
- query: 线程正在执行查询或者正在将结果发送给客户端
- locked: 在MySQL服务器层，该线程正在等待表锁
- analyzing and statistics: 线程正在收集存储引擎的统计信息
- copying to tmp table [on disk]
- sorting result
- sending data

#### 6.4.2 查询缓冲 ####

#### 6.4.3 查询优化处理 ####

**查询优化器**

MySQL使用基于成本的优化器，他将尝试预测一个查询使用某种执行计划时的成本，并选择其中成本最小的一个。

可以通过查询当前会话的 `Last_query_cost` 的值来得知MySQL计算的当前查询的成本。

MySQL能够处理的优化类型：

- 重新定义关联表的顺序
- 将外连接转化成内连接
- 使用等价变换规则
- 优化 COUNT() MIN() MAX()
- 预估并转化为常数表达式
- 覆盖索引扫描
- 子查询优化
- 提前终止查询

### 6.5 MySQL查询优化器的局限性 ###

## 7. MySQL高级特性 ##

## 8. 优化服务器配置 ##

### 8.1 MySQL配置的工作原理 ###

对于查找配置文件的路径：

```console
which mysql
/usr/sbin/mysqld --verbose --help | grep -A 1 'Default options'
```

#### 8.1.1 语法，作用域和动态性 ####

