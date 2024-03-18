from classes.BioGroups.ArmoredHerbivore import ArmorHerbivore as AH

class Ceratopsidae(AH):

    FAMILY = "ceratopsidae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)