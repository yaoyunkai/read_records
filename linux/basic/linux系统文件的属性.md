Linux 系统文件的属性
==========

tail -f 文件被移走或者删除了，需要重新进行追踪
tail -F 文件被移走或者删除了，不需要重新进行追踪，只要文件恢复会继续追踪。

```bash
[root@mylnx ~]# ls -li
total 8
 67156866 -rw-------. 1 root root 1989 Jul 10 23:52 anaconda-ks.cfg
    83659 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Desktop
    83660 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Documents
 34265551 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Downloads
 67156891 -rw-r--r--. 1 root root 2037 Jul 10 23:53 initial-setup-ks.cfg
 34265556 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Music
 67417642 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Pictures
100673834 drwxr-xr-x. 5 root root   61 Jul 11 17:33 projects
100672847 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Public
 67417641 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Templates
100672848 drwxr-xr-x. 2 root root    6 Jul 10 23:59 Videos
```

**利用命令区分文件类型** `file`

**链接的创建方式** `ln -s /src dest`

### linux 常见的文件类型

"d" ---- 目录文件

"-" ---- 普通文件

"c/b" ---- 块文件/字符文件

"s" ---- socket文件

