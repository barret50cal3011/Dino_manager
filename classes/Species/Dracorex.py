from classes.Family.Pachycephalosauridae import Pachycephalosauridae as Pachy
from classes.Species.Nodosaurus import Nodosaurus

class Dracorex(Pachy):

    SPECIES = "dracorex"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"
        
        self._likes.add(Nodosaurus.get_species())