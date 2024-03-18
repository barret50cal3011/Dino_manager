from classes.Dinosaur import Dinosaur as Dino
from data_structures.search import search_family
from Upload_base_game import upload


if __name__ == "__main__":
    dinosaurs = upload();
    armor_herbivores = search_family(i_dinosaurs=dinosaurs, i_family="nodosauridae")

    print("nodosauridae")
    for dino in armor_herbivores:
        print(armor_herbivores[dino].to_string())