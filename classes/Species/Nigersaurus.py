from classes.Family.Rebbachisauridae import Rebbachisauridae

class Nigersaurus(Rebbachisauridae):

    SPECIES = "nigersaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"