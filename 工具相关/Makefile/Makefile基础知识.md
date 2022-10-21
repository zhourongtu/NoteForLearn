参考资料：https://makefiletutorial.com/

**Makefile的基本特征**
- makefile的目标是一旦文件需要重新编译的情况下，进行`重新编译`，一般`依赖于文件被修改`。


> targets可能是多个，但是每一个都是单独处理。
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
- 变量只能是字符串，使用`:=`，`=`也可。`=`号前后跟空格。
- Makefile中变量的赋值不要使用单引号或者双引号，这都没有意义。
- 请使用`$(x)`或者`${x}`来处理字符串

**自动变量**
- `$@`是一种自动变量，包含目标名。
- `$?`：所有依赖
- `$^`：所有比目标更新的依赖。
- `$<`: 第一个依赖。

**Wildcard通配符**
> 更多的参考资料：https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html  
- `*`和`%`在Make中都是通配符。
- `*`搜索文件系统中所有符合目标的文件。
  > 建议用`wildcard`函数包裹起来
    ``` Makefile
    print: $(wildcard *.c)
      ls -la  $?
    ```
  - `*`的特点：target、prerequisites、或者wildcard function
  - 注意：不能直接用作变量声明 --> 直接认为是字符串，除非使用`wildcard`函数
- `%`通配符，不同模式有不同的含义
  - 匹配模式：`%`匹配1或多个字符。（称作桩(stem)）
  - 替换模式：匹配对应的桩，并作替换。
  - 通常用于规则定义或特定的函数。

**规则介绍**
- 隐式规则
  - 编译C程序：`n.o`会自动地从`n.c`得到，使用命令`$(CC) -c $(CPPFLAGS) $(CFLAGS) $^ -o $@`
  - 编译Cpp程序：`n.o`会自动地从`n.c` 或者 `n.cpp`得到，使用命令`$(CXX) -c $(CPPFLAGS) $(CXXFLAGS) $^ -o $@`
  - 链接单个对象文件：`n`会自动地从`n.o`得到，使用命令`$(CC) $(LDFLAGS) $^ $(LOADLIBES) $(LDLIBS) -o $@`
  - 隐式变量如下：
    - CC: Program for compiling C programs; default cc
    - CXX: Program for compiling C++ programs; default g++
    - CFLAGS: Extra flags to give to the C compiler
    - CXXFLAGS: Extra flags to give to the C++ compiler
    - CPPFLAGS: Extra flags to give to the C preprocessor
    - LDFLAGS: Extra flags to give to compilers when they are supposed to invoke the linker
- 静态模板规则
  ``` Makefile
  targets...: target-pattern: prereq-patterns ...
    commands
  ```
  > 具体参考文件LearnMakefile_3的Makefile内容。
  - 简要说明
    - 1.target-pattern用于匹配targets（每一个target都是单独编译的）。
    - 2.使用%匹配了target的字符串，此时称作`匹配好的字符串`
    - 3.通过`匹配好的字符串`，去prereq-patterns替换`%`，就是依赖的内容。
- 静态模板规则 + Filter
  - filter可以用来在静态模板规则的时候，获得正确的匹配文件。
- 模板规则
  - 两个认知
    - 自定义隐式规则的一种方式。
    - 一个比静态模板规则更简单的形式。
  - 一个简单的例子如下：定义了一个模板规则，将所有的.c文件编译为.o文件。
  ``` Makefile
  %.o : %.c
		$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
  ```
- 双引号规则
  - 双引号规则允许对一个目标有多种规则，如果只有一个引号，存在多个规则则会报错。
  ``` Makefile
  all: blah

  blah::
    echo "hello"

  blah::
    echo "hello again"
  ```
