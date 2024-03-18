from classes.Family.Ankilosauridae import Ankilosauridae

class Ankilosaurus(Ankilosauridae):

    SPECIES = "ankilosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"