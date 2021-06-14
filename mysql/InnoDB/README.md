# InnoDB  #

## 2. InnoDB 存储引擎 ##

### 2.3 体系架构 ###

<img src=".assets/b6ec80fe2e1ee0c8eb7af2b65f4d7136.png" alt="体系结构.png" style="zoom: 50%;" />

#### 2.3.1 后台线程 ####

- Master Thread

- IO Thread: 处理写IO请求，通过 `innodb_read_io_threads` `innodb_write_io_threads` 参数设置。

  ```
  I/O thread 0 state: wait Windows aio (insert buffer thread)
  I/O thread 1 state: wait Windows aio (log thread)
  I/O thread 2 state: wait Windows aio (read thread)
  I/O thread 3 state: wait Windows aio (read thread)
  I/O thread 4 state: wait Windows aio (read thread)
  I/O thread 5 state: wait Windows aio (read thread)
  I/O thread 6 state: wait Windows aio (write thread)
  I/O thread 7 state: wait Windows aio (write thread)
  I/O thread 8 state: wait Windows aio (write thread)
  I/O thread 9 state: wait Windows aio (write thread)
  ```

- Purge Thread: undo log ，`innodb_purge_threads`

- Page Cleaner Thread: 处理脏页

#### 2.3.2 内存 ####

**1. 缓冲池**

大小通过 `innodb_buffer_pool_size` 设置。

innodb可以有多个缓冲池实例，可以通过 `innodb_buffer_pool_instances` 设置。

查看缓冲池状态： `INFORMATION_SCHEMA.INNODB_BUFFER_POOL_STATUS`

**2. LRU list Free list Flush List**

在LRU list 中，新读取到的页，并不是直接放入到LRU list列表的首部，而是放入到LRU列表的midpoint 位置。该位置由 `innodb_old_blocks_pct` 控制。

系统变量`innodb_old_blocks_time` 用于表示页读取到mid位置后需要等待多久才会被加入到 LRU列表的热端。

当页从LRU list的old -> new ,此时发生的操作为 page_made_young

因为 `innodb_old_blocks_time` 的设置导致页没有从 old -> new 的操作为 page not made young

### 2.4 Checkpoint ###

Write Ahead Log : 当事务提交时，先写重做日志，再修改页。

假如有以下场景：如果重做日志可以无限地增大，同时缓冲池也足够大，能够缓冲所有数据库的数据，那么是不需要将缓冲池中页的新版本刷新回磁盘。

checkpoint 解决的问题：

- 缩短数据库的恢复时间
- 缓冲池不够用时，将脏页刷新到磁盘
- 重做日志(redo log)不可用时，刷新脏页。

当缓冲池不够用时，根据LRU算法会溢出最近最少使用的页，若此页为脏页，那么需要强制执行checkpoint,将脏页也就是页的新版本刷新回磁盘。

在innodb中，通过 LSN (log sequence number) 来标记版本，是一个8字节的数字。

```
Log sequence number 432376306
Log flushed up to   432376306
Pages flushed up to 432376306
Last checkpoint at  432376297
```

**checkpoint 发生的条件和时机**

种类：

- Sharp
- Fuzzy

Sharp 发生数据库关闭时。对应的参数 `innodb_fast_shutdown=1`

以下列出了 Fuzzy 可能发生的情况：

- Master thread 

  以一定的频率从缓冲池的脏页列表刷新一定比例的页到磁盘。这个过程不会阻塞用户线程

- FLUSH_LRU_LIST

  在Page Cleaner 线程进行，由于LRU list 需要保证可用的空闲页。 `innodb_lru_scan_depth`

- Async / Sync Flush

  重做日志不可用的情况，此时需要强制将一些页刷新回磁盘，脏页从脏页列表选取。保证重做日志的循环使用的可能性，也是在 Page Cleaner 线程中进行

- Dirty Page too mach

  `innodb_max_dirty_pages_pct`

### 2.5 Master Thread 工作方式 ###

早期的 main loop的逻辑：

每秒一次：

- always: redo log
- may: merge insert buffer
- may: purge dirty page

每十秒：

- may: flush dirty page
- always: merge insert buffer
- always: redo log
- always: delete undo page
- always: purge dirty page

简单地列出其逻辑：

```c
void master_thread() 
{
goto loop;

// main loop
loop:
	for (int i = 0; i < 10; i++) {
        thread_sleep(1);
        do log buffer flush to disk;
        if (last_one_second_ios < 5% innodb_io_capacity) 
            do merge 5% innodb_io_capacity insert buffer;
        if (buf_get_modified_ratio_pct > innodb_max_dirty_pages_pct) 
            do buffer pool flush 100% innodb_io_capacity dirty page;
        else if (enable adaptive flush) 
            do buffer pool flush desired amount dirty page;
        
        if (no user activity) {
            goto background loop;
        }
    }
    
    if (last_ten_second_ios < innodb_io_capacity) 
        do buffer pool flush 100% innodb_io_capacity dirty page;
    do merge 5% innodb_io_capacity insert buffer;
    do log buffer flush to disk;
    do full purge;
    
    if ( buf_get_modified_ratio_pct > 70% )
        do buffer pool flush 100% innodb_io_capacity dirty page;
    else
   		do buffer pool flush 10% innodb_io_capacity dirty page;
    goto loop;

background loop:
    do full purge;
    do merge 100% innodb_io_capacity insert buffer;
    if (not idle)
        goto loop
    else
        goto flush loop

flush loop:
    do buffer pool flush 100% innodb_io_capacity ditry page;
    if ( buf_get_modified_ratio_pct > innodb_max_dirty_pages_pct)
        goto flush loop;
    goto suspend loop
        
suspend loop:
    suspend_thread()
    waiting event
    goto loop;
    
}
```

### 2.6 关键特性 ###

- insert buffer
- double write
- adaptive hash index
- async io
- flush neighbor page

#### 2.6.1 插入缓冲 ####

在通常情况下，一张表上有多个非聚集的辅助索引 (secondary index) , 这个时候的插入情况对于非聚集索引叶子节点的插入不再是顺序的了，而需要离散地访问非聚集索引页。

而这种插入缓冲先将页放到 Insert Buffer 对象中，再以一定的频率和情况进行 Insert Buffer 和辅助索引页子节点的merge操作。

Insert Buffer 的使用需要满足：

- secondary index
- not unique index

**Insert Buffer的内部实现**

Insert buffer 是一个 B+ 树，存放再共享表空间中 ibdata1 。因此试图通过独立表空间ibd 文件恢复表中数据时，往往会导致 check table 失败，还需要进行 REPIAR TABLE 重建表上所有的辅助索引。

由叶节点和非叶节点组成。 非叶节点存放的是查询的 search key :

其构造包括三个字段：space （4 byte）+ marker（1byte） + offset（4byte） = search key （9 byte ）

​	**space**表示待插入记录所在的表空间id，InnoDB中，每个表有一个唯一的space id，可以通过space id查询得知是哪张表；

​	**marker**是用来兼容老版本的insert buffer；

​	**offset**表示页所在的偏移量。

**4. Merge Insert Buffer**

合并动作发生的情况：

- 辅助索引被读取到缓冲池中
- Insert Buffer Bitmap 页追踪到该辅助索引页以无可用空间时。
- Master Thread

#### 2.6.2 Double Write ####

先写 doublewrite buffer 再将dublewrite buffer 中的页写入各个表空间文件中。

#### 2.6.3 自适应哈希索引 ####

由innodb自动在特定条件下创建。

只能在等值得条件下命中。

### 2.7 启动，关闭，恢复 ###

关闭时，影响innodb引擎行为得参数： `innodb_fast_shutdown=1`

影响innodb恢复时得参数：`innodb_force_recovery`

## 3. 文件 ##

### 3.1 参数文件 ###

### 3.2 日志文件 ###

- 重做日志（redo log）
- 回滚日志（undo log）
- 二进制日志（binlog）
- 错误日志（errorlog）
- 慢查询日志（slow query log）
- 一般查询日志（general log）
- 中继日志（relay log）

#### 3.2.1 redo log ####

确保事务的持久性。防止在发生故障的时间点，尚有脏页未写入磁盘，在重启mysql服务的时候，根据redo log进行重做，从而达到事务的持久性这一特性。

事务开始之后就产生redo log，redo log的落盘并不是随着事务的提交才写入的，而是在事务的执行过程中，便开始写入redo log文件中。

当对应事务的脏页写入到磁盘之后，redo log的使命也就完成了，重做日志占用的空间就可以重用（被覆盖）。

之所以说重做日志是在事务开始之后逐步写入重做日志文件，而不一定是事务提交才写入重做日志缓存，原因就是，重做日志有一个缓存区`Innodb_log_buffer`，`Innodb_log_buffer`的默认大小为8M，Innodb存储引擎先将重做日志写入innodb_log_buffer中。

#### 3.2.2 undo log ####

保存了事务发生之前的数据的一个版本，可以用于回滚，同时可以提供多版本并发控制下的读（MVCC），也即非锁定读

事务开始之前，将当前是的版本生成undo log，undo 也会产生 redo 来保证undo log的可靠性.

当事务提交之后，undo log并不能立马被删除，而是放入待清理的链表，由purge线程判断是否由其他事务在使用undo段中表的上一个事务之前的版本信息，决定是否可以清理undo log的日志空间。

默认情况下undo文件是保持在共享表空间的，也即ibdatafile文件中

#### 3.2.3 bin log ####

事务提交的时候，一次性将事务中的sql语句（一个事物可能对应多个sql语句）按照一定的格式记录到binlog中。

这里与redo log很明显的差异就是redo log并不一定是在事务提交的时候刷新到磁盘，redo log是在事务开始之后就开始逐步写入磁盘。

### 3.5 表结构定义文件 ###

### 3.6 InnoDB存储引擎文件 ###

#### 3.6.1 表空间文件 ####

在默认情况下会有一个10MB名为 ibdata1的文件，该文件就是默认的表空间文件 tablespace file ，可以通过参数 `innodb_data_file_path` 进行设置。

在设置了 `innodb_data_file_path` 参数后，所有基于innodb存储引擎的表的数据都会保存在该共享表空间中。

如果设置了 `innodb_file_per_table` 那么就是使用独立表空间 `table_name.ibd`

#### 3.6.2 重做日志文件 redo_log ####

在默认情况下，在数据目录下会有两个名为 ib_logfile0 和 ib_logfile1 的文件。

下列参数影响重做日志文件的属性：

- innodb_log_file_size : 指定每个重做日志的大小
- innodb_log_files_in_group ：日志文件组中日志文件的数量
- innodb_mirrored_log_groups ：日志镜像文件组的数量
- innodb_log_group_home_dir ：日志文件组所在路径

```mysql
show variables like 'innodb\_log\_%';
```

## 4. table ##

### 4.1 索引组织表 ###

### 4.2 InnoDB 逻辑存储结构 ###

<img src=".assets/1062001-20180806105300673-894487905.png" alt="img" style="zoom:50%;" />

#### 4.2.1 tablespace ####

单独的表空间保存：数据 索引 和 insert buffer bitmap

共享的表空间保存： undo, insert buffer, 系统事务信息，doublewrite buffer，

#### 4.2.2 segment ####

数据段为树的叶子节点

非数据段为树的非索引节点

#### 4.2.3 extent ####

任何情况下每个区的大小都为1MB 。

InnoDB1.0.x版本开始引入压缩页，每个页的大小可以通过参数KEY_BLOCK_SIZE设置为2K、4K、8K，因此每个区对应的页尾512、256、128.

InnoDB1.2.x版本新增了参数innodb_page_size，通过该参数可以将默认页的大小设置为4K、8K，但是页中的数据不是压缩的。

#### 4.2.4 页 ####

在InnoDB存储引擎中，常见的页类型有：

- 数据页 B-tree Node
- undo 页 Undo Log Page
- 系统页 System Page
- 事务数据页 Transaction system Page
- Insert Buffer Bitmap
- Insert Buffer Free List
- Uncompressed BLOB Page
- compressed Blob Page

#### 4.2.5 行 ####

InnoDB 存储引擎是面向列的 (`row-oriented`)

### 4.3 InnoDB 行记录格式 ###

innoDB存储引擎提供了两种格式：`Compact` 和 `Redundant` ，默认格式为Compact行格式。

#### 4.3.1 Compact行格式 ####

在MySQL5.0 中引入，一个页中存放的行数据越多，其性能就越高。

<img src=".assets/s1.ax1x.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg" alt="img" style="zoom: 67%;" />

首部：是一个非NULL变长字段长度列表的表，并且是按照列的顺序逆序放置的，其长度：

- 若列的长度小于255字节，用一字节表示
- 若大于255字节，用两字节表示。

NULL值列表：占1个字节。

record header: 5字节，其信息如下图：

![img](.assets/20180706113144768)

最后的部分就是实际存储每个列的数据。

每行数据除了用户定义的列，还有两个隐藏列，事务ID列和回滚指针列，分别为6字节和7字节的大小。如果没有主键还会有一个隐藏的6字节的主键。

接下来使用具体的demo来查看：

```mysql
create table mytest
(
    t1 varchar(10),
    t2 varchar(10),
    t3 char(10),
    t4 varchar(10)
) engine = innodb
  charset = LATIN1
  ROW_FORMAT = COMPACT;
  
# 插入三条数据
insert into mytest values ('a', 'bb', 'cc', 'ccc');
insert into mytest values ('d', 'ee', 'ee', 'fff');
insert into mytest values ('d', NULL, NULL, 'fff');
```

此时我们可以查看mytest.idb文件：

```
0000c070  73 75 70 72 65 6d 75 6d  03 02 01 00 00 00 10 00  |supremum........|
0000c080  2c 00 00 00 0c 06 00 00  00 00 01 6e 19 b9 00 00  |,..........n....|
0000c090  01 1f 01 10 61 62 62 63  63 20 20 20 20 20 20 20  |....abbcc       |
0000c0a0  20 63 63 63 03 02 01 00  00 00 18 00 2b 00 00 00  | ccc........+...|
0000c0b0  0c 06 01 00 00 00 01 6e  1a ba 00 00 01 2f 01 10  |.......n...../..|
0000c0c0  64 65 65 65 65 20 20 20  20 20 20 20 20 66 66 66  |deeee        fff|
0000c0d0  03 01 06 00 00 20 ff 98  00 00 00 0c 06 02 00 00  |..... ..........|
0000c0e0  00 01 6e 1f bd 00 00 01  24 01 10 64 66 66 66 00  |..n.....$..dfff.|
```

真正的数据记录开始位置： 0000c078

下面列出第一个记录的数据：

```c
03 02 01 								// 变长字段长度列表
00       								// NULL 标志位
00 00 10 00 2c 							// record header
00 00 00 0c 06 00 						// row id
00 00 00 01 6e 19 						// transaction id
b9 00 00 01 1f 01 10 					// roll pointer 回滚指针
61                                      // 列1数据
62 62                                   // 列2数据
63 63 20 20 20 20 20 20 20 20           // 列3数据
63 63 63                                // 列4数据
```

第二个记录：

```c
03 02 01
00
00 00 18 00 2b
00 00 00 0c 06 01
00 00 00 01 6e 1a
ba 00 00 01 2f 01 10
64
65 65
65 65 20 20 20 20 20 20 20 20
66 66 66
```

第三个记录：

```c
03 01
06                         // 0000 0110
00 00 20 ff 98
00 00 00 0c 06 02
00 00 00 01 6e 1f
bd 00 00 01 24 01 10
64                          // 第一列数据
66 66 66                    // 第四列数据
```

#### 4.3.2 Redundant 行格式 ####

![Redundant格式](.assets/20180709154351705)

首部是一个字段长度偏移列表，也是按照列的顺序逆序放置的。

record header: 占6字节。

![redundant](.assets/20180709154809671)

同样列出以下的demo:

```mysql
create table mytest2
    engine = innodb
    row_format = redundant as
select *
from mytest;
```

接下来查看idb文件:

```
0000c070  08 03 00 00 73 75 70 72  65 6d 75 6d 00 23 20 16  |....supremum.# .|
0000c080  14 13 0c 06 00 00 10 0f  00 ba 00 00 00 0c 06 03  |................|
0000c090  00 00 00 01 6e 24 a2 00  00 01 15 01 10 61 62 62  |....n$.......abb|
0000c0a0  63 63 20 20 20 20 20 20  20 20 63 63 63 23 20 16  |cc        ccc# .|
0000c0b0  14 13 0c 06 00 00 18 0f  00 ea 00 00 00 0c 06 04  |................|
0000c0c0  00 00 00 01 6e 24 a2 00  00 01 15 01 1f 64 65 65  |....n$.......dee|
0000c0d0  65 65 20 20 20 20 20 20  20 20 66 66 66 21 9e 94  |ee        fff!..|
0000c0e0  14 13 0c 06 00 00 20 0f  00 74 00 00 00 0c 06 05  |...... ..t......|
0000c0f0  00 00 00 01 6e 24 a2 00  00 01 15 01 2e 64 00 00  |....n$.......d..|
0000c100  00 00 00 00 00 00 00 00  66 66 66 00 00 00 00 00  |........fff.....|
```

那么可以得出第一条记录的数据：

```c
23 20 16 14 13 0c 06                     // 长度偏移列表： 06 0c 13 14 16 20 23
00 00 10 0f 00 ba                        // record header
00 00 00 0c 06 03                        // row id
00 00 00 01 6e 24                        // transaction id
a2 00 00 01 15 01 10                     // roll pointer
61                                       // col1
62 62                                    // col2
63 63 20 20 20 20 20 20 20 20            // col3
63 63 63                                 // col4
```

解释一下长度偏移列表：06 0c 13 14 16 20 23

第一列长度6     (0x00+6=0x06)
第二列长度6    (0x06+6= 0x0c)
第三列长度7    (0x0c+7=  0x13)
第四列长度1    (0x13+1=   0x14)
第五列长度2    (0x14+2=  0x16)
第六列长度10  (0x16+10= 0x20)
第七列长度3   (0x20+3=  0x23)

第三条记录：

```c
21 9e 94 14 13 0c 06
00 00 20 0f 00 74
00 00 00 0c 06 05
00 00 00 01 6e 24
a2 00 00 01 15 01 2e
64  // col1
00 00 00 00 00 00 00 00 00 00  // col3
66 66 66  // col4
```

为什么从14变成了94 ???

NULL 标志的影响，最高位的标志位设为1

