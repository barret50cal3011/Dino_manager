from classes.BioGroups.ArmoredHerbivore import ArmorHerbivore as AH


class Hauyangosauridae(AH):

    FAMILY = "hauyangosauridae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)