import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import approximation as approx

G = nx.Graph()

G.add_edge("0", "1", weight=907)
G.add_edge("0", "3", weight=688)
G.add_edge("0", "5", weight=891)
G.add_edge("0", "6", weight=70)
G.add_edge("0", "4", weight=589)
G.add_edge("0", "2", weight=91)

G.add_edge("5", "1", weight=903)
G.add_edge("5", "4", weight=603)
G.add_edge("5", "6", weight=695)
G.add_edge("5", "2", weight=391)
G.add_edge("5", "3", weight=453)

G.add_edge("6", "1", weight=787)
G.add_edge("6", "2", weight=651)
G.add_edge("6", "3", weight=655)
G.add_edge("6", "4", weight=25)

G.add_edge("2", "4", weight=547)
G.add_edge("2", "3", weight=986)
G.add_edge("2", "1", weight=64)

G.add_edge("4", "3", weight=712)
G.add_edge("4", "1", weight=685)

G.add_edge("3", "1", weight=533)

cycle = approx.simulated_annealing_tsp(G, "greedy", source="0")
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
print("\nTask 2: Simulated Annealing")
print("Originating from Node 0:", cycle)
print("Tour cost:", cost, "\n")


pos=nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show() 