# -*- coding: utf-8 -*-
import os
import sys
current_file_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_file_directory)
import calculate_infix_expression
from Expression import Block


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

1. 中缀表达式计算
2. 表达式计算框架
"""

if __name__ == "__main__":
    parser = Parser('test_file.txt')
    parser.parse()
    print('calculate_infix_expression: {}'.format(calculate_infix_expression.calculate('1 + 1')))

