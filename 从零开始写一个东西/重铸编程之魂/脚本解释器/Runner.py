# -*- coding: utf-8 -*-
import os
import sys
current_file_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_file_directory)

from enum_helper import ExpressionType, ExpressionValueType
from VM import VM, Commands
from collections import deque
from Expression import Expression
from Variable import Variable


class Constants(object):
    EAX_IDX = 1
    EBX_IDX = 2
    ECX_IDX = 3
    EDX_IDX = 4



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

    def translate(self, expression: Expression):
        value_type = expression.getValueType() # type: ExpressionValueType
        if value_type == ExpressionValueType.VALUE:
            expression_type = expression.getType()
            if expression_type == ExpressionType.VAR:
                self.constants[expression.getName()] = int(expression.getIndex())
                self.commands.append(Commands.PUSH | expression.getIndex() << 8 | 0xFFFF0000)
            elif expression_type == ExpressionType.FUNC:
                pass
                # TODO: 执行函数
        elif value_type == ExpressionValueType.EXPRESSION:
            expression_type = expression.getType()
            if expression_type == ExpressionType.VAR:
                self.parseExpression(expression.getValue())
                self.constants[expression.getIndex()] = int(self.vm.eax)
                self.commands.append(Commands.PUSH | expression.getIndex() << 8 | 0xFFFF0000)
            elif expression_type == ExpressionType.FUNC:
                pass
                # TODO: 执行函数

        self.vm.run(self.commands)

    def parseExpression(self, expression_str):
        symbols = deque()
        entries = expression_str.split('#')

        SYMBOLS = ['+', '-', '*', '/', '%', '(', ')']
        for entry in entries:
            if entry in SYMBOLS:
                symbols.append(entry)
            else:
                self.vm.stackPush(self.getVariableIndex(entry))

        while symbols:
            symbol = symbols.pop()
            self.calc(symbol)

        print(self.vm.getStack())
        print(symbols)

    def getVariableIndex(self, entry):
        variable = self.variables.get(entry) # type: Variable
        if not variable:
            raise Exception('变量未定义')
        return variable.getIndex()

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
            symbol = symbols.pop(-1)
            while symbol != '(':
                self.calc(symbol)
                symbol = symbols.pop(-1)
            return
        
        # 符号优先级高先入栈
        peek_one = symbols[-1]
        if symbol_priority[entry] > symbol_priority[peek_one]:
            symbols.append(entry)
        else:
            symbol = symbols.pop(-1)
            self.calc(symbol)
            self.pushSymbol(symbols, entry)

    def calc(self, symbol):
        self.commands.append(Commands.POP | Constants.EBX_IDX << 16 | 0xFF00FF00)
        self.commands.append(Commands.POP | Constants.EDX_IDX << 16 | 0xFF00FF00)
        
        if symbol == '+':
            # 含义，将edx指向的变量，移动到eax寄存器中
            self.commands.append(Commands.MOV | self.vm.edx << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
            # 加到eax当中，再存储
            self.commands.append(Commands.ADD | self.vm.ebx << 8 | 0xFF000000)
            self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)
        elif symbol == '-':
            self.commands.append(Commands.MOV | self.vm.edx << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
            self.commands.append(Commands.SUB | self.vm.ebx << 8 | 0xFF000000)
            self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)
        elif symbol == '*':
            self.commands.append(Commands.MOV | self.vm.edx << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
            self.commands.append(Commands.MUL | self.vm.ebx << 8 | 0xFF000000)
            self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)
        elif symbol == '/':
            self.commands.append(Commands.MOV | self.vm.edx << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
            self.commands.append(Commands.DIV | self.vm.ebx << 8 | 0xFF000000)
            self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)
        elif symbol == '%':
            self.commands.append(Commands.MOV | self.vm.edx << 8 | Constants.EAX_IDX << 16 | 0xFF000000)
            self.commands.append(Commands.SUR | self.vm.ebx << 8 | 0xFF000000)
            self.commands.append(Commands.PUSH | Constants.EAX_IDX << 16 | 0xFF000000)

