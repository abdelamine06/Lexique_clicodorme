class Atom():
    
    def __init__(self, atoms = list()):
        self.atoms = atoms
    
    def add(self, atom):
        self.atoms.append(atom)
        
    def toString(self):
        result = ''
        first = True
        for atom in self.atoms:
            if (first):
                first = False
            else:
                result += '|'
            result += atom
        return result
    
