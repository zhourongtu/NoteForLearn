# -*- coding: utf-8 -*-


class Variable(object):
    def __init__(self, name, index, value) -> None:
        self.name = name
        self.index = index
        self.value = value
    
    def getName(self):
        return self.name
    
    def getIndex(self):
        return self.index
    
    def getValue(self):
        return self.value
    
