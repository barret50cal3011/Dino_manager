from classes.Family.Diplodocidae import Diplodocidae

class Apatosaurus(Diplodocidae):

    SPECIES = "apatosaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"