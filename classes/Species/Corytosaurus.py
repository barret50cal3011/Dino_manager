from classes.Family.Hadrosauridae import Hadrosauridae

class Corytosaurus(Hadrosauridae):

    SPECIES = "corytosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"