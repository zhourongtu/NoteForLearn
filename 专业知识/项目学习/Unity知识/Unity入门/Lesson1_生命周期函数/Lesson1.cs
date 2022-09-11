using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lesson1 : MonoBehaviour
{
    #region 知识点一 了解帧的概念
    //Unity 底层已经帮助我们做好了死循环
    //我们需要学习Unity的生命周期函数
    //利用它做好的规则来执行我们的游戏逻辑就行了
    #endregion

    #region 知识点二 生命周期函数的概念
    //所有继承MonoBehavior的脚本 最终都会挂载到GameObject游戏对象上
    //生命周期函数 就是该脚本对象依附的GameObject对象从出生到消亡整个生命周期中
    //会通过反射自动调用的一些特殊函数

    //Unity帮助我们记录了一个GameObject对象依附了哪些脚本
    //会自动的得到这些对象，通过反射去执行一些固定名字的函数
    #endregion

    #region 知识点三 生命周期函数
    //注意：
    //生命周期函数的访问修饰符一般为private和protected
    //因为不需要再外部自己调用生命周期函数 都是Unity自己帮助我们调用的

    //当对象（自己这个类对象）被创建时 才会调用该生命周期函数
    //类似构造函数的存在 我们可以在一个类对象 该创建 进行一些初始化操作
    protected virtual void Awake()
    {
        //在Unity中打印信息的两种方式
        //1. 没有继承MOnoBehavior类的时候
        //Debug.Log("123");
        //Debug.LogError("出错了！！！！！");
        //Debug.LogWarning("警告！！！");
        //2. 继承了MonoBehavior 有一个线程的方法 可以使用
        print("Awake");
    }

    //对于我们来说 想要当一个对象被激活时 进行一些逻辑处理 就可以写在这个函数
    void OnEnable()
    {
        print("OnEnable");
    }

    //主要作用还是用于初始化信息的 但是它相对Awake来说 要晚一点
    //因为它是在对象 进行第一次帧更新之前才会执行的
    void Start()
    {
        print("Start");
    }
    
    //它主要是用于 进行物理更新 
    //它是每一帧的执行的 但是 这里的帧 和游戏帧 有点不同
    //它的时间间隔 是可以在 project setting中的 Time里去设置的
    void FixedUpdate()
    {
        print("FixedUpdate");
    }

    //主要用于处理游戏核心逻辑更新的函数
    void Update()
    {
        print("Update");   
    }

    //一般这个更新是用来处理 摄像机位置更新相关内容的
    //Update和LateUpdate之间 Unity进了一些处理 处理我们动画相关的更新
    void LateUpdate()
    {
        print("LateUpdate");
    }

    //如果我们希望在一个对象失活时做一些处理 就可以在该函数中写逻辑
    void OnDisable()
    {
        print("OnDisable");    
    }

    void OnDestroy()
    {
        print("OnDestroy");    
    }

    #endregion

    #region 知识点四 生命周期函数 支持继承多态

    #endregion
}

//总结
//这些生命周期函数 如果你不打算在其中写逻辑 那就不要在这些出生命周期函数
