from classes.Family.Stegosauria import Stegosauria

class Gigantspinosaurus(Stegosauria):

    SPECIES = "gigantspinosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"