from classes.Family.Pachycephalosauridae import Pachycephalosauridae as Pachy

class Stygimoloch(Pachy):

    SPECIES = "stygimoloch"

    def __init__(self):
        super().__init__(self.SPECIES);
        self._era = "late cretaceous"