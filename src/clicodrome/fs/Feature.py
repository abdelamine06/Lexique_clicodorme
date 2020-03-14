from .Value import *
from sqlalchemy.sql.expression import false


class Feature():
    
    def __init__(self, attr, value):
        self.attr = attr
        self.value = value
        self.flag = False
        
    def setFlag(self):
        self.flag = True
    
    def isFlag(self):
        return self.flag
    
    def unify(self, other):
        # print('Feature.unification ' + self.toString() + ' U ' + other.toString())
        value = self.value.unify(other.value);
        if value == None:
            return None
        else:
            return Feature(self.attr, value)
        
    def toString(self):
        return self.attr + ':' + self.value.toString()
    
