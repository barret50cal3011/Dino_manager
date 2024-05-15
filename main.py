from classes.Dinosaur_json import Dinosaur
from data_structures.likes_dislikes_graph import generate_graph
from load_from_json import load_form_db
from classes.Park.Park import Park
from classes.Park.Terrestrial import Terrestrial
from classes.Park.Aviary import Aviary
from classes.Park.Lagoon import Lagoon
from classes.Park.Utility import sugest_new_dinosaur


if __name__ == "__main__":
    (dinosaurs, ids) = load_form_db();
    
    (likes, dislikes) = generate_graph(dinosaurs)
    
    my_park = Park(i_biome="Dessert")

    enclosure_0 = Terrestrial()
    enclosure_0.add_dinosaur(dinosaurs["Nasutoceratops"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Struthiomimus"], 17)
    enclosure_0.add_dinosaur(dinosaurs["Muttaburrasaurus"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Nodosaurus"], 4)
    enclosure_0.add_dinosaur(dinosaurs["Torosaurus"], 5)

    enclosure_1 = Terrestrial()
    enclosure_1.add_dinosaur(dinosaurs["Parasaurolophus"], 4)
    enclosure_1.add_dinosaur(dinosaurs["Gallimimus"], 14)
    enclosure_1.add_dinosaur(dinosaurs["Brachiosaurus"], 1)
    enclosure_1.add_dinosaur(dinosaurs["Chasmosaurus"], 4)
    enclosure_1.add_dinosaur(dinosaurs["Minmi"], 4)

    enclosure_2 = Terrestrial()
    enclosure_2.add_dinosaur(dinosaurs["Amargasaurus"], 2)
    enclosure_2.add_dinosaur(dinosaurs["Kentrosaurus"], 5)
    enclosure_2.add_dinosaur(dinosaurs["Dracorex"], 6)
    enclosure_2.add_dinosaur(dinosaurs["Maiasaura"], 4)

    enclosure_3 = Terrestrial()
    enclosure_3.add_dinosaur(dinosaurs["Diplodocus"], 2)
    enclosure_3.add_dinosaur(dinosaurs["Euoplocephalus"], 4)
    enclosure_3.add_dinosaur(dinosaurs["Dryosaurus"], 9)
    enclosure_3.add_dinosaur(dinosaurs["Pachycephalosaurus"], 7)

    enclosure_4 = Terrestrial()
    enclosure_4.add_dinosaur(dinosaurs["Styracosaurus"], 4)
    enclosure_4.add_dinosaur(dinosaurs["Corythosaurus"], 5)
    enclosure_4.add_dinosaur(dinosaurs["Dreadnoughtus"], 1)

    enclosure_5 = Terrestrial()
    enclosure_5.add_dinosaur(dinosaurs["Apatosaurus"], 3)

    enclosure_c0 = Terrestrial()
    enclosure_c0.add_dinosaur(dinosaurs["Ceratosaurus"], 3)

    enclosure_c1 = Terrestrial()
    enclosure_c1.add_dinosaur(dinosaurs["Carnotaurus"], 3)

    aviary = Aviary()
    aviary.add_dinosaur(dinosaurs["Dimorphodon"], 3)
    aviary.add_dinosaur(dinosaurs["Cearadactylus"], 2)


    lagoon = Lagoon()
    lagoon.add_dinosaur(dinosaurs["Plesiosaurus"], 1)

    my_park.add_enclosure(enclosure_0)
    my_park.add_enclosure(enclosure_1)
    my_park.add_enclosure(enclosure_2)
    my_park.add_enclosure(enclosure_3)
    my_park.add_enclosure(enclosure_c0)

    print(sugest_new_dinosaur(enclosure_0, likes, dislikes, dinosaurs, top=20, park=my_park))
    print()
    print(sugest_new_dinosaur(enclosure_1, likes, dislikes, dinosaurs, top=20, park=my_park))
    print()
    print(sugest_new_dinosaur(enclosure_2, likes, dislikes, dinosaurs, top=20, park=my_park))
    print()
    print(sugest_new_dinosaur(enclosure_3, likes, dislikes, dinosaurs, top=20, park=my_park))
    print()
    print(sugest_new_dinosaur(enclosure_4, likes, dislikes, dinosaurs, top=20, park=my_park))
    print()
    print(sugest_new_dinosaur(enclosure_5, likes, dislikes, dinosaurs, top=20, park=my_park))

    print()
    print()
    print(sugest_new_dinosaur(aviary, likes, dislikes, dinosaurs, top=20, park=my_park))


    print()
    print()
    print(sugest_new_dinosaur(lagoon, likes, dislikes, dinosaurs, top=20, park=my_park))

    print()
    print()
    print(sugest_new_dinosaur(enclosure_c0, likes, dislikes, dinosaurs, top=20, park=my_park))

    


