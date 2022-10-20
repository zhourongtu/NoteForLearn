参考资料：https://makefiletutorial.com/

**Makefile的基本特征**
- makefile的目标是一旦文件需要重新编译的情况下，进行`重新编译`，一般`依赖于文件被修改`。

**Makefile的语法**
``` Makefile
targets: prerequisites
    command
    command
```
- `目标是文件名`，以`空格分隔`。通常每个规则只有一个.
- 这些命令是通常用于创建目标的一系列步骤。这些需要从`制表符`开始，而`不是空格`。
- `先决条件也是文件名`，以`空格分隔`。在运行目标的命令之前，这些文件`必须存在`。这些也称为`依赖项`
> 第一个makefile的例子中，hello不存在，每一次make hello都会运行，hello存在后，则不会运行。  
> 注意：hello既是目标，也是`文件`，两个概念被连接在一起了。

- 1.找到目标
- 2.找到依赖
- 3.依赖项的修改时间晚于目标，启动编译。

**Makefile的清理(clean)**
- clean事实上是其中的一个目标
- 使用make clean完成该目标

**Makefile的变量**
- 变量只能是字符串，使用`:=`，`=`也可。