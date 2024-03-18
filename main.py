from classes.Dinosaur import Dinosaur as Dino
from data_structures.search import search_bio_group
from Upload_base_game import upload


if __name__ == "__main__":
    dinosaurs = upload();
    armor_herbivores = search_bio_group(i_dinosaurs=dinosaurs, i_bio_group="armor herbivore")

    print("armor herbivores")
    for dino in armor_herbivores:
        print(armor_herbivores[dino].to_string())