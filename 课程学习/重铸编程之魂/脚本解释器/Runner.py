# -*- coding: utf-8 -*-
import os
import sys
current_file_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_file_directory)

from enum_helper import ExpressionType, ValueType
from VM import VM, Commands, Constants
from collections import deque
from Expression import Expression, Function, FunctionFactory
from Variable import Variable



# 解释器
class Runner(object):
    def __init__(self) -> None:
        self.commands = []
        self.vm = None
        self.constants = {}
        self.variables = {}
    
    def getConstants(self):
        return self.constants
    
    def getCommands(self):
        return self.commands

    def putCommands(self, cmd):
        self.commands.append(cmd)

class CalangRuner(Runner):
    def __init__(self, vm: VM, variables):
        self.vm = vm
        self.constants = {}
        self.commands = []
        self.variables = variables # {}
        self.vm.setConstants(self.constants)

    def translate(self, expression: Expression):
        value_type = expression.getValueType() # type: ValueType
        if value_type == ValueType.VALUE:
            expression_type = expression.getType()
            if expression_type == ExpressionType.VAR:
                self.constants[expression.getIndex()] = int(expression.getValue())
                self.vm.stackPush(self.getVariableValue(expression.getName())) # 栈顶存储了变量的值（是a、b的）
            elif expression_type == ExpressionType.FUNC:
                pass
                # TODO: 执行函数
        elif value_type == ValueType.EXPRESSION:
            expression_type = expression.getType()
            if expression_type == ExpressionType.VAR:
                self.parseExpression(expression.getValue())
                self.variables[expression.getName()].setValue(self.vm.registers[Constants.EAX_IDX])
                self.constants[expression.getIndex()] = self.vm.registers[Constants.EAX_IDX]
            elif expression_type == ExpressionType.FUNC:
                self.parseFunction(expression)
                # TODO: 执行函数

        self.vm.run(self.commands)

    def parseExpression(self, expression_str):
        symbols = deque()
        entries = expression_str.split('#')

        SYMBOLS = ['+', '-', '*', '/', '%', '(', ')']
        for entry in entries:
            if entry in SYMBOLS:
                self.pushSymbol(symbols, entry)
            else:
                self.vm.stackPush(self.getVariableValue(entry)) # 存储临时变量

        while symbols:
            symbol = symbols.pop()
            self.calc(symbol)

        # print(self.vm.getStack())
        # print(symbols)

    def parseFunction(self, expression: Expression):
        function = expression.getValue() # type: Function
        if len(function.getValues()) >= function.getNArgs():
            values = function.getValues()
            for i in range(len(values)):
                self.parseExpression(values[i])
                values[i] = self.vm.stackPop()
        function_factory = FunctionFactory.instance()
        function_factory.run(function)

    def getVariableIndex(self, entry):
        variable = self.variables.get(entry) # type: Variable
        if not variable:
            raise Exception('变量未定义')
        return variable.getIndex()
    
    def getVariableValue(self, name):
        import re
        if re.match(Constants.VARIALBLE_PATTERN, name):
            variable = self.variables.get(name) # type: Variable
            if not variable:
                raise Exception('变量未定义')
            return int(variable.getValue())
        else:
            return int(name)

    # 中缀表达式的改版
    def pushSymbol(self, symbols: list, entry):
        symbol_priority = {}
        symbol_priority['('] = 0
        symbol_priority['+'] = 1
        symbol_priority['-'] = 1
        symbol_priority['*'] = 2
        symbol_priority['/'] = 2
        symbol_priority['%'] = 2
        symbol_priority[')'] = 3
        
        if not symbols or entry == '(':
            symbols.append(entry)
            return
        
        if entry == ')':
            symbol = symbols.pop()
            while symbol != '(':
                self.calc(symbol)
                symbol = symbols.pop()
            return
        
        # 符号优先级高先入栈
        peek_one = symbols[-1]
        if symbol_priority[entry] > symbol_priority[peek_one]:
            symbols.append(entry)
        else:
            while symbols:
                # 把优先级高的先算了
                peek_one = symbols[-1]
                if symbol_priority[peek_one] >= symbol_priority[entry]:
                    symbol = symbols.pop()
                    self.calc(symbol)
                else:
                    break
            self.pushSymbol(symbols, entry)


    def calc(self, symbol):
        self.commands.append(Commands.POP | Constants.EBX_IDX << 16 | 0xFF00FF00)
        self.commands.append(Commands.POP | Constants.EDX_IDX << 16 | 0xFF00FF00)
        self.vm.run(self.commands)
        self.commands.append(Commands.MOV | self.vm.registers[Constants.EDX_IDX] << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
        if symbol == '+':
            self.commands.append(Commands.ADD | self.vm.registers[Constants.EBX_IDX] << 8 | 0xFF000000)
        elif symbol == '-':
            self.commands.append(Commands.SUB | self.vm.registers[Constants.EBX_IDX] << 8 | 0xFF000000)
        elif symbol == '*':
            self.commands.append(Commands.MUL | self.vm.registers[Constants.EBX_IDX] << 8 | 0xFF000000)
        elif symbol == '/':
            self.commands.append(Commands.DIV | self.vm.registers[Constants.EBX_IDX] << 8 | 0xFF000000)
        elif symbol == '%':
            self.commands.append(Commands.SUR | self.vm.registers[Constants.EBX_IDX] << 8 | 0xFF000000)
        self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)
        self.vm.run(self.commands)
