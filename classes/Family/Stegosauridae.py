from classes.BioGroups.ArmoredHerbivore import ArmorHerbivore as AH

class Stegosauridae(AH):

    FAMILY = "stegosauridae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)