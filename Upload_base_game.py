from classes.Dinosaur import Dinosaur as Dino
from classes.Species.Parasaurolophus import Parasaurolophus
from classes.Species.Torosaurus import Torosaurus
from classes.Species.Nodosaurus import Nodosaurus
from classes.Species.Gallimimus import Gallimimus
from classes.Species.Stygimoloch import Stygimoloch
from classes.Species.Pachycephalosaurus import Pachycephalosaurus
from classes.Species.Homalocephale import Homolocephale
from classes.Species.Dracorex import Dracorex
from classes.Species.Archeornithomimus import Archeornithomimus
from classes.Species.Struthiomimus import Struthiomimus
from classes.Species.Stegosaurus import Stegosaurus


def add_dino(i_data: dict, i_dino: Dino):
    i_data[i_dino.get_species()] = i_dino;


def upload(dinosaurs:dict={}):
    add_dino(i_data=dinosaurs, i_dino=Archeornithomimus());
    add_dino(i_data=dinosaurs, i_dino=Dracorex());
    add_dino(i_data=dinosaurs, i_dino=Gallimimus());
    add_dino(i_data=dinosaurs, i_dino=Homolocephale());
    add_dino(i_data=dinosaurs, i_dino=Nodosaurus());
    add_dino(i_data=dinosaurs, i_dino=Pachycephalosaurus());
    add_dino(i_data=dinosaurs, i_dino=Parasaurolophus());
    add_dino(i_data=dinosaurs, i_dino=Stegosaurus());
    add_dino(i_data=dinosaurs, i_dino=Struthiomimus());
    add_dino(i_data=dinosaurs, i_dino=Stygimoloch());
    add_dino(i_data=dinosaurs, i_dino=Torosaurus());
    return dinosaurs;