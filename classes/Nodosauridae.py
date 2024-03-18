from classes.ArmoredHerbivore import ArmorHerbivore as AH

class Nodosauridae(AH): 
    
    FAMILY = "nodosauridae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)