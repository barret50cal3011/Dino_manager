from classes.BioGroups.SmallHerbivore import SmallHerbivore as SH

class Ornithomimidae(SH):
    
    FAMILY = "ornithimimidae"

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)