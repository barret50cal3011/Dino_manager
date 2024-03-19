from classes.Family.Rhabdodontomorpha import Rhabdodontomorpha

class Muttaburrasaurus(Rhabdodontomorpha):

    SPECIES= "muttaburrasaurus"

    def __init__(self):
        super().__init__(self.SPECIES)
        self._era = "early cretaceous"