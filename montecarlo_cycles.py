import networkx as nx
import random
import pdb

def contain_cycle(graph, cycle):
    result = True
    for edge in cycle:
        result = result and edge in graph.edges
    
    return result


def contain_cycles(graph):
    cycles=[
        [(1,2),(2,3),(3,6),(6,1)],
        [(1,2),(2,3),(3,7),(7,1)],
        [(1,2),(2,3),(3,6),(6,7),(7,1)],
        [(1,4),(4,2),(2,3),(3,6),(6,1)],
        [(1,4),(4,2),(2,3),(3,7),(7,1)],
        [(1,4),(4,6),(6,3),(3,2),(2,1)],
        [(1,2),(2,3),(3,8),(8,7),(7,1)],
        [(1,2),(2,6),(6,3),(3,7),(7,1)],
        [(1,2),(2,5),(5,3),(3,6),(6,1)]
    ]
    result = False
    for cycle in cycles:
        result = result or contain_cycle(graph, cycle)
    return result

def montecarlo(graph, aspp):
    result = graph.copy()
    opuesto = graph.copy()
    opuesto.clear_edges()
    for edge in nx.edges(graph):
        al_var = random.random()
        
        if al_var > aspp:
            result.remove_edge(edge[0], edge[1])
            opuesto.add_edge(edge[0], edge[1])

    if contain_cycles(result) and not contain_cycles(opuesto):
        return 1
    else:
        return 0


def call(edges, p):
    G = nx.Graph()

    estimation = 0
    iter = 5000
    varianza = 0
    for i in range(0,iter):
        G.add_edges_from(edges)
        res = (montecarlo(G,p))
        estimation += res
        varianza += res*res
        G.clear_edges()
    
    return [(estimation/iter), (varianza-(estimation*estimation)/iter)/(iter*(iter-1))]