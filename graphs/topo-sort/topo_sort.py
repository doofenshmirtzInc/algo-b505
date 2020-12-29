
#author: jack mcshane
#assignment: double-degree array
"""description:
stuff
"""



import sys
from collections import defaultdict

def topo_helper(graph, i, visited, stk):
    visited[i] = True
    for node in graph[i-1]:
        if not visited[node-1]:
            topo_helper(graph, node, visited, stk)

    stk.append(i)



def topological_sort(graph):
    stk = []
    num_nodes = len(graph)
    visited = [False] * num_nodes

    for i in range(num_nodes):
        if not visited[i]:
            topo_helper(graph, i, visited, stk)


    print(stk[::-1])



####driver code
##read input
infile = sys.stdin.readlines()
info = [int(elem) for elem in infile[0].split()]
edges = [[int(elem) for elem in infile[i].split()] for i in range(1,len(infile))]

##build graph
#create graph dict
graph = defaultdict(list)

#flesh out edge lists of nodes
for edge in edges:
    n1, n2 = edge
    graph[n1].append(n2)

print(graph)

topological_sort(graph)
#print(*sortd_graph)
