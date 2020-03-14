from .UnificationException import *

class Atom():
    
    def __init__(self, atoms):
        self.atoms = atoms
    
    def add(self, atom):
        self.atoms.append(atom)
        
    def unify(self, other):
        #print('Atom.Unification ' + self.toString() + ' U ' + other.toString())
        result = Atom(list())
        otherAtoms = other.clone()
        found = False
        for item1 in self.atoms:
            for item2 in otherAtoms.atoms:
                if item1 == item2:
                    result.add(item1)
                    found = True
                    break
        if found:
            return result
        else:
            raise UnificationException('*** Unification error: ' + self.toString() + ' U ' + other.toString())
        
    def clone(self):
        result = Atom(list())
        for item in self.atoms:
            result.add(item)
        return result

    def toString(self):
        result = ''
        first = True
        for item in self.atoms:
            if (first):
                first = False
            else:
                result += '|'
            result += item
        return result
    
