from classes.Family.Hadrosauridae import Hadrosauridae

class Maiasaura(Hadrosauridae):

    SPECIES = "maiasaura"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late certaceous"