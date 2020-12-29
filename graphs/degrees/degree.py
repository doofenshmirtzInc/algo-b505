#author: jack mcshane
#assignment: double-degree array
"""description:
stuff
"""



import sys

##read input
infile = sys.stdin.readlines()
info = [int(elem) for elem in infile[0].split()]
edges = [[int(elem) for elem in infile[i].split()] for i in range(1,len(infile))]

##build graph
#create graph dict
graph = {}
for i in range(1, info[0] + 1):
    graph[str(i)] = []

#flesh out edge lists of nodes
for edge in edges:
    n1, n2 = edge
    graph[str(n1)].append(n2)
    graph[str(n2)].append(n1)

##calc sum of degrees of each nodes neighbor
#degrees = [sum( x ) for node in graph]
#neigh = []
#for node in graph:
    #neigh = [len( graph[str(endpt)] ) for endpt in graph[str(node)]]

sum_of_neighbors = [sum( [len( graph[str(endpt)] ) for endpt in graph[str(node)]] ) for node in graph]
print(*sum_of_neighbors)
