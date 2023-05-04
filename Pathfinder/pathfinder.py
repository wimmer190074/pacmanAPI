import networkx as nx
import matplotlib.pyplot as plt
from .database import Database

class PathFinder:
    def __init__(self):
        db = Database()

    def find_shortest_path(self, start, end, via=[]):
        if not via:
            # The via nodes are already in the shortest path
            shortest_path = nx.shortest_path(self.G, start, end, weight="weight")
            return shortest_path
        else:   
            # Find the shortest path that includes the via nodes
            paths_via = [nx.shortest_path(self.G, start, via[0], weight="weight")]
            for i in range(1, len(via)):
                paths_via.append(nx.shortest_path(self.G, via[i-1], via[i], weight="weight")[1:])
            paths_via.append(nx.shortest_path(self.G, via[-1], end, weight="weight")[1:])
            shortest_path = []
            for path in paths_via:
                shortest_path.extend(path)
            if len(shortest_path) > 0:
                return shortest_path
            else:
                return nx.shortest_path(self.G, start, end, weight="weight")
        
    def calculate_total_distance(self, path):
        total_distance = sum([self.G[path[i]][path[i+1]]["weight"] for i in range(len(path)-1)])
        return total_distance

    def add_postOffice(name, adjacentOffices):
        # Takes the name of a new offices and a list of tuples of the offices that are adjacent to it and the distance between them. If the Adjacent Office doesn't already exist it gets created.
        location = name.split(" ")[2:][0]
        print(location)

        new_post_office = Database().create_post_office(name=name, location=location)

        for i in adjacentOffices:
            adj_name = i[0] #Office Name
            adj_distance = i[1] #Distance to that Office
            print(adj_distance)
            print(adj_name)
            print(name)
            _return = Database().create_edge(name, adj_name, adj_distance)
            if _return is not None: 
                print("The " + _return + " didn't exist and was therefore created.")

    def remove_postOffice(self, id):
        #remove edges of this thing
        Database().delete_edge(id)
        Database().delete_post_office(id)
        name_ = Database().get_post_office_by_id(id)
        print("Post Office " + str(name_) + " was removed.")


    #adj1 = ('Post Office Graz', '200')
    #adj2 = ('Post Office St.Pölten', '70')
    #listst = [adj1, adj2]
    #PathFinder.add_postOffice("Post Office Vienna", listst)

