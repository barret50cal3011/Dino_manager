from classes.Family.Brachiosauridae import Brachiosauridae

class Brachiosaurus(Brachiosauridae):

    SPECIES = "brachiosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"