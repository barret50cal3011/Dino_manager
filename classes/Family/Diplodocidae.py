from classes.BioGroups.GiantHerbivore import GiantHerbivore as GH

class Diplodocidae(GH):

    FAMILY = "diplodocidae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)