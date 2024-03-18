from classes.MediumHerbivore import MediumHerbivore as MH

class Hadrosauridae(MH):

    FAMILY = "hadrosauridae";

    def __init__(self, i_species):
        super().__init__(i_species, self.FAMILY)