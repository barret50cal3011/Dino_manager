from classes.Family.Nodosauridae import Nodosauridae as Nodo

class Nodosaurus(Nodo):

    SPECIES = "nodosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"