class Park:

    def __init__(self) -> None:
        self.__enclosures = []

    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)