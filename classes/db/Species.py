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
    
    @resource_group.setter
    def resource_group(self, i_resource_group):
        if(self.__resource_group != None):
            raise Exception("Resource group is already set")
        self.__resource_group = i_resource_group

    