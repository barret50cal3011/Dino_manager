from classes.Dinosaur import Dinosaur as Dino
from classes.Parasaurolophus import Parasaurolophus
from classes.Torosaurus import Torosaurus
from classes.Nodosaurus import Nodosaurus
from classes.Gallimimus import Gallimimus


def add_dino(i_data: dict, i_dino: Dino):
    i_data[i_dino.get_species()] = i_dino;


def upload():
    data = {};
    add_dino(i_data=data, i_dino=Gallimimus());
    add_dino(i_data=data, i_dino=Torosaurus());
    add_dino(i_data=data, i_dino=Nodosaurus());
    add_dino(i_data=data, i_dino=Parasaurolophus());
    return data;