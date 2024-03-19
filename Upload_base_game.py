from classes.Dinosaur import Dinosaur as Dino

from classes.Species.Amargasaurus import Amargosaurus
from classes.Species.Ankilosaurus import Ankilosaurus
from classes.Species.Apatosaurus import Apatosaurus
from classes.Species.Archeornithomimus import Archeornithomimus
from classes.Species.Brachiosaurus import Brachiosaurus
from classes.Species.Camarasaurus import Camarasaurus
from classes.Species.Chasmosaurus import Chasmosaurus
from classes.Species.Chungkingosaurus import Chungkingosaurus
from classes.Species.Corytosaurus import Corytosaurus
from classes.Species.Crichtonsaurus import Crichtonsaurus
from classes.Species.Diplodocus import Diplodocus
from classes.Species.Dracorex import Dracorex
from classes.Species.Dreadnoghtus import Dreadnoghtus
from classes.Species.Dyosaurus import Dyosaurus
from classes.Species.Edmontosaurus import Edmontosaurus
from classes.Species.Euoplocephalus import Euoplocephalus
from classes.Species.Gallimimus import Gallimimus
from classes.Species.Gigantspinosaurus import Gigantspinosaurus
from classes.Species.Homalocephale import Homolocephale
from classes.Species.Iguanodon import Iguanodon
from classes.Species.Kentrosaurus import Kentrosaurus
from classes.Species.Maiasaura import Maiasaura
from classes.Species.Mamenchisaurus import Mamenchisaurus
from classes.Species.Muttaburrasaurus import Muttaburrasaurus
from classes.Species.Nasutoceratops import Nasutoceratops
from classes.Species.Nigersaurus import Nigersaurus
from classes.Species.Nodosaurus import Nodosaurus
from classes.Species.Oloratitan import Olorotitan
from classes.Species.Ouranosaurus import Ouranosaurus
from classes.Species.Pachycephalosaurus import Pachycephalosaurus
from classes.Species.Parasaurolophus import Parasaurolophus
from classes.Species.Pentaceratops import Pentaceratops
from classes.Species.Polacanthus import Polacanthus
from classes.Species.Sauropelta import Sauropelta
from classes.Species.Sinoceratops import Sinoceratops
from classes.Species.Stegosaurus import Stegosaurus
from classes.Species.Struthiomimus import Struthiomimus
from classes.Species.Stygimoloch import Stygimoloch
from classes.Species.Styracosaurus import Styracosaurus
from classes.Species.Torosaurus import Torosaurus
from classes.Species.Triceratops import Triceratops
from classes.Species.Tsintaosaurus import Tsintaosaurus


def add_dino(i_data: dict, i_dino: Dino):
    i_data[i_dino.get_species()] = i_dino;


def upload(dinosaurs:dict={}):
    add_dino(i_data=dinosaurs, i_dino=Amargosaurus());
    add_dino(i_data=dinosaurs, i_dino=Ankilosaurus());
    add_dino(i_data=dinosaurs, i_dino=Apatosaurus());
    add_dino(i_data=dinosaurs, i_dino=Archeornithomimus());
    add_dino(i_data=dinosaurs, i_dino=Brachiosaurus());
    add_dino(i_data=dinosaurs, i_dino=Camarasaurus());
    add_dino(i_data=dinosaurs, i_dino=Chasmosaurus());
    add_dino(i_data=dinosaurs, i_dino=Chungkingosaurus());
    add_dino(i_data=dinosaurs, i_dino=Corytosaurus());
    add_dino(i_data=dinosaurs, i_dino=Crichtonsaurus());
    add_dino(i_data=dinosaurs, i_dino=Diplodocus());
    add_dino(i_data=dinosaurs, i_dino=Dracorex());
    add_dino(i_data=dinosaurs, i_dino=Dreadnoghtus());
    add_dino(i_data=dinosaurs, i_dino=Dyosaurus());
    add_dino(i_data=dinosaurs, i_dino=Edmontosaurus());
    add_dino(i_data=dinosaurs, i_dino=Euoplocephalus());
    add_dino(i_data=dinosaurs, i_dino=Gallimimus());
    add_dino(i_data=dinosaurs, i_dino=Gigantspinosaurus());
    add_dino(i_data=dinosaurs, i_dino=Homolocephale());
    add_dino(i_data=dinosaurs, i_dino=Iguanodon());
    add_dino(i_data=dinosaurs, i_dino=Kentrosaurus());
    add_dino(i_data=dinosaurs, i_dino=Maiasaura());
    add_dino(i_data=dinosaurs, i_dino=Muttaburrasaurus());
    add_dino(i_data=dinosaurs, i_dino=Mamenchisaurus());
    add_dino(i_data=dinosaurs, i_dino=Nasutoceratops());
    add_dino(i_data=dinosaurs, i_dino=Nigersaurus());
    add_dino(i_data=dinosaurs, i_dino=Nodosaurus());
    add_dino(i_data=dinosaurs, i_dino=Olorotitan());
    add_dino(i_data=dinosaurs, i_dino=Ouranosaurus());
    add_dino(i_data=dinosaurs, i_dino=Pachycephalosaurus());
    add_dino(i_data=dinosaurs, i_dino=Parasaurolophus());
    add_dino(i_data=dinosaurs, i_dino=Pentaceratops());
    add_dino(i_data=dinosaurs, i_dino=Polacanthus());
    add_dino(i_data=dinosaurs, i_dino=Sauropelta());
    add_dino(i_data=dinosaurs, i_dino=Sinoceratops());
    add_dino(i_data=dinosaurs, i_dino=Stegosaurus());
    add_dino(i_data=dinosaurs, i_dino=Struthiomimus());
    add_dino(i_data=dinosaurs, i_dino=Stygimoloch());
    add_dino(i_data=dinosaurs, i_dino=Styracosaurus());
    add_dino(i_data=dinosaurs, i_dino=Torosaurus());
    add_dino(i_data=dinosaurs, i_dino=Triceratops());
    add_dino(i_data=dinosaurs, i_dino=Tsintaosaurus());
    return dinosaurs;