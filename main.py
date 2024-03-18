from Dinosaur import Dinosaur as Dino
from Upload_default import upload


if __name__ == "__main__":
    data = upload();
    for key in data:
        print(data[key].to_string())
