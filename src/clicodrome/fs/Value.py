from .Features import *
from .UnificationException import *

class Value():

    def __init__(self, val):
        self.val = val
    
    def unify(self, other):
        #print('Value.unification ' + self.toString() + ' U ' + other.toString())
        if (isinstance(self.val, (str, int, float, complex))):
            if self.val == other.val:
                return self.val
            else:
                return None
        elif (self.val.__class__.__name__ == 'Features'):
            val = self.val.unify(other.val)
            return val
        elif (self.val.__class__.__name__ == 'Atom'):
            val = self.val.unify(other.val)
            return val
        else:
            raise UnificationException('*** Unification error: unknown value')
        
    def toString(self):
       if (isinstance(self.val, str)):
           return self.val
       elif (isinstance(self.val, (int, float, complex))):
           return str(self.val)
       else:
           return self.val.toString()
        
        