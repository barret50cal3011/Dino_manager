from classes.BioGroups.GiantHerbivore import GiantHerbivore as GH

class Macronaria(GH):

    FAMILY = "macronaria"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)