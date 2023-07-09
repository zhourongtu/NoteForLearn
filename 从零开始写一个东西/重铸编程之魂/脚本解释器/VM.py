# -*- coding: utf-8 -*-
from collections import deque


class Constants(object):
    FUNCTION_PATTERN = '^[A-Za-z_]\w*\(.*\)'
    VARIALBLE_PATTERN = '^[A-Za-z_]\w*'
    STRING_PATTERN = '^\"[^\"]*\"$'

    EAX_IDX = 0
    EBX_IDX = 1
    ECX_IDX = 2
    EDX_IDX = 3


class Commands(object):
    PUSH = 0x01
    POP = 0x08
    MOV = 0x03
    ADD = 0x02
    SUB = 0x04
    MUL = 0x05
    DIV = 0x06
    SUR = 0x07 # 求余


class VM(object):
    def __init__(self) -> None:
        # 通用寄存器
        # eax用于存放返回值，ebx、edx用于存放临时变量的索引
        # eax、ebx、ecx、edx
        self.registers = [0] * 4
        # eip寄存器
        self.eip = 0
        # 栈寄存器
        self.ebp = 0
        self.esp = 0 # 栈顶
        # 标志寄存器
        self.eflags = 0
        # 栈空间
        self.stack = deque() # append、pop、[-1]栈顶，if判断空
        # 堆空间
        self.heap = [] # heapq操作它，最小堆

    # 虚拟机常量池
    def setConstants(self, constants):
        self._constants = constants

    def cleanVariables(self, variables):
        variables.clear()
        self._constants.clear()

    def getStack(self):
        return self.stack

    # 各个指令的实现
    def stackPush(self, value):
        self.stack.append(value)
        self.esp += 1

    def stackPop(self):
        result = self.stack.pop()
        self.esp -= 1
        return result

    def getHeapObject(self, index):
        return self.heap[index]
    
    def setHeapObject(self, value):
        self.heap.append(value)
        return len(self.heap) - 1
    
    def run(self, commands):
        i = self.eip
        while i < len(commands):
            # 逐行读取指令
            command = commands[i]
            # 执行指令
            self.exec(command)
            # 检测异常
            self.interrupt(command)
            self.eip += 1

            i += 1

    def exec(self, command):
        used_command = command & 0x000000FF

        cmd_2_func = {
            Commands.MOV: self.cmdMove,
            Commands.PUSH: self.cmdPush,
            Commands.SUB: self.cmdSub,
            Commands.ADD: self.cmdAdd,
            Commands.MUL: self.cmdMul,
            Commands.SUR: self.cmdSur,
            Commands.POP: self.cmdPop,
        }
        cmd_2_func[used_command](command)


    def interrupt(self, command):
        pass

    def cmdPush(self, command):
        # push：将值放在栈顶
        register_index = command & 0x00FF0000
        register_index = register_index >> 16
        self.stackPush(self.registers[register_index])

    def cmdPop(self, command):
        # pop是pop到寄存器中
        register_index = command & 0x00FF0000
        register_index = register_index >> 16
        self.registers[register_index] = self.stack.pop()

    def cmdMove(self, command):
        # move 是将某个值放到寄存器中
        register_index = command & 0x00FF0000
        register_index = register_index >> 16
        import numpy
        register_index = numpy.int8(register_index)

        # 立即数？
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8
        
        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index
        
        # 先采用立即数
        param_value = local_param_index

        try:
            print('zrt_test')
            print(register_index)
            print(param_value)
            self.registers[register_index] = param_value
        except:
            print('error')

    def cmdAdd(self, command):
        # add是将特定内存中的值，加到eax寄存器中
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8

        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index
        
        param_value = local_param_index

        eax_value = self.registers[Constants.EAX_IDX]
        ret_value = eax_value + param_value
        self.registers[Constants.EAX_IDX] = ret_value

    def cmdSub(self, command):
        # add是将特定内存中的值，加到eax寄存器中
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8

        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index

        param_value = local_param_index

        eax_value = self.registers[Constants.EAX_IDX]
        ret_value = eax_value - param_value
        self.registers[Constants.EAX_IDX] = ret_value

    def cmdMul(self, command):
        # add是将特定内存中的值，加到eax寄存器中
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8

        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index

        param_value = local_param_index

        eax_value = self.registers[Constants.EAX_IDX]
        ret_value = eax_value * param_value
        self.registers[Constants.EAX_IDX] = ret_value

    def cmdDiv(self, command):
        # add是将特定内存中的值，加到eax寄存器中
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8

        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index

        param_value = local_param_index

        eax_value = self.registers[Constants.EAX_IDX]
        ret_value = eax_value / param_value
        self.registers[Constants.EAX_IDX] = ret_value

    def cmdSur(self, command):
        # add是将特定内存中的值，加到eax寄存器中
        local_param_index = command & 0xFF00
        local_param_index = local_param_index >> 8

        # TODO: 这里按照立即数先处理了
        # if local_param_index in self._constants:
        #     param_value = self._constants[local_param_index]

        # param_value = self.stack[local_param_index] if len(self.stack) > local_param_index else local_param_index

        param_value = local_param_index

        eax_value = self.registers[Constants.EAX_IDX]
        ret_value = eax_value % param_value
        self.registers[Constants.EAX_IDX] = ret_value

class CalangVm(VM):
    def __init__(self, heapSize):
        super(CalangVm, self).__init__()
        self.eip = 0
        self.registers = [0] * 4
        self.stack = deque()
        self.heap = []
