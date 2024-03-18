from classes.Family.Hadrosauridae import Hadrosauridae as Hauro

class Parasaurolophus(Hauro):

    SPECIES = "parasaurolophus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"