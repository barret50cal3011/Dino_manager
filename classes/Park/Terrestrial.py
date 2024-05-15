from classes.Park.Enclosure import Enclosure
from classes.db.Species import Species

class Terrestrial(Enclosure):
    def __init__(self) -> None:
        super().__init__("Terrestrial")

    def add_dinosaur(self, dinosaur: Species, amount: int):
        if(dinosaur.is_terrestrial()):
            super().add_dinosaur(dinosaur, amount)