from tracemalloc import start
import networkx as nx
import random

def random_num(graph, node, neighbours):
    cont = 0
    for nei in neighbours:
        ran = random.random()
        if ran > graph.get_edge_data(node,nei)["weight"]:
            cont += 1
    return cont

def compute_q_c(graph, node):
    q_c = 1
    for nei in graph[node]:
        p_nei = graph.get_edge_data(node,nei)["weight"]
        q_c = q_c * (1-p_nei)
    return q_c

def remove_edges(graph, node, al_var):
    for n in range(0,al_var):
        first_nei = None
        for neighbour in graph[node]:
            first_nei = neighbour
            break
        graph.remove_edge(node,first_nei)
    return graph

def contract_edge(graph, node):
    node_to_contract = None
    for neighbour in graph[node]:
            node_to_contract = neighbour
            break
    node_neighs = [n for n in graph[node]]
    node_to_contract_neighs = [n for n in graph[node_to_contract]]
    nodes_intersection = set(node_to_contract_neighs).intersection(node_neighs)
    for node_i in nodes_intersection:
        weight_with_node = graph.get_edge_data(node,node_i)["weight"]
        weight_with_node_to_contract = graph.get_edge_data(node_to_contract,node_i)["weight"]
        new_weight = weight_with_node + weight_with_node_to_contract - weight_with_node * weight_with_node_to_contract
        attrs = {(node, node_i): {"weight": new_weight}}
        nx.set_edge_attributes(graph, attrs)

    return nx.contracted_edge(graph, (node,node_to_contract))

def remove_archs(graph):
    removed_archs = graph.copy()
    for edge in graph.edges:
        if edge[0] == edge[1]:
            removed_archs.remove_edge(edge[0], edge[1])
    return removed_archs

def rvr(graph):
    if nx.number_of_nodes(graph) == 1:
        return 0
    if not nx.is_connected(graph):
        return 1
    for node in nx.nodes(graph):
        al_var = random_num(graph, node, graph[node])

        q_c = compute_q_c(graph, node)
        if al_var <= 0:
            graph = remove_edges(graph, node, al_var-1)
        if not nx.is_connected(graph):
            return 1
        if al_var != len(graph[node]):
            graph = contract_edge(graph, node)
        graph = remove_archs(graph)

        return q_c + (1-q_c)*rvr(graph)


def call(edges):
    G = nx.Graph()

    iter = 5000
    estimation = 0
    varianza = 0
    for i in range(0,iter):
        G.add_weighted_edges_from(edges)
        res = (1-rvr(G))
        estimation += res
        varianza += res*res
        G.clear_edges()
    return [(estimation/iter), (varianza-(estimation*estimation)/iter)/(iter*(iter-1))] 
    

