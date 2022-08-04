import networkx as nx
import random

def montecarlo(graph, aspp):
    result = graph
    for edge in nx.edges(graph):
        al_var = random.random()
        
        if al_var > aspp:
            result.remove_edge(edge[0], edge[1])

    if nx.is_connected(result):
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