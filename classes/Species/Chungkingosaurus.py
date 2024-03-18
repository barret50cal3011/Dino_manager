from classes.Family.Hauyangosauridae import Hauyangosauridae

class Chungkingosaurus(Hauyangosauridae):
    
    SPECIES = "chungkingosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"