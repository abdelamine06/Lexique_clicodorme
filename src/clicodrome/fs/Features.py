from .Feature import *

class Features():
    
    features = set()
    
    def __init__(self, features):
        self.features = features
    
    def add(self, feature):
        self.features.add(feature)
        
    def toString(self):
        result = "["
        first = True
        for feature in self.features:
            if (first):
                first = False
            else:
                result += ','
            result += feature.toString()
        return result + "]"
    
