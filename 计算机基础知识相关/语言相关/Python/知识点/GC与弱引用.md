
- 引用计数
- 标记-清除
- 分代机制
https://www.atjiang.com/Python2Lib-ds-weakref/
- weakref（弱引用）
``` python
  # 如果parent的生命周期cover了child的生命周期
  def AddChild(self, child):
    child.parent = weakref.proxy(self)
    self.children[name] = child
  # 如果child生命周期cover了parent的生命周期
  def AddChild(self, child):
    # child.parent = weakref.proxy(self)
    # self.children = weakref.WeakValueDictionary()
    self.children[name] = child
```