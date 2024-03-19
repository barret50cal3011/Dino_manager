from classes.BioGroups.SmallHerbivore import SmallHerbivore as SH

class Dryosauridae(SH):

    FAMILY = "dyosauridae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)