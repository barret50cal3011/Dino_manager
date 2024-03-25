from classes.Park.Enclosure import Enclosure

class Park:

    def __init__(self) -> None:
        self.__enclosures = []

    def add_enclosure(self, enclosure: Enclosure):
        self.__enclosures.append(enclosure)

    def has_dinosaur(self, dinosaur: str):
        for enclosure in self.__enclosures:
            if enclosure.has_dinosaur(dinosaur):
                return True
        return False

    def get_enclosures(self, dinosaur: str):
        return [enclosure for enclosure in self.__enclosures if enclosure.has_dinosaur(dinosaur)]
    
    