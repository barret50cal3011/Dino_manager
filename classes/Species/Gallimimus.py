from classes.Family.Ornithomimidae import Ornithomimidae
from classes.Species.Nodosaurus import Nodosaurus
from classes.Species.Parasaurolophus import Parasaurolophus
from classes.Species.Torosaurus import Torosaurus

class Gallimimus(Ornithomimidae):

    SPECIES = "gallimimus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"

        self._likes.add(Nodosaurus.SPECIES)
        self._likes.add(Parasaurolophus.SPECIES)
        self._likes.add(Torosaurus.SPECIES)