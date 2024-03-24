

def search_era(i_dinosaurs: dict, i_era: str):
    res = {};
    for species in i_dinosaurs:
        if i_dinosaurs[species].get_era() == i_era:
            res[species] = i_dinosaurs[species]
    return res


def search_bio_group(i_dinosaurs: dict, i_bio_group: str):
    res = {}
    for species in i_dinosaurs:
        if i_dinosaurs[species].get_bio_group() == i_bio_group:
            res[species] = i_dinosaurs[species]
    return res


def search_family(i_dinosaurs: dict, i_family: str):
    res = {}
    for species in i_dinosaurs:
        if i_dinosaurs[species].get_family() == i_family:
            res[species] = i_dinosaurs[species]
    return res

def search_id(i_dinosaurs: dict, i_id: int):
    res = None
    for species in i_dinosaurs:
        if i_dinosaurs[species].id == i_id:
            res = i_dinosaurs[species]
    return res

def search_resource_group(i_dinosaurs: dict, i_resource_group: str):
    res = set()
    for species in i_dinosaurs:
        if i_dinosaurs[species].resource_group == i_resource_group:
            res.add(i_dinosaurs[species].name)
    return res