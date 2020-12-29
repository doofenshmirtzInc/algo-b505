import sys
from collections import defaultdict




class Graph:
    def __init__(self, num_nodes):
        self.graph = defaultdict(list)
        for node in range(1, num_nodes):
            self.graph[i] = list()
        self.num_nodes = num_nodes


    def addEdge(self, n1, n2):
        self.graph[n1].append(n2)


    def topo_helper(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v + 1]:
            if not visited[i]:
                self.topo_helper(i, visited, stack)

        stack.append[v]


    def topologicalSort(self):
        visited = [False] * self.num_nodes
        stack = []

        for i in range(self.num_nodes):
            if not visited[i]:
                self.topo_helper(i, visited, stack)

        print(stack[::-1])


#####driver code


##read input
infile = sys.stdin.readlines()
info = [int(elem) for elem in infile[0].split()]
edges = [[int(elem) for elem in infile[i].split()] for i in range(1,len(infile))]

g = Graph(info[0])
for edge in edges:
    g.addEdge(edge[0], edge[1])


g.topologicalSort()
