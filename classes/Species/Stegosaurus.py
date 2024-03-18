from classes.Family.Stegosauridae import Stegosauridae

class Stegosaurus(Stegosauridae):

    SPECIES = "stegosaurus"

    def __init__(self):
        super().__init__(self.SPECIES);
        self._era = "late jurassic"