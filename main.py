from classes.Dinosaur_json import Dinosaur
from data_structures.likes_dislikes_graph import generate_graph
from load_from_json import upload_base_game


if __name__ == "__main__":
    dinosaurs = upload_base_game();
    
    for dino in dinosaurs:
        print(dinosaurs[dino].to_string())
        print()
    
    (likes, dislikes) = generate_graph(dinosaurs)
    print("LIKES:\n\n")
    print(likes.to_string())

    print("DISLIKES:\n\n")
    print(dislikes.to_string())

