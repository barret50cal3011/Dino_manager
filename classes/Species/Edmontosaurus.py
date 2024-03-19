from classes.Family.Hadrosauridae import Hadrosauridae

class Edmontosaurus(Hadrosauridae):

    SPECIES = "edmontosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"