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
- Inspector窗口可编辑的变量
  - 显示的可编辑内容就是脚本的成员变量（私有和保护不可编辑）
  - 私有和保护可以使用[SerializeField]强制序列化特性
    - 序列化：把一个对象保存到一个文件或者数据库字段去。
  - 公共的默认可以编辑，可以通过[HideInInspector]特性隐藏。
  - 大部分类型均可以显示编辑：int[]、List、Enum类、GameObject...
    - 字典（怎么都不行）
    - 自定义类型不行（struct、class），添加[System.Serializable]特性
  - 辅助特性
    - 分组说明特性[Header]，[Header("abc")]，增加分组
    - 悬停注释，为变量添加说说明[ToolTips]
    - 间隔特性[Space]
    - 修饰数值滑条范围[Range(min, max)]
    - 多行显示字符串[Multiline(4)]，默认3行
    - 滚动条显示字符串[TextArea(3, 4)]，最少显示3行，超过4行出现滚动条
    - 为变量添加快捷方法（参数1按钮名、参数2方法名）[ContextMenuItem("重置钱", "Test")]，右键可以重置
    - 为方法添加特性，能够在Inspector中执行[ContextMenu("行为")]，脚本旁边出现函数。
  > Inspector就是在显示成员变量，改变它为成员变量的值。脚本内、Inspector、运行时数据是不一样的，运行时也是不会修改Inspector的值的。（CopyComponent可以用于复制）
> 反射可以检测特性，Unity利用反射和特性机制实现了上述功能。
- MonoBehavior(Mono)
  - 重要成员
    - 获取依附的GameObject对象、对象位置信息、脚本是否激活。
    - 
    ``` C#
    this.gameObject
    this.transform
    this.gameObject.transform
    this.enable = false
    // 也可以获取到别人的信息
    ```
  - 重要方法
    - 得到依附对象的其他脚本
    ``` C#
    this.GetComponent(...) as ;
    ```
