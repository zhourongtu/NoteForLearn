参考资料：

唐老狮——Unity入门概述：https://www.taikr.com/my/course/1175

1. Unity环境搭建
2. Unity工作原理
3. Unity脚本基础
4. Unity重要组件和API
5. Unity部分核心系统

**主要学习方式**
理论+习题+实践
理论：语法操作相关知识
习题：基于知识点的针对性习题
实践：基于知识的小项目实践

**游戏引擎是什么？我们学习Unity究竟在学什么？**
专门做游戏的软件，提供了现成的功能使用，让开发游戏事半功倍。
- 降低游戏开发门槛、提升开发效率。
- 软件操作、公共API、核心系统

**Unity的工程文件的构成**
- **Assets：工程资源文件夹（美术资源、脚本等等）**（最重要）
- Library：库文件夹（Unity自动生成管理）
- Logs
- obj
- Packages（包）
- ProjectSettings（项目设置）
- Tmp

## Unity的软件操作方式
1. Layout布局
2. Scene和Hierarchy
  - Hierarchy和Scene的关系：场景内所有对象展现的不同方式。
    - 它们负责所有对象的管理：增、删、改、查。
  - 学习相关操作方式
3. Game和Project
  - Game：游戏画面窗口
  - Project：工程资源窗口
4. Inspector和Console
  - Inspector：C#脚本信息
  - Console
5. 工具栏与父子关系

## Unity工作原理（反射机制与游戏场景、预设体和资源包的导入导出）
- Unity开发的本质：在Unity引擎的基础上利用反射和引擎提供的各种功能进行的拓展开发。
  > 反射：程序在运行时，可以查看其他程序集或自身的元数据。（函数、变量、类、对象等），实例化、执行、操作它们。  
  一个运行的程序查看本身或其他程序的元数据的行为就叫反射。
- 游戏场景本质上是一个配置文件，Unity通过该配置文件，使用反射机制创建场景，展现于屏幕之中。

## Unity脚本基础
- 脚本基本规则（继承MonoBehavior的和不继承MonoBehavior的）
- 生命周期函数

