import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import approximation as approx


def GA(path):
    chromosome = path.copy()
    chromosome.pop(0)
    chromosome.pop()
    index1= random.randint(0,len(chromosome)-1)
    index2= random.randint(0,len(chromosome)-1)
    while index2 == index1:
        index2= random.randint(0,len(chromosome)-1)

    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
    return chromosome


def crossOver(paths):


    print("parent1", paths[0])
    print("parent2", paths[1])
    parent1 = paths[0]
    parent2 = paths[1]
    

    offspring=[None]*len(parent1)

    index1= random.randint(0,len(parent1)-1)
    index2= random.randint(0,len(parent1)-1)
    while index2 == index1:
        index2= random.randint(0,len(parent1)-1)

    index1 = 2
    index2 = 3

    if index1>index2:
        for i in range(index2,index1+1):
            offspring[i]=parent1[i]
    else:
        for i in range(index1,index2+1):
            offspring[i]=parent1[i]

    print(offspring)

    #algorithm to do corssovers from parents to offspring
    if index1>index2:
        for i in range(index1+1, len(offspring)):
            for j in range(0, len(offspring)):
                if parent2[j] not in offspring:
                    offspring[i] = parent2[j]
                    break
        for i in range(0, index2):
            for j in range(0, len(offspring)):
                if parent2[j] not in offspring:
                    offspring[i] = parent2[j]
                    break
    else:
        for i in range(index2+1, len(offspring)):
            for j in range(0, len(offspring)):
                if parent2[j] not in offspring:
                    offspring[i] = parent2[j]
                    break
        for i in range(0, index1):
            for j in range(0, len(offspring)):
                if parent2[j] not in offspring:
                    offspring[i] = parent2[j]
                    break

 
    print("offspring",offspring)


    





    

    




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






cycle1 = approx.simulated_annealing_tsp(G, "greedy", source="0", alpha=.01)
print(cycle1)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle1))
print(cost)

pathsList=[]
for i in range(0,500):
    pathsList.append(GA(cycle1))



#Task 2 simulated annealing
cycle2 = approx.simulated_annealing_tsp(G, "greedy", source="0")
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle2))
# print("\nTask 2: Simulated Annealing")
# print("Originating from Node 0:", cycle2)
# print("Tour cost:", cost, "\n")



crossOver(pathsList)







pos=nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show() 


