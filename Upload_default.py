from Dinosaur import Dinosaur as Dino


def add_dino(i_data: dict, i_dino: Dino):
    i_data[i_dino.get_species()] = i_dino;

def upload():
    data = {};
    add_dino(i_data=data, i_dino=Dino(i_family=Dino.ORNITHOMIMIDAE, i_species="glamimus"));
    add_dino(i_data=data, i_dino=Dino(i_family=Dino.CERATOPSIDAE, i_species="torosau"));
    add_dino(i_data=data, i_dino=Dino(i_family=Dino.NODOSAURIDAE, i_species="nodosaurus"));
    add_dino(i_data=data, i_dino=Dino(i_family=Dino.HADROSAURIDAE, i_species="parasaurolophus"));
    return data;