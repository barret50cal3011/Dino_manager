import json
from classes.Dinosaur_json import Dinosaur

def upload_base_game(dinosaurs:dict={}):

    file_name = "data/dinosaurs/base_game.json"
    file = open(file_name)
    data = json.load(file)
    json_dinos = data["dinosaurs"]
    for dino in json_dinos:
        new_dino = Dinosaur(
            i_species=dino["species"],
            i_family=dino["family"],
            i_bio_group=dino["bio_group"],
            i_diet=dino["diet"],
            i_era=dino["era"],
            i_habitat=dino["habitat"],
            i_height=dino["height"],
            i_length=dino["length"],
            i_weight=dino["weight"],
            i_base_appeal=dino["base_appeal"],
            i_likes=dino["likes"],
            i_dislikes=dino["dislikes"]
        )

        dinosaurs[new_dino.get_species()] = new_dino
    file.close()

    return dinosaurs