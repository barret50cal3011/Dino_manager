from classes.Family.Mamenchisauridae import Mamenchisauridae 

class Mamenchisaurus(Mamenchisauridae):

    SPECIES = "mamenchisaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"