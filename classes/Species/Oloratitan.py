from classes.Family.Hadrosauridae import Hadrosauridae

class Olorotitan(Hadrosauridae):

    SPECIES = "olorotitan"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"