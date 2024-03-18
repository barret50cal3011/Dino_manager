from classes.Family.Ceratopsidae import Ceratopsidae

class Nasutoceratops(Ceratopsidae):

    SPECIES = "nasutoceratops"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"