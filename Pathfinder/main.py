from pathfinder import PathFinder

import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path_finder = PathFinder()
    path_finder.visualize_graph()

    start = "Post Office Weiz"
    end = "Post Office Liezen"
    via = ["Post Office Gleisdorf", "Post Office Voitsberg"]
    
    shortest_path = path_finder.find_shortest_path(start, end, via)
    total_distance = path_finder.calculate_total_distance(shortest_path)
    
    print(f"The shortest path from {start} to {end} via {via} is: {shortest_path}")
    print(f"The total distance is: {total_distance}")
