from classes.Family.Diplodocidae import Diplodocidae 

class Diplodocus(Diplodocidae):

    SPECIES = "diplodocus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"