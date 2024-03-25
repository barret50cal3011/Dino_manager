from classes.Dinosaur_json import Dinosaur
from data_structures.likes_dislikes_graph import generate_graph
from load_from_json import load_form_db
from data_structures.search import search_resource_group
from classes.Park.Park import Park
from classes.Park.Terrestrial import Terrestrial
from classes.Park.Utility import sugest_new_dinosaur


if __name__ == "__main__":
    (dinosaurs, ids) = load_form_db();
    
    (likes, dislikes) = generate_graph(dinosaurs)
    
    my_park = Park()

    enclosure_0 = Terrestrial()
    enclosure_0.add_dinosaur(dinosaurs["Nasutoceratops"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Struthiomimus"], 11)
    enclosure_0.add_dinosaur(dinosaurs["Muttaburrasaurus"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Nodosaurus"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Torosaurus"], 2)

    enclosure_1 = Terrestrial()
    enclosure_1.add_dinosaur(dinosaurs["Parasaurolophus"], 4)
    enclosure_1.add_dinosaur(dinosaurs["Gallimimus"], 4)
    enclosure_1.add_dinosaur(dinosaurs["Diplodocus"], 4)

    enclosure_2 = Terrestrial()
    enclosure_2.add_dinosaur(dinosaurs["Amargasaurus"], 1)

    enclosure_c0 = Terrestrial()
    enclosure_c0.add_dinosaur(dinosaurs["Ceratosaurus"], 4)

    my_park.add_enclosure(enclosure_0)
    my_park.add_enclosure(enclosure_1)
    my_park.add_enclosure(enclosure_c0)

    print(sugest_new_dinosaur(enclosure_2, likes, dislikes, top=20, park=my_park))

    print(likes.is_directly_connected("Nasutoceratops", "Struthiomimus"))
    print(likes.is_directly_connected("Struthiomimus", "Nasutoceratops"))
    


