# -*- coding: utf-8 -*-


class Variable(object):
    def __init__(self, name, index, value) -> None:
        self.name = name
        self.index = index
        self.value = value
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
