import json

def dino_base():
    dino = {}
    dino["species"] = input("Species: ")
    dino["family"] = input("Family: ")
    dino["bio_group"] = input("Bio Group: ")
    dino["diet"] = input("Diet: ")
    dino["era"] = input("Era: ")
    dino["habitat"] = input("Habitat: ")
    dino["height"] = float(input("Height: "))
    dino["length"] = float(input("Length: "))
    dino["weight"] = int(input("Weight: "))
    dino["base_appeal"] = int(input("Base Appeal: "))
    dino["likes"] = []
    dino["dislikes"] = []

    dino_json = json.dumps(dino, indent=4)
    print(dino_json)