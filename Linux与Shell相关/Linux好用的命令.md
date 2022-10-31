# 命令功能系列

## 列出文件类型
- 

## 历史命令相关
- 查询历史命令：ctrl+r、ctrl+p、ctrl+n
- 重复上一条命令：方向键上+回车执行、!!回车、!-1回车执行
- history | grep， 使用!<指令序号>
- !#上一个指令名、!$上一个指令最后一个参数、!#:n上一个指令第n个参数
- 最后一个参数:!$、$_

## 移除除了某个文件类型外的所有文件
- -v参数用于反选。
``` shell
find . -type f | grep -v ".*\.png" | xargs rm
find . -type f | grep ".*\.png" | xargs rm
```

## 删除所有空文件夹
``` shell
find . -type d -empty -delete
rm -d path
rm dir
```
