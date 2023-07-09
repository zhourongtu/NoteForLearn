# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

class DataType(object):
    STRING = 1
    VOID = 2
    INTERGER = 3
    UNKNOWN = 4


class ExpressionType(object):
    VAR = 1 # 变量入栈
    FUNC = 2 # 函数调用
    UNKNOWN = 3 # 未知类型


class ValueType(object):
    VALUE = 1
    EXPRESSION = 2
