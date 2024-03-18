from classes.Family.Ceratopsidae import Ceratopsidae

class Chasmosaurus(Ceratopsidae):

    SPECIES = "chasmosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"