from classes.Family.Ceratopsidae import Ceratopsidae

class Triceratops(Ceratopsidae):

    SPECIES = "triceratos"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"