import pytest
import networkx as nx
from Pathfinder import PathFinder

class TestPathFinder:
    def setup_method(self):
        self.path_finder = PathFinder()

    def test_find_shortest_path_no_via(self):
        G = nx.Graph()
        G.add_edge('A', 'B', weight=2)
        G.add_edge('A', 'C', weight=3)
        G.add_edge('B', 'C', weight=1)
        self.path_finder.G = G
        shortest_path = self.path_finder.find_shortest_path('A', 'B')
        assert shortest_path == ['A', 'B']

    def test_find_shortest_path_with_via(self):
        G = nx.Graph()
        G.add_edge('A', 'B', weight=2)
        G.add_edge('A', 'C', weight=3)
        G.add_edge('B', 'C', weight=1)
        self.path_finder.G = G
        shortest_path = self.path_finder.find_shortest_path('A', 'C', via=['B'])
        assert shortest_path == ['A', 'B', 'C']

    def test_calculate_total_distance(self):
        G = nx.Graph()
        G.add_edge('A', 'B', weight=2)
        G.add_edge('B', 'C', weight=3)
        self.path_finder.G = G
        total_distance = self.path_finder.calculate_total_distance(['A', 'B', 'C'])
        assert total_distance == 5

    def test_add_post_office(self):
        G = nx.Graph()
        self.path_finder.G = G
        self.path_finder.add_postOffice("Post Office Vienna", [('Post Office Graz', '200'), ('Post Office St.Pölten', '70')])
        assert G.has_node('Post Office Vienna')
        assert G.has_edge('Post Office Vienna', 'Post Office Graz')
        assert G.has_edge('Post Office Vienna', 'Post Office St.Pölten')

    def test_remove_post_office(self):
        G = nx.Graph()
        G.add_edge('A', 'B', weight=2)
        G.add_edge('B', 'C', weight=3)
        self.path_finder.G = G
        self.path_finder.remove_postOffice('B')
        assert not G.has_node('B')
        assert not G.has_edge('A', 'B')
        assert not G.has_edge('B', 'C')
