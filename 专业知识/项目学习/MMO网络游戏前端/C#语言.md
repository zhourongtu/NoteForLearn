# 手动编译运行C#



# 关键字
- new：运算符、约束、修饰符
  - 运算符：创建对象和调用构造函数
  - 约束：泛型声明中限制泛型参数为一个类，带无参的构造函数
  - 修饰符：显示隐藏从基类继承的成员，用于在派生类和基类中相同签名的属性或方法。

## 特性
特性通过声明的方式，提供了与代码之间的联系。（提供了一系列可重用的元素），例子[Obsolete]
- 特性是一种从基类(一种tag)继承的继承的类，


- 前置：反射、泛型
  - 1.特性的介绍——使用场景、特性本质
  - 2.特性简单定义、查找、使用
  - 3.常用的特性验证类+自动特性验证


# C#核心

## 第19课：拓展方法
1. 知识点一、拓展方法基本概念
- 概念：为现有非静态 变量类型 添加 新方法
- 作用：
  - 1.提升程序拓展性
  - 2.不需要在类中重新写方法
  - 3.不需要继承来添加新方法
  - 4.为别人封装的类型写额外的方法
- 特点：
  - 1.一定是写在静态类中
  - 2.一定是一个静态函数
  - 3.第一个参数是拓展目标
  - 4.第一个参数使用this修饰
  - 5.拓展方法重名，使用原方法。
  - 6.不能为静态类拓展方法
  - 7.可以有返回值与多个参数。
2. 知识点二、基本语法
``` C#
// 访问修饰符 static 返回值 函数名(this 拓展类名 参数名, 参数类型 参数名, 参数类型 参数名, ...)
```
> 一定是静态类  
> 第一个参数使用this + 拓展类型 + 参数名
3. 知识点三、实例
``` C#
static class Tools
{
  // 为int拓展了一个成员方法
  // 成员方法 是需要 实例化对象后 才 能使用的
  // value代表 使用该方法的 实例化对象
  public static void SpeakValue(this int value)
  {
    // 拓展方法的逻辑
    Console.WriteLine("拓展的方法" + value);
  }
}
```
4. 知识点四、使用
``` C#
int i = 10;
i.SpeakValue();
```
5. 知识点五、为自定义类型拓展方法
6. 作业
  - 为整型拓展一个求平方的方法
  - 写一个玩家类，包含姓名，血量，攻击力，防御力等特征，攻击，移动，受伤等方法
  - 为该玩家类拓展一个自杀的方法。

# C#进阶

## 第3章：泛型
### 泛型
1. 知识点一、泛型是什么？
- 泛型实现了类型参数化，达到代码重用的目的
- 通过类型参数化来实现同一份代码上操作多种类型

- 泛型相当于类型占位符
- 定义类或方法时使用代替符代表变量类型
- 当真正使用了或方法时再具体指定类型
2. 知识点二、泛型分类
- 泛型类和泛型接口
- 基本语法
``` C#
class 类名<泛型占位字母>;
interface 接口名<泛型展位字母>;
```
- 泛型函数
- 基本语法：
``` C#
函数名<泛型占位字母>(参数列表)
```
- 注意：泛型占位字符可以有多个，用逗号分开
3. 知识点三、泛型类和接口
``` C#
class TestClass<T>
{
  public T value;
}
TestClass<int> t = new TestClass<int>();
interface TestInterface<T>
{
  T value{
    get;
    set;
  }
}
class Test: TestInterface<int>
{
  // public int value{
  //   get;
  //   set;
  // }
}
```
4. 知识点四、泛型方法
- 1.普通类的泛型方法
``` C#
class Test
{
  void Func<T>(T value)
  {
    // 逻辑处理
    T t = default(T);
  }
  // ... 可重载
}
```
- 2.泛型类的泛型方法
``` C#
class Test<T>
{
  public T value;
  public void TestFun(T t); // 不属于泛型方法
  public void TestFunc2<K>();
}
// 可省略不写，但不合适
Test<string> a;
a.TestFunc2("abc"); // 可以推断...
```
5. 知识点五、泛型的作用
- 1.不同类型对象的相同逻辑可以选择泛型
- 2.使用泛型可以一定程度上避免装箱拆箱
- 举例：优化ArrayList
``` C#
class ArrayList<T>
{
  private T[] array;
  ...add?
  ...?
}
```
### 泛型约束

## 第10章：反射和特性
- 编译器是一种翻译程序
- 程序集：由编译器编译得到的，用于进一步编译的中间产物。.dll，.exe。代码库文件、可执行文件。
- 元数据：用于描述数据的数据。（类、类的函数、类的变量等）
### 反射
- 反射：程序在运行时，可以查看其他程序集或自身的元数据。（函数、变量、类、对象等），实例化、执行、操作它们。  
  一个运行的程序查看本身或其他程序的元数据的行为就叫反射。
- 反射的作用：
  - 因为反射可以在编译时获得信息，提高了程序的拓展性和灵活性
  - 1.程序运行时获得元数据，包括元数据的特性。
  - 2.程序运行时，实例化对象，操作对象。
  - 3.程序运行时创建新对象，用这些对象执行任务。
``` C#
using System.Reflection;
// Type、Assembly、Activator
// Type（类的信息类）
// 它是反射功能的基础！
// 它是访问元数据的主要方式。
// 使用 Type 的成员获取有关类型声明的信息。
// 有关类型的成员（如构造方法、方法、字段、属性和类的事件）
int a = 42;
Type type = a.GetType();
Type type = typeof(int);
Type type3 = Type.GetType("System.Int32");// 类的名字，类名必须包含命名空间
type.Assembly;
// 获取一系列成员
MemberInfo[] infos = type.GetMembers();
ConstructorInfo[] ctors = t.GetConstructors(); // 获取构造函数
ConstructorInfo info = t.GetConstructor(new Type[0]); // 获取无参构造
Test my_test = info.Invoke(null) as Test; // 无参构造传null
ConstructorInfo info2 = t.GetConstructor(new Type[]{typeof(int)}); // 获取无参构造
my_test = info2.Invoke(new object[]{2});
FiledInfo[] fieldInfos = t.GetFields();
FiledInfo infoJ = t.GetField("j");
infoJ.GetValue(对象);
infoJ.SetValue(对象, value);
MethodInfo subStr = strType.GetMethod("Substring", new Type[] { typeof(int), typeof(int) });
subStr.Invoke(str_object, new object[]{1, 2});
// 反射获取和设置对象的值。
```

### 特性