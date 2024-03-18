from classes.Family.Ornithomimidae import Ornithomimidae

class Struthiomimus(Ornithomimidae):

    SPECIES = "struthiomimus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"