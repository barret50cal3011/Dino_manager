class Dinosaur:

    def __init__(self, i_species, i_family, i_bio_group):
        self._species = i_species;
        self._family = i_family;
        self._bio_goup = i_bio_group;
        self._diet = None;
        self._era = None;


    def get_species(self):
        return self._species;


    def get_family(self):
        return self._family;


    def to_string(self):
        return f"species: {self._species}, family: {self._family}"