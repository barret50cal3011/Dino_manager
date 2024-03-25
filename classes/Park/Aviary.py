from classes.Park.Enclosure import Enclosure
from classes.db.Species import Species

class Aviary(Enclosure):
    def __init__(self) -> None:
        super().__init__()

    def add_dinosaur(self, dinosaur: Species, amount: int):
        if(dinosaur.is_pterosaur):
            super().add_dinosaur(dinosaur, amount)