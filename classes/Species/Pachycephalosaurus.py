from classes.Family.Pachycephalosauridae import Pachycephalosauridae as Pachy

class Pachycephalosaurus(Pachy):
    
    SPECIES = "pachycephalosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late cretaceous"