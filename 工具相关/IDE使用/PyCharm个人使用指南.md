

参考资料：https://www.jetbrains.com/help/pycharm/refactoring-source-code.html

# 整体界面介绍
- Navigation bar 导航栏
- Gutter 槽
- Project tool window 项目工具窗口
- Popup Menu 在项目工具窗口右键弹出的菜单
- Run tool window 运行工具窗口
- Python Package tool window Python的包工具窗口
- Python Console Python的控制台
- Python interpreter selector Python解释器选择
- Status Bar 状态栏
- Editor 编辑器
- Context menu 编辑器右键打开的上下文菜单
- Scrollbar 编辑器滚动条
- Notification tool Window 通知工具窗口（基本没软用）

# 1.了解编辑器(Editor)
- 参考资料：[编辑器基础](https://www.jetbrains.com/help/pycharm/using-code-editor.html)
## 编辑器结构
- Scrollbar 滑动条展示错误与警告
- breadcrumbs 面包屑导航（下侧）
- Gutter 槽显示行数与标记
- Tabs 显示当前打开的文件
## 导航功能
- Ctrl + Shift + F12 只显示编辑器
- Alt + F12 控制terminal显隐
- Ctrl + Tab 控制窗口切换。⭐⭐⭐⭐⭐
- F12 回到上一个窗口（可能是左边、下面）
- IDE外观：Ctrl+`
- 导航栏 Alt + Home

# 重构工具
- 1.ExtractMethod 提炼方法
  - 行为：命名、参数
  - 风险注意 ⭐⭐⭐⭐⭐
    - 局部变量再赋值
  - [提炼函数交叉参考](../../书籍相关/重构相关书籍/《重构》.md#61-提炼函数)
- 2.Rename 重命名
  - 变量重命名
  - 函数重命名
  - 比较靠谱 ⭐
- 3.ExtractSuperlass 提取超类
  - 超类名
  - 超类基础方法
  - 是否保留超类的继承-->多继承与超类继承。
- 4.Introduce 引入
  - 引入变量

