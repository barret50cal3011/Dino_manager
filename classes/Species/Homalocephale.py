from classes.Family.Pachycephalosauridae import Pachycephalosauridae as Pachy

class Homolocephale(Pachy):

    SPECIES = "Homalocephale"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"