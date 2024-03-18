from classes.Family.Ornithomimidae import Ornithomimidae

class Archeornithomimus(Ornithomimidae):

    SPECIES = "archeornithomimus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"