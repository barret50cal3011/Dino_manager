from classes.Dinosaur import Dinosaur as Dino
from Upload_base_game import upload


if __name__ == "__main__":
    dinosaurs = upload();
    for name in dinosaurs:
        print(dinosaurs[name].to_string())
