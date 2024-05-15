from classes.Park.Enclosure import Enclosure
from classes.Park.Park import Park
from data_structures.likes_dislikes_graph import Graph

def sugest_new_dinosaur(i_enclousure: Enclosure , i_likes: Graph, i_dislikes: Graph, dinosaurs: dict, top: int = 5, park: Park = None):
    # dict with a numerical value that represents the best dinosaur to add to the enclosure
    dinosaurs_value = {}
    for dino in i_likes.nodes:
        if(not i_enclousure.has_dinosaur(dino) and not (park != None and park.has_dinosaur(dino))):
            if(
                (i_enclousure.type == "Lagoon" and not dinosaurs[dino].is_aquatic) or
                (i_enclousure.type == "Aviary" and not dinosaurs[dino].is_pterosaur) or
                (i_enclousure.type == "Terrestrial" and (dinosaurs[dino].is_aquatic or dinosaurs[dino].is_pterosaur))
            ):
                continue
            value = 0
            for dino_in_enclosure in i_enclousure.dinosaurs():
                if(i_likes.is_directly_connected(dino_in_enclosure, dino)):
                    value += 10
                if(i_dislikes.is_directly_connected(dino_in_enclosure, dino)):
                    value -= 1000
                if(i_likes.is_directly_connected(dino, dino_in_enclosure)):
                    value += 10
                if(i_dislikes.is_directly_connected(dino, dino_in_enclosure)):
                    value -= 1000
                if not (
                    i_likes.is_directly_connected(dino_in_enclosure, dino) or 
                    i_dislikes.is_directly_connected(dino_in_enclosure, dino) or 
                    i_likes.is_directly_connected(dino, dino_in_enclosure) or 
                    i_dislikes.is_directly_connected(dino, dino_in_enclosure)
                ):
                    value += 5
                for resource in dinosaurs[dino].paleo_preferences:
                    if((park.biome == "Dessert" and resource == "Forest") or resource == "Wetland"):
                        continue
                    if(i_enclousure.has_resources(resource)):
                        value += 5

            dinosaurs_value[dino] = value

    top_dinos = sorted(dinosaurs_value, key=dinosaurs_value.get, reverse=True)[:top]
    return {dino: dinosaurs_value[dino] for dino in top_dinos}
    
    