参考资料：唐老狮——https://www.taikr.com/course/1154/task/36588/show

**什么是数据持久化**
游戏运行时的变量数据存在内存中，把数据保存到内存中，就叫数据存储化。

**主要学习内容**
- PlayerPrefs的基本方法
- PlayerPrefs在不同平台的存储位置
- 利用反射结合PlayerPrefs制作通用存储工具

**学习目的**
1. 熟练使用PlayerPrefs存储读取相关的API
2. 感受反射在实际应用中的作用
3. 掌握反射结合PlayerPrefs制作通用存储工具的方法


## PlayerPrefs基本知识
- PlayerPrefs是什么？是Unity提供的可以用于存储读取玩家数据的公共类。
  - 直接点进去查看就能明白。
- 存储相关
  - PlayerPrefs的数据存储 类似于键值对存储 一个键对应一个值
  - 提供了存储三种数据的方法 int float string
  - 键：string类
  - 值：int float string 对应三种API
``` C#
PlayerPrefs.SetInt("myAge", 18); // 到内存中
PlayerPrefs.SetFloat("myHeight", 1.11f);
PlayerPrefs.SetString("myName", "奇葩");
PlayerPrefs.SetString("myAge", "abc"); // 同名覆盖
// 游戏结束会存储
PlayerPrefs.Save();
```
- 读取相关
``` C#
PlayerPrefs.GetInt("myAge");
PlayerPrefs.HasKey("myName"); // 判断键是否重复比较有用
```
- 删除
``` C#
PlayerPrefs.DeleteKey("myAge");
PlayerPrefs.DeleteAll();
```