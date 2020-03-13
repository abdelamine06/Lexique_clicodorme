from .Features import *

class ListFeatures():
    
    list = list()
    
    def __init__(self, list):
        self.list = list
    
    def add(self, features):
        self.list.add(features)
        
    def toString(self):
        result = "<"
        first = True
        for item in self.list:
            if (first):
                first = False
            else:
                result += ','
            result += item.toString()
        return result + ">"
    
