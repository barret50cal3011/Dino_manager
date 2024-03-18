from classes.Dinosaur import Dinosaur as Dino

class SmallCarnivore(Dino):

    BIO_GROUP = "small carnivore"

    def __init__(self, i_species, i_family):
        super().__init__(i_species, i_family, self.BIO_GROUP)
        self._diet = "carnivore"