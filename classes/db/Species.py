class Species:

    def __init__(self, i_id, i_name, i_dlc_pack, i_is_live_bait, i_bio_group, i_is_pterosaur, i_is_aquatic):
        self.__id = i_id
        self.__name = i_name
        self.__dlc_pack = i_dlc_pack
        self.__is_live_bait = i_is_live_bait
        self.__bio_group = i_bio_group
        self.__is_pterosaur = i_is_pterosaur
        self.__is_aquatic = i_is_aquatic
        self.__resource_group = None
        self.__cohabitation_likes = set()
        self.__cohabitation_dislikes = set()
        self.__paleo_preferences = {}

    
    @property
    def id(self):
        return self.__id
        
    @property
    def name(self):
        return self.__name
    
    @property
    def dlc_pack(self):
        return self.__dlc_pack

    @property
    def is_live_bait(self):
        return self.__is_live_bait

    @property
    def bio_group(self):
        return self.__bio_group

    @property
    def is_pterosaur(self):
        return self.__is_pterosaur

    @property
    def is_aquatic(self):
        return self.__is_aquatic
    
    @property
    def resource_group(self):
        return self.__resource_group
    
    @property
    def cohabitation_likes(self):
        return self.__cohabitation_likes
    
    @property
    def cohabitation_dislikes(self):
        return self.__cohabitation_dislikes
    
    @property
    def paleo_preferences(self):
        return self.__paleo_preferences

    def is_terrestrial(self):
        return not (self.__is_aquatic or self.__is_pterosaur)
    
    def add_preference(self, i_preference, i_amount):
        self.__paleo_preferences[i_preference] = i_amount
    
    @resource_group.setter
    def resource_group(self, i_resource_group):
        if(self.__resource_group != None):
            raise Exception("Resource group is already set")
        self.__resource_group = i_resource_group

    def add_cohabitation_like(self, i_species:set):
        self.__cohabitation_likes = self.__cohabitation_likes.union(i_species)

    def add_cohabitation_dislike(self, i_species:set):
        self.__cohabitation_dislikes = self.__cohabitation_dislikes.union(i_species)

    def remove_cohabitation_like(self, i_species:set):
        self.__cohabitation_likes.remove(i_species)

    def remove_cohabitation_dislike(self, i_species:set):
        self.__cohabitation_dislikes.remove(i_species)
    