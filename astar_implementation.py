from problems import GraphProblem
from search import *
import romania
import numpy as np

class AStarGraphProblem(GraphProblem):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph, v_V):
        super().__init__(initial, goal, graph)
        self.v_V = v_V

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B)/self.v_V[A][0] or np.inf)

    def h(self, node):
        """h function is straight-line distance from a node's state to goal 
            divided by the speed limit of the node's state."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node.state], locs[self.goal])/self.v_V[node.state][1])
            return int(distance(locs[node.state], locs[self.goal])/self.v_V[node.state][1])
        else:
            return np.inf


initial_N = 'Arad'
goal_N = 'Bucharest'
problem = AStarGraphProblem(initial_N, goal_N, romania.graph, romania.speeds)

# A* call. astar_search is from search.py
shortest_Path = astar_search(problem).path()

print("Shortest path from", initial_N, "to", goal_N, "->",  shortest_Path)

# d_v = dict(
#     Arad=dict(Zerind=(75,15, 60), Sibiu=(140, 28, 36), Timisoara=(118, 23, 48)),
#     Bucharest=dict(Urziceni=(85, 17, 10), Pitesti=(101, 20), Giurgiu=(90, 18), Fagaras=(211, 42)),
#     Craiova=dict(Drobeta=(120, 24), Rimnicu=(146, 29), Pitesti=(138, 27)),
#     Drobeta=dict(Mehadia=(75, 15)),
#     Eforie=dict(Hirsova=(86, 17)),
#     Fagaras=dict(Sibiu=(99, 19)),
#     Hirsova=dict(Urziceni=(98, 19)),
#     Iasi=dict(Vaslui=(92, 18), Neamt=(87, 17)),
#     Lugoj=dict(Timisoara=(111, 22), Mehadia=(70, 14)),
#     Oradea=dict(Zerind=(71, 14), Sibiu=(151, 30)),
#     Pitesti=dict(Rimnicu=(97, 19)),
#     Rimnicu=dict(Sibiu=(80, 16)),
#     Urziceni=dict(Vaslui=(142, 28))
# )
