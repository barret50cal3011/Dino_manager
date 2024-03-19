from classes.Family.Dicraeosauridae import Dicraeosauridae

class Amargosaurus(Dicraeosauridae):

    SPECIES = "amargosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"