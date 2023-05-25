import networkx as nx
import matplotlib.pyplot as plt
from fastapi import FastAPI

from .pathfinder import PathFinder

app = FastAPI()
path_finder = PathFinder()

