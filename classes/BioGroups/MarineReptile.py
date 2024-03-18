from classes.Dinosaur import Dinosaur as Dino

class MarineReptile(Dino):

    BIO_GROUP = "marine reptile"

    def __init__(self, i_species, i_family):
        super().__init__(i_species, i_family, self.BIO_GROUP)
        self._diet = "pisivore"