# Git相关

参考资料：https://www.php.cn/manual/view/35002.html

## 1.Git的数据模型
``` python
// 文件就是一组数据
type blob = array<byte>

// 一个包含文件和目录的目录
type tree = map<string, tree | blob>

// 每个提交都包含一个父辈，元数据和顶层树
type commit = struct {
    parent: array<commit>
    author: string
    message: string
    snapshot: tree
}
type object = blob | tree | commit

objects = map<string, object>

def store(object):
    id = sha1(object)
    objects[id] = object

def load(id):
    return objects[id]
```

## 显示层
- 引用（branch）、HEAD
- 暂存区：部分处理的特性。
- 一些命令
  - help xxx、init、status、add、commit、log
  - git log --all --graph --decorate
  - git diff <filename>
  - git diff <revision> <filename>: 显示某个文件两个版本之间的差异
  - git checkout <revision>: 更新 HEAD 和目前的分支
  - branch、branch <name>、checkout -b <name>
  - merge
  - mergetool
  - rebase
  - 
