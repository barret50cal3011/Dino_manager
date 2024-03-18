from classes.Family.Nodosauridae import Nodosauridae

class Polacanthus(Nodosauridae):

    SPECIES = "polacanthus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"