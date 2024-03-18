from classes.Ornithomimidae import Ornithomimidae

class Gallimimus(Ornithomimidae):

    SPECIES = "gallimimus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"