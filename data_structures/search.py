

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