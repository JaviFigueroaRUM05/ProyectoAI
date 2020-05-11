from graphs import UndirectedGraph

# ______________________________________________________________________________
# Romania Map and Properties

# Graph with actual cost values -> g(n)
graph = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

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

# Dictionary of speeds. Format: City(actual speed, speed limit)
speeds = dict(
        Arad=(20, 35), Bucharest=(38, 50), Craiova=(10, 20),
        Drobeta=(36, 41), Eforie=(11, 22), Fagaras=(22, 30),
        Giurgiu=(7, 12), Hirsova=(15, 19), Iasi=(18, 22),
        Lugoj=(21, 33), Mehadia=(24, 29), Neamt=(19, 34),
        Oradea=(44, 55), Pitesti=(15, 20), Rimnicu=(22, 31),
        Sibiu=(20, 36), Timisoara=(33, 48), Urziceni=(6, 10),
        Vaslui=(11, 25), Zerind=(50, 60))



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