# Head First MySQL #

## 6. 表类型的选择 ##

```mysql
# show default engine
show variables like 'default_storage_engine';

# show all support engine
show engines;
```

### 6.2 各种存储引擎的特性 ###

#### 6.2.2 InnoDB ####

**1. 自动增长列**

**2. 外键约束**

**3. 主键和索引**

InnoDB 的数据文件本身就是以聚簇索引的形式保存的，这个索引也被称为主索引，并且也是InnoDB表的主键。

**4. 存储方式**

- 使用共享表空间：这种方式结构放在 .frm 文件中，数据和索引保存在 `innodb_data_home_dir` 和 `innodb_data_file_path` 定义的表空间中。
- 使用多表空间存储： 这种方式结构放在 .frm 文件中，但是每个文件表的数据和索引单独保存在 .ibd 中。 `innodb_file_per_table`

## 7. 选择合适的数据类型 ##

### 7.1 char & varchar ###

### 7.2 text & blob ###

text & blob 值会引起一些性能问题，特别是在执行大量的删除操作时。

删除操作会在数据表中留下空洞，以后填入这些 空洞 的记录在插入的性能上会有影响。可以定期使用 `OPTIMIZE TABLE` 进行碎片整理。

```mysql
create table t (id varchar(100), context text);

insert into t values (1, repeat('haha', 100));
insert into t values (2, repeat('hehe', 100));
insert into t values (3, repeat('xixi', 100));

insert into t select * from t;
delete from t where id = 1;
optimize table t;
```

## 15. SQL优化 ##

### 15.1 一般步骤 ###

#### 15.1.1 show status 查看各种SQL执行频率 ####

```mysql
show session status like 'Com_%';
```

- Com_select: 执行select操作的次数
- Com_insert:
- Com_update:
- Com_delete:

#### 15.1.2 定位低效率的SQL语句 ####

## 16. 锁问题 ##

### 16.2 MyISAM 表锁 ###

#### 16.2.1 查询表级锁争用情况 ####

通过检查 table_locks_waited 和 table_locks_immediate 状态变量:

```mysql
show status like 'table%';
+--------------------------+-----+
|Variable_name             |Value|
+--------------------------+-----+
|Table_locks_immediate     |243  |
|Table_locks_waited        |0    |
|Table_open_cache_hits     |40   |
|Table_open_cache_misses   |5    |
|Table_open_cache_overflows|0    |
+--------------------------+-----+
```

#### 16.2.2 MySQL 表级锁的锁模式 ####

下面列出表锁的兼容性：

|           | None | Read | Write |
| --------- | ---- | ---- | ----- |
| **Read**  | :ok: | :ok: | :x:   |
| **Write** | :ok: | :x:  | :x:   |

#### 16.2.3 如何加表锁 ####

myisam在执行查询语句前，会自动给涉及的所有表加读锁。在执行更新操作前，会自动给表加写锁。

#### 16.2.4 并发插入 Concurrent Inserts ####

#### 16.2.5 MyISAM 锁调度 ####

#### 16.3 InnoDB ####

#### 16.3.1 背景知识 ####

并发事务处理带来的问题：

- 更新丢失：最后的更新覆盖了由其他事务所做的更新。
- 脏读：一个事务所做的修改还未提交，但另一个事务读取到了未提交的记录。
- 不可重复读：
- 幻读：

#### 16.3.2 获取innodb行锁争用 ####

```mysql
show status like 'innodb_row_lock%';
```

#### 16.3.3 InnoDB 的行锁模式以及加锁方式 ####

意向锁是innodb自动加的。对于 update delete insert 语句，innodb会自动给涉及数据集加排他锁，对于普通 select语句 innodb 不会加任何锁，事务可以通过 `select lock in share mode` `select for update` 给记录集加共享锁或排他锁。

#### 16.3.4 innodb行锁实现方式 ####

innodb行锁通过给索引上的索引项加锁来实现的。

- record lock
- gap lock
- next-key lock

如果不通过索引条件检索数据，那么innodb将对表中的所有记录加锁。

如果是使用相同的索引键，也会出现锁冲突的。

当表有多个索引的时候，不同的事务可以使用不同的索引锁定不同的行。

走不走索引是由MySQL来决定的，这也会影响锁冲突的情况。

还要考虑隐式的类型转换导致的索引失效。

#### 16.3.5 Next-key Lock ####

主要是影响范围查询。

主要目的是防止幻读。

innodb 如果使用相等条件请求给一个不存在的记录加锁，innodb也会使用next-key 锁。

#### 16.3.8 innodb表锁 ####

lock tables 和 autocommit 不能一起使用。

