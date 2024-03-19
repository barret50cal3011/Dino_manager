from classes.Family.Dryosauridae import Dryosauridae 

class Dyosaurus(Dryosauridae): 

    SPECIES = "dyosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"