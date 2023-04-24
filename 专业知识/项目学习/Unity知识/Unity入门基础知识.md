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
- MonoBehavior(Mono)（可以通过点进去查看）
  - 重要成员
    - 获取依附的GameObject对象、对象位置信息、脚本是否激活。
  - 重要方法
    - 得到依附对象的其他脚本GetComponent

## Unity的重要组件和API
1. GameObject
  > 增删查（static、成员变量）改（成员方法）系列
  - 成员变量（this.gameObject.xxx)
    - .name(可改)、.activeSelf、.isStatic、.layer、.tag(字符串)、.transform
  - 静态方法（点进去看，搜public static，进一步再查看Unity的Object）
    - GameObject：CreatePrimtive(...)、Find、Tag...（+s可以查找多个）
      > 注意：找不到失活的对象，查找单个对象不确定
    - Object：
      - 查找某一个脚本对象、...
      - 实例化对象（克隆）（**1.场景中的一个对象**、**2.预制体对象（主要）**）
      - 删除一个对象（也可以删除脚本，可以删除很多东西）
      > Destroy不会马上移除（只是加了个移除标志），一般情况下，下一帧时会移除。（降低卡顿）  
      > 也可以选择马上移除
    > 查找方法中，一个是查找GameObject，一个是查找脚本对象，查找效率都都不高，后者更低。  
    > 继承Mono可以不打GameObject调用静态方法
    - 默认切场景时，移除对象，如果过场景不被消除，可以使用DontDestroyOnLoad
  - 成员方法（点进去看）
    - 重要成员方法
      - 创建空物体
      - 为对象添加脚本AddComponent
      - 得到脚本（与Mono相同）
      - 标签比较
      - 设置激活失活 SetActive
    - 次要（不建议，效率低）
      - 广播或者消息，让别人或者自己 执行某个行为 SendMessage("func_name")（使用反射）
      - BroadcastMessage.. 自己和子对象
      - SendMessageUpwards 自己和父对象
2. Time
  - 时间相关内容 主要 用于游戏中参与位移、记时、时间暂停等。
  - 1.时间缩放比例（可以查看static变量）
    - Time.timescale = 0
    - Time.timescale = 1
    - Time.timescale = 2
    - 影响相关时间
  - 2.帧间隔时间：最近的一帧用了多长时间（秒）
    > 主要用于计算位移，路程 = 时间*速度
    - Time.deltaTime
    - Time.unscaledDeltaTime
    > 帧率高会使CPU压力大等
  - 3.游戏开始到现在的时间
    > 它主要用来计时 单机游戏中计时间（网络游戏使用服务器时间）
    - Time.time
    - Time.unscaledTime
  - 4.物理帧时间
    - Time.fixedTDeltaTime
    - Time.fixedUnscaledDeltaTime
  - 5.帧数
    > 从开始到现在游戏跑了多少帧（次循环）
    - Time.frameCount
  - 物理间隔时间设置：edit、project setting、time部分
3. Transform
  - 主要用来做什么？游戏对象（GameObject）的**位移、旋转、缩放、父子关系、坐标转换**等都由它处理。 （极其重要⭐⭐⭐⭐⭐）
  - Vector3：表示三维坐标中的一个点或者方向（向量）。
  - **世界**坐标系：.position
    - Inspector显示：相对坐标位置，localPosition
    - 位置（position）只能整体改变
    - 注意：可以先取出来Vector3再赋值，再赋回去。
  - 对象朝向：.forward、.back、.up、down、right、left
    - 从transform点出来的
  - **位移**：方向、速度、时间
    - s = vt
  - 角度 和 旋转

### 4.MonoBehavior的重要内容
#### 4.1 延迟函数
#### 4.2 协同程序
- 知识点一 Unity是否支持多线程？
  - Unity是支持多线程的，但是新开线程**无法访问Unity相关对象**的内容
    - 要注意关闭Unity中的多线程（避免共生，比如在OnDestroy的时候关闭线程）。
    > 利用共同内存区域，来使用多线程。
- 知识点二 协同程序是什么？
  - 简称协程
  - 它是“假”的多线程，它不是多线程
  - 它的主要作用：将代码分步、分时执行，不卡主线程。
  - 主要使用场景：异步加载文件、异步下载文件、场景异步加载、批量创建时防止卡顿
- 知识点三 协同程序和线程的区别
  - 新开一个线程是独立的一个管道，和主线程并行执行
  - 新开一个协程是在原线程之上开启，进行逻辑分时分布执行
- 知识点四 协程的使用
  - yield return xxxx（时机设计）
- 知识点五 开启协程与关闭协程的方法
- 知识点六 协程受对象和组件失活的影响
  - 协程开启后，组件和物体销毁，协程不执行
  - 物体失活协程不执行，组件失活协程执行
#### 4.3 协同程序原理（协程）
- 知识点一 协程的本质
  - 协程可以分为两部分
    - 1.协程函数本体
    - 2.协程调度器

  - 协程本体就是一个能够中间暂停返回的函数
    > 交叉参考：[协程概念](..\..\..\计算机基础知识相关\概念知识\基础概念辨析.md#协程)
  - 协程调度器是Unity内部实现，会在对应的时机帮助我们继续执行协程函数

  - Unity只实现了协程调度部分
  - 协程的本质就是一个C#的迭代器方法
- 知识点二 协程本体是迭代器方法的体现
  - 写一个C#的迭代器函数，并使用它
  - 理解Unity的协程调度器
    - 遵循Unity的规则

``` C#
IEnumerator Test()
{
  yield return 1;
  yield return 2;
  ...
}
IEnumerator ie = Test();
// 具体方法 current、moveNext、reset
```
