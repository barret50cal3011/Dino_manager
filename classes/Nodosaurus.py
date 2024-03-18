from classes.Nodosauridae import Nodosauridae as Nodo

class Nodosaurus(Nodo):

    SPECIES = "nodosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)