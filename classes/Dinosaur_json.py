class Dinosaur:
    def __init__(self, 
                 i_species, 
                 i_family, 
                 i_bio_group, 
                 i_diet, i_era, 
                 i_habitat, 
                 i_height, 
                 i_length, 
                 i_weight, 
                 i_base_appeal,
                 i_likes,
                 i_dislikes):
        self.__species = i_species
        self.__family = i_family
        self.__bio_group = i_bio_group
        self.__diet = i_diet
        self.__era = i_era
        self.__habitat = i_habitat
        self.__height = i_height
        self.__length = i_length
        self.__weight = i_weight
        self.__base_appeal = i_base_appeal
        self.__likes = i_likes
        self.__dislikes = i_dislikes


    def get_species(self):
        return self.__species


    def get_family(self):
        return self.__family


    def get_bio_group(self):
        return self.__bio_group


    def get_diet(self):
        return self.__diet
    

    def get_era(self):
        return self.__era
    

    def get_habitat(self):
        return self.__habitat
    

    def get_height(self):
        return self.__height
    

    def get_length(self):
        return self.__length
    

    def get_weight(self):
        return self.__weight


    def get_base_appeal(self):
        return self.__base_appeal


    def get_likes(self):
        return self.__likes
    

    def get_dislikes(self):
        return self.__dislikes

    def to_string(self):
        return f"species: {self.__species}\nfamily: {self.__family},\ndiet: {self.__diet}"
