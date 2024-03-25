from classes.Dinosaur_json import Dinosaur
from data_structures.likes_dislikes_graph import generate_graph
from load_from_json import load_form_db
from data_structures.search import search_resource_group


if __name__ == "__main__":
    (dinosaurs, ids) = load_form_db();
    
    (likes, dislikes) = generate_graph(dinosaurs)
    print(likes.is_directly_connected("Brachiosaurus", "Ankylodocus"))
    print(dislikes.is_directly_connected("Brachiosaurus", "Ankylodocus"))
