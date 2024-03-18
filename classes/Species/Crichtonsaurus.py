from classes.Family.Ankilosauridae import Ankilosauridae

class Crichtonsaurus(Ankilosauridae):

    SPECIES = "crichtonsaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"