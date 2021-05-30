## innodb_autoinc_lock_mode ##

InnoDB提供了一个可配置的锁定机制，可以显着提高使用AUTO_INCREMENT列向表中添加行的SQL语句的可伸缩性和性能。 要对InnoDB表使用AUTO_INCREMENT机制，必须将AUTO_INCREMENT列定义为索引的一部分，以便可以对表执行相当于索引的`SELECT MAX (ai_col)`查找以获取最大列值。 通常，这是通过使列成为某些表索引的第一列来实现的。

### InnoDB AUTO_INCREMENT Lock Modes ###

本节描述用于生成自动增量值的AUTO_INCREMENT锁模式，以及每种锁模式如何影响复制。自动增量锁模式是在启动时使用innodb_autoinc_lock_mode变量配置的。

以下术语用于描述 innodb_autoinc_lock_mode 设置:

- insert-like 

  所有可以向表中增加行的语句,包括`INSERT`, `INSERT ... SELECT`, `REPLACE`, `REPLACE ... SELECT`, and `LOAD DATA`.包括“simple-inserts”, “bulk-inserts”, and “mixed-mode” inserts.

- Simple inserts

  可以提前确定要插入的行数的语句(在初始处理语句时)。 这包括没有嵌套子查询的单行和多行INSERT和REPLACE语句，但不包括`INSERT ... ON DUPLICATE KEY UPDATE`。

- Bulk inserts

  事先不知道要插入的行数（和所需自动递增值的数量）的语句。 这包括`INSERT ... SELECT`，`REPLACE ... SELECT`和`LOAD DATA`语句，但不包括纯INSERT。 InnoDB在处理每行时一次为AUTO_INCREMENT列分配一个新值。

- Mixed-mode inserts

  这些是“Simple inserts”语句但是指定一些（但不是全部）新行的自动递增值。示例如下，其中c1是表t1的AUTO_INCREMENT列： 

  `INSERT INTO t1 (c1,c2) VALUES (1,'a'), (NULL,'b'), (5,'c'), (NULL,'d');`

另一种类型的 Mixed-mode inserts 是 `INSERT ... ON DUPLICATE KEY UPDATE` 其在最坏的情况下实际上是INSERT语句随后又跟了一个UPDATE，其中AUTO_INCREMENT列的分配值不一定会在 UPDATE 阶段使用。

对于 innodb_autoinc_lock_mode 有个值可以设置：

- **0: traditional**

传统的锁定模式提供了在MySQL 5.1中引入innodb_autoinc_lock_mode配置参数之前存在的相同行为。传统的锁定模式选项用于向后兼容性，性能测试以及解决“Mixed-mode inserts”的问题，因为语义上可能存在差异。

在此锁定模式下，所有“INSERT-like”语句获得一个特殊的表级AUTO-INC锁，用于插入具有AUTO_INCREMENT列的表。此锁定通常保持到语句结束（不是事务结束），以确保为给定的INSERT语句序列以可预测和可重复的顺序分配自动递增值，并确保自动递增由任何给定语句分配的值是连续的。

在statement-based replication的情况下，这意味着当在从服务器上复制SQL语句时，自动增量列使用与主服务器上相同的值。多个INSERT语句的执行结果是确定性的，SLAVE再现与MASTER相同的数据。如果由多个INSERT语句生成的自动递增值交错，则两个并发INSERT语句的结果将是不确定的，并且不能使用基于语句的复制可靠地传播到从属服务器。

```sql
CREATE TABLE t1 (
  c1 INT(11) NOT NULL AUTO_INCREMENT,
  c2 VARCHAR(10) DEFAULT NULL,
  PRIMARY KEY (c1)
) ENGINE=InnoDB;

/*
假设有两个事务正在运行，每个事务都将行插入到具有AUTO_INCREMENT列的表中。 一个事务正在使用插入1000行的INSERT … SELECT语句，另一个事务正在使用插入一行的“Simple inserts”语句:

Tx1: INSERT INTO t1 (c2) SELECT 1000 rows from another table ...  # bulk insert
Tx2: INSERT INTO t1 (c2) VALUES ('xxx');  # simple insert

*/
```

InnoDB不能预先得知有多少行会从TX1的select部分获取到,所以在事务进行过程中,InnoDB一次只会为AUTO_INCREMENT列分配一个值. 

通过一个表级锁的控制,保证了在同一时刻只有一个引用表t1的INSERT语句可以执行,直到整个INSERT语句结束,并且由不同语句生成自动递增数不会交错

只要SQL语句在从二进制日志（当使用基于语句的复制或在恢复方案中）重放时以相同的顺序执行，结果将与Tx1和Tx2首次运行时的结果相同。 因此，持续至语句结束的表级锁定( table-level locks)保证了在statement-based replication中对auto-increment列的插入数据的安全性. 但是，当多个事务同时执行insert语句时，这些表级锁定会限制并发性和可伸缩性。

在 consecutive 模式下，InnoDB可以避免为“Simple inserts”语句使用表级AUTO-INC锁，其中行数是预先已知的，并且仍然保留基于语句的复制的确定性执行和安全性。

- **1: consecutive**

在这个模式下,“bulk inserts”仍然使用AUTO-INC表级锁,并保持到语句结束.这适用于所有`INSERT ... SELECT`，`REPLACE ... SELECT`和`LOAD DATA`语句。同一时刻只有一个语句可以持有AUTO-INC锁.

“Simple inserts”（要插入的行数事先已知）通过在mutex（轻量锁）的控制下获得所需数量的自动递增值来避免表级AUTO-INC锁， 它只在分配过程的持续时间内保持，而不是直到语句完成。 不使用表级AUTO-INC锁，除非AUTO-INC锁由另一个事务保持。 如果另一个事务保持AUTO-INC锁，则“simple inserts”等待AUTO-INC锁，如同它是一个“批量插入”。

此锁定模式确保,当行数不预先知道的INSERT存在时(并且自动递增值在语句过程执行中分配)由任何“类INSERT”语句分配的所有自动递增值是连续的，并且对于基于语句的复制(statement-based replication)操作是安全的。

这种锁定模式显著地提高了可扩展性,并且保证了对于基于语句的复制(statement-based replication)的安全性.此外，与“传统”锁定模式一样，由任何给定语句分配的自动递增数字是连续的。 与使用自动递增的任何语句的“传统”模式相比，语义没有变化. 

- 2 interleaved

在这种锁定模式下,所有类INSERT(“INSERT-like” )语句都不会使用表级`AUTO-INC lock`,并且可以同时执行多个语句。这是最快和最可扩展的锁定模式，但是当使用基于语句的复制或恢复方案时，从二进制日志重播SQL语句时，这是不安全的。

在此锁定模式下，自动递增值保证在所有并发执行的“类INSERT”语句中是唯一且单调递增的。但是，由于多个语句可以同时生成数字（即，跨语句交叉编号），为任何给定语句插入的行生成的值可能不是连续的。

如果执行的语句是“simple inserts”，其中要插入的行数已提前知道，则除了“混合模式插入”之外，为单个语句生成的数字不会有间隙。然而，当执行“批量插入”时，在由任何给定语句分配的自动递增值中可能存在间隙。

### InnoDB AUTO_INCREMENT Lock Mode Usage Implications ###

- 在复制环节中使用自增列

- “Lost” auto-increment values and sequence gaps

  在所有锁定模式中，如果生成自动递增值的事务回滚，那些自动递增值将“丢失”。 一旦为自动增量列生成了值，无论是否完成“类似INSERT”语句以及包含事务是否回滚，都不能回滚。 这种丢失的值不被重用。 因此，存储在表的AUTO_INCREMENT列中的值可能存在间隙。

- Specifying NULL or 0 for the `AUTO_INCREMENT` column

  在所有锁定模式中，如果用户在INSERT中为AUTO_INCREMENT列指定NULL或0，InnoDB会将该行视为未指定值，并为其生成新值。

- Assigning a negative value to the `AUTO_INCREMENT` column

  在所有锁定模式中，如果您为AUTO_INCREMENT列分配了一个负值，则不会定义自动增量机制的行为。

- 如果AUTO_INCREMENT值大于指定整数类型的最大整数

  在所有锁定模式中，如果值大于可以存储在指定整数类型中的最大整数，则不定义自动递增机制的行为。

- Gaps in auto-increment values for “bulk inserts”

