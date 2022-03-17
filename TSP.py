#Authors: Danny Habash & Blake Alvarez
#Description: Traveling salesman problem with simulated annealing and Genetic algorithms
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import approximation as approx
import time
from tqdm import tqdm

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



#mutation function, swaps 2 random indexes in a path
def mutation(path):
    mutation = path
    index1= random.randint(0,len(mutation)-1)
    index2= random.randint(0,len(mutation)-1)
    while index2 == index1:
        index2= random.randint(0,len(mutation)-1)
    mutation[index1], mutation[index2] = mutation[index2], mutation[index1]
    return mutation


#function to create children from parent chromosomes using crossover 
def crossOver(parent1, parent2):

    offspring=[None]*len(parent1)
    offspring2=[None]*len(parent1)

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


    if index1>index2:
        for i in range(index2,index1+1):
            offspring2[i]=parent2[i]
    else:
        for i in range(index1,index2+1):
            offspring2[i]=parent2[i]

    #algorithm to do corssovers from parents to offspring2
    if index1>index2:
        for i in range(index1+1, len(offspring2)):
            for j in range(0, len(offspring2)):
                if parent1[j] not in offspring2:
                    offspring2[i] = parent1[j]
                    break
        for i in range(0, index2):
            for j in range(0, len(offspring2)):
                if parent1[j] not in offspring2:
                    offspring2[i] = parent1[j]
                    break
    else:
        for i in range(index2+1, len(offspring2)):
            for j in range(0, len(offspring2)):
                if parent1[j] not in offspring2:
                    offspring2[i] = parent1[j]
                    break
        for i in range(0, index1):
            for j in range(0, len(offspring2)):
                if parent1[j] not in offspring2:
                    offspring2[i] = parent1[j]
                    break
 
    return offspring, offspring2


#generating random graph of 50
G = nx.complete_graph(50)
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,1000)



#SA to determine GA Task1
cycle1 = approx.simulated_annealing_tsp(G, "greedy", source=0, alpha=.01)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle1))

#creating swapped indices of parents
pathsList=[]
children=[]
for i in range(0,500):
    pathsList.append(GA(cycle1))

#crossover parents to create two children
for i in range(0,500,4):
    child1, child2= crossOver(pathsList[i],pathsList[i+1])
    children.append(child1)
    children.append(child2)


#mutation of 1% of children
for i in range(0,len(children),50):
    mutation(children[i])


#finding the lowest cost value
lowestCost= sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(children[0]))
chosenChild=children[0]
for i in range(0, len(children)):
    children[i].append(0)
    children[i].insert(0, 0)
    
    cost=sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(children[i]))
    if cost < lowestCost:
        lowestCost=cost
        chosenChild=children[i]

#print algorithm results
baseline1=sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(chosenChild))
print("\nTask 1: Genetic Algorithm")
print("Originating from Node 0:",chosenChild )
print("Tour cost:", baseline1, "\n")


#Task 2 simulated annealing
cycle2 = approx.simulated_annealing_tsp(G, "greedy", source=0)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle2))
print("\nTask 2: Simulated Annealing")
print("Originating from Node 0:", cycle2)
print("Tour cost:", cost, "\n")


outputFile =open("output.txt" , "w")

lowest = cost
chosenAlpha = 0.01
chosenPath = cycle1

print("\nPROGRESS: TASK 3")
for z in tqdm(np.arange(0.01, 1.0, 0.001)):

    #SA to determine GA
    cycle1 = approx.simulated_annealing_tsp(G, "greedy", source=0, alpha=float("{:.3f}".format(z)))
    cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle1))

    #creating swapped indices of parents
    pathsList=[]
    children=[]
    for i in range(0,500):
        pathsList.append(GA(cycle1))

    #crossover parents to create two children
    for i in range(0,500,4):
        child1, child2= crossOver(pathsList[i],pathsList[i+1])
        children.append(child1)
        children.append(child2)


    #mutation of 1% of children
    for i in range(0,len(children),50):
        mutation(children[i])


    #finding the lowest cost value
    lowestCost= sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(children[0]))
    chosenChild=children[0]
    for i in range(0, len(children)):
        children[i].append(0)
        children[i].insert(0, 0)
        
        cost=sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(children[i]))
        if cost < lowestCost:
            lowestCost=cost
            chosenChild=children[i]
    
    if lowestCost < lowest:
        lowest = lowestCost
        chosenAlpha = float("{:.3f}".format(z))
        chosenPath=chosenChild
        
    
    print("Alpha: ", float("{:.3f}".format(z)),"\t", "Path: ", chosenChild, "\t", "Cost: ", lowestCost, file=outputFile) 

print("\nTask 3: Different Alpha Values")
print("\nAlpha: ", chosenAlpha,"\t", "Path: ", chosenPath, "\t", "Cost: ", lowest)


pos=nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show() 