import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def graph(happy_path, transitions):
    G = nx.DiGraph()

    ts = [(s,e) for s,e in transitions]
    G.add_edges_from(ts, color='slategray')

    hp = [(s, e) for s,e in happy_path]
    G.add_edges_from(hp, color='goldenrod')

    node_color_map = ['maroon' if node in np.unique(happy_path).tolist() else 'cadetblue' for node in G]

    edge_in_happy_path = ((np.expand_dims(happy_path,1) == np.array(list(G.edges))).sum(axis=-1) == 2).sum(axis=0).astype(bool)
    edge_color_map = ['goldenrod' if happy_edge else 'slategray' for happy_edge in edge_in_happy_path]

    return G, node_color_map, edge_color_map

