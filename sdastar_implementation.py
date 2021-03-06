#
# Authors: Javier Figueroa, Jadhiel Alvarez and Brian Muñoz
#
from problems import GraphProblem
import romania
from search import *
from math import exp
from random import random
import numpy as np

class SDAStarGraphProblem(GraphProblem):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph, v_V):
        super().__init__(initial, goal, graph)
        self.v_V = v_V

    def path_cost(self, cost_so_far, A, action, B):
        random_var = random()
        probability = 1 - exp(-1.5*cost_so_far)
        if (random_var >= probability):
            step_cost = (self.graph.get(A, B)/self.v_V[A][0] or np.inf)
        else:
            step_cost = (self.graph.get(A, B)/self.v_V[A][1] or np.inf)

        return cost_so_far + step_cost

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
problem = SDAStarGraphProblem(initial_N, goal_N, romania.graph, romania.speeds)

# A* call. astar_search is from search.py
shortest_Path = astar_search(problem).path()

print("Shortest path from", initial_N, "to", goal_N, "->",  shortest_Path)

