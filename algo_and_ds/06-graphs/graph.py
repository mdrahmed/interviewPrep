'''
Linked list and trees are a subset of graphs.
E <= V^2
'''

# matrix 2D grid
from collections.abc import ValuesView


grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

# adjacency matrix
adjMatrix = [[0,0,0,0],
             [1,1,0,0],
             [0,0,0,1],
             [0,1,0,0]]

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
