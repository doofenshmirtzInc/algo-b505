from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        #init graph as dictionary that holds list of neighbors
        self.graph = defaultdict(list)
        #number of nodes in the graph
        self.nodes = nodes

    def addEdge(self, n1, n2):
        #add n2 to n1's edge list
        self.graph[n1].append(n2)
