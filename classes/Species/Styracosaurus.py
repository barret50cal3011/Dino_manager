from classes.Family.Ceratopsidae import Ceratopsidae

class Styracosaurus(Ceratopsidae):

    SPECIES = "styracosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"