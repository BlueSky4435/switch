
from operator import ne


class object:

    def __init__ (self, name, model, type):
        self.name = name
        self.model = model
        self.type = type
    
    def trax(self, neagtive):
        self.neagtive = neagtive
        print(neagtive)
