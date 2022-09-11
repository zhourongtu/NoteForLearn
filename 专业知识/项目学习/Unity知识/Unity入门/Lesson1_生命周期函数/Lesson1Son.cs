using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lesson1Son : Lesson1
{
    protected override void Awake()
    {
        base.Awake();
        print("子类的Awake");
    }
}
