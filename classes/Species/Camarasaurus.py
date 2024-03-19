from classes.Family.Macronaria import Macronaria

class Camarasaurus(Macronaria):

    SPECIES = "camarasaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "late jurassic"