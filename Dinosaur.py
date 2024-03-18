class Dinosaur:

    CERATOPSIDAE = "ceratopsidae";
    ORNITHOMIMIDAE = "ornithomimidae";
    ANKILOSAURID = "ankilosaurid";
    HADROSAURIDAE = "hadrosauridae";
    NODOSAURIDAE = "nodosauridae"


    def __init__(self, i_species, i_family):
        self.__species = i_species;
        self.__family = i_family;


    def get_species(self):
        return self.__species;


    def get_family(self):
        return self.__family;


    def to_string(self):
        return f"species: {self.__species}, family: {self.__family}"