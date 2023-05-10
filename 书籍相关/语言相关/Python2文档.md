
## 3.数据模型
- Object 是Python对数据(data)的抽象，所有的数据在python程序中的表示都是对象，或对象之间的关系。
  - 从某种程度上讲，它符合冯诺依曼的“存储程序计算机模型”，代码也是由对象表示的。
- 对象、值、类型
  - 对象：数据的抽象
    - id：唯一编号
    - type：指定对象支持的操作
    - 可变对象、不可变对象
      - 不可变：num、str、tuple
      - 可变：dict、list





# 一些小知识点

### 1.Python default value is mutable
  - 当你说“Python default value is mutable”时，意思是Python函数参数的默认值是可变的。这意味着，如果一个可变对象（比如列表或字典）被用作默认值，并在函数内部被修改，这些更改将在后续调用同一函数时保留。
