from classes.BioGroups.MediumHerbivore import MediumHerbivore as MH

class Rhabdodontomorpha(MH):

    FAMILY = "rhabdodontomorpha"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)