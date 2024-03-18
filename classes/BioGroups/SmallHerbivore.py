from classes.Dinosaur import Dinosaur as Dino

class SmallHerbivore(Dino):

    BIO_GROUP = "small herbivore"

    def __init__(self, i_species, i_family):
        super().__init__(i_species, i_family, self.BIO_GROUP);
        self._diet = "herbivore"