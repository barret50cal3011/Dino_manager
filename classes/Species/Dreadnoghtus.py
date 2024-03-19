from classes.Family.Titanosauria import Titanosauria

class Dreadnoghtus(Titanosauria):

    SPECIES = "dreadnoght"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"