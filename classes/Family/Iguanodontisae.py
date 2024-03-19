from classes.BioGroups.MediumHerbivore import MediumHerbivore as MH

class Iguanodontidae(MH):

    FAMILY = "iguanodontidae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)