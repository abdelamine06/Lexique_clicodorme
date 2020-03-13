from .Value import *

class Feature():
    
#    attr = ""
#    value = Value()
     
    def __init__(self, attr, value):
        self.attr = attr
        self.value = value
        
    def toString(self):
        return self.attr + ':' + self.value.toString()
    