import json
from data_structures.search import search_id
from classes.Dinosaur_json import Dinosaur
from classes.db.Species import Species

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

def load_form_db(dinosaurs:dict={}, ids:dict={}):
    species_file_name = "data/db/species_db.json"
    species_file = open(species_file_name)
    species_data = json.load(species_file)["rows"]

    for species in species_data:
        new_dino = Species(
            i_id=species[0],
            i_name=species[1],
            i_dlc_pack=species[5],
            i_is_live_bait=species[6],
            i_bio_group=species[7],
            i_is_pterosaur=species[10],
            i_is_aquatic=species[11]
        )
        ids[new_dino.id] = new_dino.name
        dinosaurs[new_dino.name] = new_dino

    needs_file = open("data/db/species_needs.json")
    needs_data = json.load(needs_file)["rows"]
    for need in needs_data:
        dinosaurs[ids[need[0]]].resource_group = need[7]

    return (dinosaurs, ids)

