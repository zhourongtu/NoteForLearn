import ply.lex as lex

# 定义token列表
tokens = (
    'ID',
    'PLUS',
    'MINUS',
    'NUMBER',
)

# 定义token的正则表达式模式
t_PLUS = r'\+'
t_MINUS = r'\-'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

# 忽略空格和制表符
t_ignore = ' \t'

# 处理换行符
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 错误处理函数
def t_error(t):
    print("非法字符：%s" % t.value[0])
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()

# 输入要进行token划分的文本
text = 'a + 10'

# 将文本输入词法分析器
lexer.input(text)

# 逐个获取token并输出
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
