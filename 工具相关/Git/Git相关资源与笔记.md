**Git相关**

参考资料：
https://www.php.cn/manual/view/35002.html  
《Pro Git》

# Git的数据模型
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

# Git基础知识
Git只关心文件数据的整体是否发生变化，而大多数其他系统则只关心文件内容的具体差异。
- 直接记录快照，而非差异比较
- 近乎所有操作都是本地执行
- 时刻保持数据完整性
> Git 使用 SHA-1 算法计算数据的校验和，通过对文件的内容或目录的结构计算出一个 SHA-1 哈希值，作为指纹字符串。该字串由 40 个十六进制字符（0-9 及 a-f）组成，看起来就像是：``` 24b9da6552252987aa493b52f8696cd6d3b00373 ```
- 多数操作仅添加数据
- 文件的三种状态: 已提交（committed），已修改（modified）和已暂存（staged）
- Git文件状态变化周期

## 1.了解如何配置Git。
- /etc/gitconfig Windows在安装目录。
- ~/.gitconfig Windows在用户目录下。
```
git config --global user.name "xxx"
git config --global user.email "xxx"
```
- 查看已有的配置信息
```
git config --list
git config xxx.xxx
```
- 帮助
```
git help ...
```
- 自动补全，contrib/completion 目录，会看到一个 git-completion.bash，加入.bashrc（windows自带处理）
- 别名：git config --global alias.br branch
- 忽略文件.gitignore
  - glob pattern
  - \# 或者empty会被忽略
  - 带/说明是目录
  - 以外的文件，模式前跟!
  > 所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。星号（*）匹配零个或多个任意字符；[abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；问号（?）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）。


## 2.了解如何在本地增删查改
- 增
  - 创建init、clone。增加到暂存区add。提交commit。
- 删
  - 移除暂存区git rm、取消跟踪git rm --cached、checkout、reset
  > rm：删除工作区文件。+git add，commit。删除工作区+版本库文件。
  > git rm：删除工作区文件，删除记录放入暂存区，提交后删除工作区+版本库文件。
  > 文件修改后，git rm会报错。-f。删除记录放入暂存区
  > git rm --cached：删除暂存区文件，保留工作区。
  > git 
- 查
  - 当前文件状态status、历史提交记录状态log、变化状态diff
- 改
  - 修改当前提交记录的日志(--amend)、修改分支或文件checkout [branch] [file]
- 通用标记
  - --cached：暂存区相关处理

