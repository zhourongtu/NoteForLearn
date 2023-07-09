# -*- coding: utf-8 -*-
from enum_helper import ExpressionType, ExpressionValueType, DataType
from VM import CalangVm
import re
from Variable import Variable



class Expression(object):
    def __init__(self, name, value, data_type, expression_type, index, value_type) -> None:
        self.expression_type = expression_type
        self.name = name
        self.value = value
        self.data_type = data_type
        self.index = index # VM中的局部变量表索引
        self.value_type = value_type

    def __str__(self) -> str:
        return "Expression, expression_type: {expression_type}, name: {name}, value: {value}, data_type: {data_type}".format(
            expression_type=self.expression_type,
            name=self.name,
            value=self.value,
            data_type=self.data_type
        )
    
    def getValueType(self):
        return self.value_type
    
    def getType(self):
        return self.expression_type

    def getIndex(self):
        return self.index

    def getValue(self):
        return self.value
    
    def getName(self):
        return self.name
    

def getDataType(a_symbol):
    symbol_name_2_data_type = {
        'int': DataType.INTERGER,
        'string': DataType.STRING,
    }
    return symbol_name_2_data_type.get(a_symbol, DataType.UNKNOWN)


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

        self._variables = {}

        # 用于创建表达式
        self.cur_index = 0

    def setLines(self, lines):
        self.lines = lines

    def parse(self):
        if not self.lines:
            return
        self._expressions = []
        # 创建虚拟机
        calang_vm = CalangVm(1024)
        # 创建解释器
        from Runner import CalangRuner
        calang_runner = CalangRuner(calang_vm, self._variables)

        for line in self.lines:
            # 解析表达式
            expression = self.createExpression(line)
            self._expressions.append(expression)
            # 翻译表达式
            calang_runner.translate(expression)

        # 先简单做个打印
        for expression in self._expressions:
            print(expression)

    def getValueType(self, data_type, value):
        # todo: string、int类型回头在支持
        if '#' in value:
            return ExpressionValueType.EXPRESSION
        else:
            return ExpressionValueType.VALUE

    def createExpression(self, line):
        function_factory = FunctionFactory.instance()
        trim = re.split('\s+', line.strip())
        expresstion_type = getExpressionType(line)
        
        if expresstion_type == ExpressionType.VAR:
            variable_name = trim[1]
            if len(trim) == 4:
                variable_value = trim[3]
            else:
                variable_value = '#'.join(tokenize_text(''.join(trim[3:]))) # 做特别的一个切割
            # variable添加相关变量
            variable = Variable(variable_name, len(self._variables), variable_value)
            self._variables[variable_name] = variable

            data_type = getDataType(trim[0])
            return Expression(
                name=variable.getName(),
                index=variable.getIndex(),
                value=variable_value, 
                data_type=data_type,
                value_type=self.getValueType(data_type, variable_value),
                expression_type=ExpressionType.VAR
                )
        elif expresstion_type == ExpressionType.FUNC:
            function_name_end_idx = trim[0].index('(')
            function_name = trim[0][:function_name_end_idx]
            function = function_factory.getFunction(function_name)
            
            expression_start_index = line.index('(')
            expression_end_index = line.index(')')
            value_expression_str = line[expression_start_index + 1: expression_end_index]
            
            expression_value_type = ExpressionValueType.VALUE
            try:
                int(value_expression_str)
            except:
                expression_value_type = ExpressionValueType.EXPRESSION
            return Expression(function_name, function, function.getRetType(), ExpressionType.FUNC, self.cur_index, expression_value_type)
        return None


def tokenize_text(text):
    pattern = r'(\w+|\W)'  # 匹配字母数字和非字母数字字符
    tokens = re.findall(pattern, text)

    def remove_all_elements(lst, element):
        return [x for x in lst if x != element]
    return remove_all_elements(tokens, ' ')


if __name__ == '__main__':
    print(tokenize_text('a+b'))
    print(tokenize_text('a + b'))
    print(tokenize_text('a  +  b'))
