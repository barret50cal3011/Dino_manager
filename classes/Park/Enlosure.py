from classes.db.Species import Species

class Enclosure:

    def __init__(self) -> None:
        self._dinosaurs = {}

    def add_dinosaur(self, dinosaur: str, amount: int):
        if dinosaur in self._dinosaurs:
            self._dinosaurs[dinosaur] += amount
        else:
            self._dinosaurs[dinosaur] = amount

    def get_dino_count(self, dinosaur: str):
        if dinosaur in self._dinosaurs:
            return self._dinosaurs[dinosaur]
        else:
            return 0

    def remove_dinosaur(self, dinosaur: str, amount: int):
        if dinosaur in self._dinosaurs:
            if self._dinosaurs[dinosaur] >= amount:
                self._dinosaurs[dinosaur] -= amount
            else:
                del self._dinosaurs[dinosaur]

    def has_dinosaur(self, dinosaur: str):
        return dinosaur in self._dinosaurs
    
    def dinosaurs(self):
        return self._dinosaurs

    def get_dinosaurs(self):
        pass