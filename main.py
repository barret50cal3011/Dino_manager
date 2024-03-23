from classes.Dinosaur_json import Dinosaur
from load_from_json import upload_base_game


if __name__ == "__main__":
    dinosaurs = upload_base_game();
    
    for dino in dinosaurs:
        print(dinosaurs[dino].to_string())