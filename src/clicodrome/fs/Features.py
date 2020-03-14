from .Feature import *

class Features():
    
    def __init__(self, list):
        self.list = list
    
    def add(self, feature):
        self.list.append(feature)
        
    # algo quadratique très moche
    def unify(self, other):
        #print('Features.unification ' + self.toString() + ' U ' + other.toString())
        otherFeatures = other.clone()
        result = Features(list())
        for item1 in self.list:
            found = False
            for item2 in otherFeatures.list:
                if item1.attr == item2.attr:
                    feature = item1.unify(item2)
                    if feature == None:
                        return None
                    else:
                        result.add(feature)
                    item2.setFlag()
                    found = True
                    break
            if (not(found)):
                result.add(item1)
        for item2 in otherFeatures.list:
            if not(item2.isFlag()):
                result.add(item2)
        return result
        
    def clone(self):
        result = Features(list())
        for feature in self.list:
            result.add(feature)
        return result

    def toString(self):
        result = "["
        first = True
        for feature in self.list:
            if (first):
                first = False
            else:
                result += ','
            result += feature.toString()
        return result + "]"
    
