
![[1.工具参考资料清单#Makefile参考资料]]

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

**命令和执行**
- 打印与沉默：`命令前使用@`，或者make使用`-s`参数
- 每行的命令都在`新的 shell` 中运行（或者至少效果是这样的）
  - 同一行的两个命令可以有影响。
  - 不同行没有影响。
- 默认Shell
  ``` Makefile
  SHELL=/bin/bash

  cool:
    echo "Hello from bash"
  ```
- 得到`$`符号，使用`$$`
  - 这也是使用shell变量的一种方式。
- 错误处理
  - `-k`参数：运行，哪怕有错误。
  - `-`在一个命令前，可以抑制错误
- 取消处理
  - `ctrl+c`
- 递归使用make
  - `$(MAKE)`
  - 该标记可以传递make的标记，并且不会受到它影响。
- `export`、环境、递归make
  - `export`：直接使用变量，将该变量设为环境，所有shell command都能使用它。
- `.EXPORT_ALL_VARIABLES` exports all variables for you.
  ``` Makefile
  .EXPORT_ALL_VARIABLES:
  ...
  ```
- make的参数
  - 参考资料：https://www.gnu.org/software/make/manual/make.html#Options-Summary
  - 多目标make，按顺序。`make clean run test`

**变量第二谈**
- 变量的两种类型
  - 递归式(`=`)：仅仅当变量被使用的时候才被寻找，而不是定义的时候。
  - 简单扩展(`:=`)：只有那些到目前为止被定义的才能得到扩展。
    - 可以利用后者实现：append形式-->后一个变量依赖前一个变量的值。
    - 使用递归式则会循环错误。
  - 变量的基本定义
    - `?=`设置还未设置的变量。
    - 所有未定义的变量是空字符串
    - 使用 += 可以实现append
    - 字符串替换、文本函数、文件名函数等都有一些控制字符串的方式。
- 命令行参数 和 重写（覆盖）
  - 使用make，如`make option_one=hi`会修改`option_onw`的变量值
  - 使用`override`可以保护对应变量不被修改。
  - 可以通过`override x += -g`再进一步修改变量。
- 一系列的命令与`define`
  - 注意：`define`不是函数，但是看起来很像。
  - 注意：`define`和`endef`创建了一个分配给命令列表的变量。
    - 每一个运行都是单独的shell，和`;`隔开的表现并不一致。
- 变量可以为特定的目标赋值（或者pattern-target）
  ``` Makefile
  all: one = cool
  # %.c: one = cool

  all: 
    echo one is defined: $(one)

  other:
    echo one is nothing: $(one)
  ```

**Makefile的条件**
- if/else条件
  ``` Makefile
  foo = ok

  all:
  ifeq ($(foo), ok)
    echo "foo equals ok"
  else
    echo "nope"
  endif
  ```
- 判空
  ``` Makefile
  nullstring =
  foo = $(nullstring) # end of line; there is a space here

  all:
  ifeq ($(strip $(foo)),)
    echo "foo is empty after being stripped"
  endif
  ifeq ($(nullstring),)
    echo "nullstring doesn't even have spaces"
  endif
  ```
- 变量定义
  ``` Makefile
  bar =
  foo = $(bar)

  all:
  ifdef foo
    echo "foo is defined"
  endif
  ifndef bar
    echo "but bar is not"
  endif
  ```
- `makeflag`的知识
  - `findstring`和`MAKEFLAGS`的例子
  - make -i
    ``` Makefile
    bar =
    foo = $(bar)

    all:
    # Search for the "-i" flag. MAKEFLAGS is just a list of single characters, one per flag. So look for "i" in this case.
    ifneq (,$(findstring i, $(MAKEFLAGS)))
      echo "i was passed to MAKEFLAGS"
    endif
    ```

**函数**
- 第一个函数（替换文本）
  ``` Makefile
  comma := ,
  empty:=
  space := $(empty) $(empty)
  foo := a b c
  bar := $(subst $(space),$(comma),$(foo))

  all: 
    @echo $(bar)
  ```
- 模式替换文本
  - `$(patsubst pattern,replacement,text)`
  - 速记方式1：`$(text:pattern=replacement)`，去掉了`patsubst`
  - 速记方式2（尾缀）：可以去掉`%`，`$(text:suffix=replacement)`
- 遍历函数
  - `$(foreach var,list,text)`
- if函数
  - 判断第一个参数是不是空
  ``` Makefile
  foo := $(if this-is-not-empty,then!,else!)
  empty :=
  bar := $(if $(empty),then!,else!)

  all:
    @echo $(foo)
    @echo $(bar)
  ```
- 调用函数
  - 通过定义一个小函数，使用参数做这样的替换。
  ``` Makefile
  sweet_new_fn = Variable Name: $(0) First: $(1) Second: $(2) Empty Variable: $(3)

  all:
    # Outputs "Variable Name: sweet_new_fn First: go Second: tigers Empty Variable:"
    @echo $(call sweet_new_fn, go, tigers)
  ```
- Shell函数
  - 调用shell，使用空格替换新行。
  ``` Makefile
  all: 
	@echo $(shell ls -la) # Very ugly because the newlines are gone!
  ```

**其他特性**
- 包含makefile
  ``` Makefile
  include filenames
  ```
- 相对路径：`vpath <pattern> <directories, space/colon separated>`
  - pattern中可以有`%`，匹配0或多个字符。
  ``` Makefile
  vpath %.h ../headers ../other-directory

  some_binary: ../headers blah.h
    touch some_binary

  ../headers:
    mkdir ../headers

  blah.h:
    touch ../headers/blah.h

  clean:
    rm -rf ../headers
    rm -f some_binary
  ```
- 多行，使用`\`
- 假目标，使目标不和文件实际联系起来。
  - `.phony`
  ``` Makefile
  .PHONY: clean
  ```
- `DELETE_ON_ERROR`标记
  - 当错误发生时，删除规则对应的文件
