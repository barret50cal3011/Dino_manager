import json
from data_structures.search import search_resource_group
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
    #Base information for the dinosaurs
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

    #Reasource group and cohabitation information
    needs_file = open("data/db/species_needs.json")
    needs_data = json.load(needs_file)["rows"]
    for need in needs_data:
        dinosaurs[ids[need[0]]].resource_group = need[7]

    cohabitation_file = open("data/db/species_cohabitation_db.json")
    cohabitation_data = json.load(cohabitation_file)["rows"]
    for cohabitation in cohabitation_data:
        if(cohabitation[3] == 1):
            if(cohabitation[1] == None):
                cohab_species = search_resource_group(dinosaurs, cohabitation[2])
                dinosaurs[ids[cohabitation[0]]].add_cohabitation_like(set(cohab_species))
            else:
                dinosaurs[ids[cohabitation[0]]].add_cohabitation_like(set([ids[cohabitation[1]]]))
                if(ids[cohabitation[1]] in dinosaurs[ids[cohabitation[0]]].cohabitation_dislikes):
                    dinosaurs[ids[cohabitation[0]]].remove_cohabitation_dislike(ids[cohabitation[1]])
        else:
            if(cohabitation[1] == None):
                cohab_species = search_resource_group(dinosaurs, cohabitation[2])
                dinosaurs[ids[cohabitation[0]]].add_cohabitation_dislike(set(cohab_species))
            else:
                dinosaurs[ids[cohabitation[0]]].add_cohabitation_dislike(set([ids[cohabitation[1]]]))
                if(ids[cohabitation[1]] in dinosaurs[ids[cohabitation[0]]].cohabitation_likes):
                    dinosaurs[ids[cohabitation[0]]].remove_cohabitation_like(ids[cohabitation[1]])

    #Paleo preferences
    paleo_file = open("data/db/species_paleo_preference.json")
    paleo_data = json.load(paleo_file)["rows"]
    for preference in paleo_data:
        dinosaurs[ids[preference[0]]].add_preference(preference[1], preference[2])

    return (dinosaurs, ids)

