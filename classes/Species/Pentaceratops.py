from classes.Family.Ceratopsidae import Ceratopsidae

class Pentaceratops(Ceratopsidae):

    SPECIES = "pentaceratops"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"