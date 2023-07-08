# -*- coding: utf-8 -*-
import os
import sys
current_file_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_file_directory)
import calculate_infix_expression
from collections import deque
import heapq
import re


class DataType(object):
    STRING = 1
    VOID = 2
    INTERGER = 3
    UNKNOWN = 4


def getDataType(a_symbol):
    symbol_name_2_data_type = {
        'int': DataType.INTERGER,
        'string': DataType.STRING,
    }

    return symbol_name_2_data_type.get(a_symbol, DataType.UNKNOWN)


# 实体类
class Expression(object):
    def __init__(self, name, value, data_type, expression_type) -> None:
        self._type = expression_type
        self._name = name
        self._value = value
        self._data_type = data_type

    def __str__(self) -> str:
        return "Expression, expression_type: {expression_type}, name: {name}, value: {value}, data_type: {data_type}".format(
            expression_type=self._type,
            name=self._name,
            value=self._value,
            data_type=self._data_type
        )



class ExpressionType(object):
    VAR = 1 # 变量入栈
    FUNC = 2 # 函数调用
    UNKNOWN = 3 # 未知类型


def createExpression(line):
    function_factory = FunctionFactory.instance()
    trim = re.split('\s+', line.strip())
    expresstion_type = getExpressionType(line)
    if expresstion_type == ExpressionType.VAR:
        # trim[3]做调整
        right_symbol_expression_str = ''.join(trim[3:])
        return Expression(trim[1], right_symbol_expression_str, getDataType(trim[0]), ExpressionType.VAR)
    elif expresstion_type == ExpressionType.FUNC:
        function_name_end_idx = trim[0].index('(')
        function_name = trim[0][:function_name_end_idx]
        function = function_factory.getFunction(function_name)
        return Expression(function_name, function, function.getRetType(), ExpressionType.FUNC)
    
    return None


def isFunctionType(line):
    FUNCTION_PATTERN = '[\w_]+\(.*\)'

    match_result = re.match(FUNCTION_PATTERN, line)
    if match_result:
        return True
    else:
        return False


def getExpressionType(line):
    trim = re.split('\s+', line.strip())
    if getDataType(trim[0]) != DataType.UNKNOWN:
        return ExpressionType.VAR
    elif isFunctionType(line):
        return ExpressionType.FUNC
    else:
        return ExpressionType.UNKNOWN


class Function(object):
    def __init__(self, name, n_args, arg_data_types, ret_type) -> None:
        self.name = name
        self.n_args = n_args
        self.arg_data_types = arg_data_types
        self.ret_type = ret_type

    def getRetType(self):
        return self.ret_type

    def __str__(self) -> str:
        return "Function(name: {name}, n_args: {n_args}, arg_data_types: {arg_data_types}, ret_type: {ret_type})".format(
            n_args=self.n_args,
            name=self.name,
            arg_data_types=self.arg_data_types,
            ret_type=self.ret_type
        )


class FunctionFactory(object):
    _instance = None
    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = FunctionFactory()
        return cls._instance

    def __init__(self) -> None:
        self.functions = {}

        self.print = Function('print', 1, [DataType.STRING], DataType.VOID)
        self.functions['print'] = self.print

    def getFunction(self, name):
        return self.functions.get(name, None)



class Block(object):
    def __init__(self, shortly=False) -> None:
        # 是否立即执行的
        self._shortly = shortly
        # 局部变量表
        self._local_params = {}
        # 子块
        self._sub_blocks = []
        # 表达式
        self._expressions = []

    def setLines(self, lines):
        self.lines = lines

    def parse(self):
        if not self.lines:
            return
        self._expressions = []
        # 创建虚拟机
        for line in self.lines:
            # 解析表达式
            expression = createExpression(line)
            self._expressions.append(expression)

        # 先简单做个打印
        for expression in self._expressions:
            print(expression)




# 结构类

# 解析器：将脚本文件读取到内存中，转换成一个能够识别的数据类型
class Parser(object):
    def __init__(self, file_name) -> None:
        self.root = Block(True)

        self.lines = []
        with open(file_name, 'r') as f:
            line = f.readline()
            while line:
                self.lines.append(line.strip())
                line = f.readline()

    def parse(self):
        self.root.setLines(self.lines)
        self.root.parse()


# 解释器
class Runner(object):
    def __init__(self) -> None:
        self.commands = []
        self.vm = None
        self.constants = []
    
    def CalangRuner(self, vm):
        self.vm = vm
        self.constants = []
        self.commands = []


class VM(object):
    def __init__(self) -> None:
        pass
        # 通用寄存器
        self.eax = 0
        self.ebx = 0
        self.ecx = 0
        self.edx = 0
        # eip寄存器
        self.eip = 0
        # 栈寄存器
        self.ebp = 0
        self.esp = 0
        # 标志寄存器
        self.eflags = 0
        # 栈空间
        self.stack = deque() # append、pop、[-1]栈顶，if判断空
        # 堆空间
        self.heap = [] # heapq操作它，最小堆

    # 各个指令的实现

"""
1. 流程设计
读取脚本文件（Parser）-->读取块-->表达式（函数）-->创建虚拟机-->计算表达式，计算函数-->接受结果(Runner)

2. 指令规划:
0~7、8~15、16~23、24~31
CMD、IVAL、REG1、REG2

CMD：   指令机器码
IVAL:   局部变量索引表
REG1：  操作寄存器1
REG2:   操作寄存器2

3. 指令执行过程
读取指令->执行指令->异常检测，循环

"""


"""
1. 中缀表达式计算
2. 表达式计算框架
    编译-->值（表达式）-->-->声明（常量池）、函数（调用函数）-->生成指令-->执行指令
mermaid
graph 
    
操作栈、符号栈
"""

if __name__ == "__main__":
    parser = Parser('test_file.txt')
    parser.parse()
    print('calculate_infix_expression: {}'.format(calculate_infix_expression.calculate('1 + 1')))

