from classes.db.Species import Species

class Enclosure:

    def __init__(self, i_type) -> None:
        self._dinosaurs = {}
        self._resources = set()
        self._type = i_type

    @property
    def type(self):
        return self._type

    @property
    def resources(self):
        return self._resources

    def add_dinosaur(self, dinosaur: Species, amount: int):
        if dinosaur.name in self._dinosaurs:
            self._dinosaurs[dinosaur.name] += amount
        else:
            self._dinosaurs[dinosaur.name] = amount
            for resource in dinosaur.paleo_preferences:
                self._resources.add(resource)

    def add_dinosaurs(self, dinosaurs: dict):
        for dinosaur in dinosaurs:
            self.add_dinosaur(dinosaur, dinosaurs[dinosaur])

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
        return self._dinosaurs.keys()
    
    def get_dinosaur_amount(self, dinosaur: str):
        return self._dinosaurs[dinosaur]
    
    def has_resources(self, resource: str):
        return resource in self._resources