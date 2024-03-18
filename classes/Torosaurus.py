from classes.Ceratopsidae import Ceratopsidae

class Torosaurus(Ceratopsidae):

    SPECIES = "torosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"