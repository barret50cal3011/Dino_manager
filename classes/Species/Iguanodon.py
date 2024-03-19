from classes.Family.Iguanodontisae import Iguanodontidae

class Iguanodon(Iguanodontidae):

    SPECIES = "iguanodon"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"