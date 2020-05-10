from search import *
import numpy as np

class GraphProblem(Problem):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph, V_max):
        Problem.__init__(self, initial, goal)
        self.graph = graph
        self.V_max = V_max

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        # print('Cost Before', cost_so_far)
        # print('Cost After', cost_so_far + (self.graph.get(A, B) or np.inf))
        return cost_so_far + (self.graph.get(A, B) or np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def h(self, node):
        """h function is straight-line distance from a node's state to goal 
            divided by the speed limit of the node's state."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node.state], locs[self.goal])/self.V_max[node.state])
            return int(distance(locs[node.state], locs[self.goal])/self.V_max[node.state])
        else:
            return np.inf

# Graph with actual cost values -> g(n)
graph = UndirectedGraph(dict(
        Arad=dict(Zerind=15, Sibiu=28, Timisoara=23),
        Bucharest=dict(Urziceni=17, Pitesti=20, Giurgiu=18, Fagaras=42),
        Craiova=dict(Drobeta=24, Rimnicu=29, Pitesti=27),
        Drobeta=dict(Mehadia=15),
        Eforie=dict(Hirsova=17),
        Fagaras=dict(Sibiu=19),
        Hirsova=dict(Urziceni=19),
        Iasi=dict(Vaslui=18, Neamt=17),
        Lugoj=dict(Timisoara=22, Mehadia=14),
        Oradea=dict(Zerind=14, Sibiu=30),
        Pitesti=dict(Rimnicu=19),
        Rimnicu=dict(Sibiu=16),
        Urziceni=dict(Vaslui=28))
)

# Used in the distance calculation between 
# node "n" to the goal node (straight line distance = D)
graph.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

# Speed limits (V)
V_maxToGoal = dict(
        Arad=35, Bucharest=50, Craiova=20,
        Drobeta=41, Eforie=22, Fagaras=30,
        Giurgiu=12, Hirsova=19, Iasi=22,
        Lugoj=33, Mehadia=29, Neamt=34,
        Oradea=55, Pitesti=20, Rimnicu=31,
        Sibiu=36, Timisoara=48, Urziceni=10,
        Vaslui=25, Zerind=60
)

initial_N = 'Arad'
goal_N = 'Bucharest'
problem = GraphProblem(initial_N, goal_N, graph, V_maxToGoal)

# A* call. astar_search is from search.py
shortest_Path = astar_search(problem).path()

print("Shortest path from", initial_N, "to", goal_N, "->",  shortest_Path)

# d_v = dict(
#     Arad=dict(Zerind=(75,15), Sibiu=(140, 28), Timisoara=(118, 23)),
#     Bucharest=dict(Urziceni=(85, 17), Pitesti=(101, 20), Giurgiu=(90, 18), Fagaras=(211, 42)),
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
