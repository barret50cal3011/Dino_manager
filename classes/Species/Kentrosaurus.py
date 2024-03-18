from classes.Family.Stegosauridae import Stegosauridae

class Kentrosaurus(Stegosauridae):

    SPECIES = "kentrosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"