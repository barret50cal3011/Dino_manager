class Dinosaur:

    def __init__(self, i_species, i_family, i_bio_group):
        self._species = i_species;
        self._family = i_family;
        self._bio_goup = i_bio_group;
        self._diet = None;
        self._era = None;
        self._likes = set();
        self._dislikes = set();


    def get_species(self):
        return self._species;


    def get_family(self):
        return self._family;


    def get_bio_group(self):
        return self._bio_goup;


    def get_era(self):
        return self._era;


    def to_string(self):
        return f"species: {self._species}\nfamily: {self._family}\ndiet: {self._diet}\nera: {self._era}\n\n"