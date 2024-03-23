

class Graph:

    def __init__(self):
        self.__nodes = set()
        self.__edges = {}

    def add_node(self, i_new_node):
        self.__nodes.add(i_new_node)

    
    def add_edge(self, i_origin, i_destination):
        if(not i_origin in self.__nodes):
            raise Exception(f"origin {i_origin} not in nodes")
        if(not i_destination in self.__nodes):
            raise Exception(f"deftonation {i_destination} not in nodes")
        
        if(not i_origin in self.__edges):
            self.__edges[i_origin] = set()
        self.__edges[i_origin].add(i_destination)


    def contains(self, i_dino):
        return i_dino in self.__nodes

def generate_graph(dinosaurs: dict):
    dino_likes = Graph()
    for dino in dinosaurs:
        dino_likes.add_node(dino["species"])

    for dino in dinosaurs:
        likes = dino["likes"]
        for like in likes:
            if(dino_likes.contains(like)):
                dino_likes.add_edge(i_origin=dino, i_destination=like)

    dino_dislikes = Graph()
    for dino in dinosaurs:
        dino_dislikes.add_node(dino["species"])

    for dino in dinosaurs:
        dislikes = dino["dislikes"]
        for dislike in dislikes:
            if(dino_dislikes.contains(dislike)):
                dino_dislikes.add_edge(i_origin=dino, i_destination=dislike)
    
    return (dino_likes, dino_dislikes)

    