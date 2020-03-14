from .Features import *

class ListFeatures():
    
    def __init__(self, list):
        self.list = list
    
    def add(self, features):
        self.list.append(features)
        
    def unify(self, other, effect):
        #print('ListFeatures.unification ' + self.toString() + ' U ' + other.toString())
        result = ListFeatures(list())
        found = False
        for item1 in self.list:
            if (other.__class__.__name__ == 'ListFeatures'):
                for item2 in other.list:
                    unif = item1.unify(item2, False)
                    if unif != None:
                        result.add(unif)
                        found = True
                        break
            elif (other.__class__.__name__ == 'Features'):
                unif = item1.unify(other, False)
                if unif != None:
                    result.add(unif)
                    found = True
            else:
                raise UnificationException('*** Internal unification error: ' + self.toString() + ' U ' + other.toString())
        if found:
            return result
        elif effect:
            raise UnificationException('*** Unification error: ' + self.toString() + ' U ' + other.toString())
        else:
            return None
        
    def clone(self):
        result = ListFeatures(list())
        for item in self.list:
            result.add(item)
        return result

    def toString(self):
        result = ''
        first = True
        for item in self.list:
            if (first):
                first = False
            else:
                result += "|"
            result += item.toString()
        return result + ''
    
