class Unit:
    def __init__(self):
        self.costA = None
        self.costB = None
        self.costC = None
        self.pdg = None
        self.name = None
        self.mer_nkl = None
        self.bsse = None
    
    @property
    def vypocet_mer_nkl(self):
        _mernkl = self.costC + self.costB * self.pdg + \
                 self.costB * self.pdg * self.pdg
        
        self.mer_nkl = _mernkl
        #return _mer_nkl
        
        


        
