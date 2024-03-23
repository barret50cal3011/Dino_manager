

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
    
    def to_string(self):
        str = "Nodes:\n"
        for node in self.__nodes:
            str += node + "    \n"
        str += "\n"

        for node in self.__edges:
            str += "    " + node + "|-->"
            for edge in self.__edges[node]:
                str += edge + ", "
            str += "\n"
        
        return str

def generate_graph(dinosaurs: dict):
    dino_likes = Graph()
    for dino in dinosaurs:
        dino_likes.add_node(dino)

    for dino in dinosaurs:
        likes = dinosaurs[dino].get_likes()
        for like in likes:
            if(dino_likes.contains(like)):
                dino_likes.add_edge(i_origin=dino, i_destination=like)

    dino_dislikes = Graph()
    for dino in dinosaurs:
        dino_dislikes.add_node(dino)

    for dino in dinosaurs:
        dislikes = dinosaurs[dino].get_dislikes()
        for dislike in dislikes:
            if(dino_dislikes.contains(dislike)):
                dino_dislikes.add_edge(i_origin=dino, i_destination=dislike)
    
    return (dino_likes, dino_dislikes)

    