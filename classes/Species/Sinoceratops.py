from classes.Family.Ceratopsidae import Ceratopsidae

class Sinoceratops(Ceratopsidae):

    SPECIES = "sinoceratops"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"