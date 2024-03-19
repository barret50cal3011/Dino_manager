from classes.Family.Hadrosauridae import Hadrosauridae

class Ouranosaurus(Hadrosauridae):

    SPECIES = "ouranosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"