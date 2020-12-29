#author: jack mcshane
#
#This program implements BFS on a given graph structure
#
import sys

class Graph:

    def __init__(self, nodes):
        self.graph = dict()
        self.nodes = nodes
        #create empty list of neighboring nodes for each list
        for node in range(1, self.nodes + 1):
            self.graph[node] = list()


    def addEdge(self, init, term):
        #append terminal node to inits list of connected nodes
        self.graph[init].append(term)


    def addEdges(self, edgelist):
        for init, terminal in edgelist:
            self.addEdge(init, terminal)
        return self



def bfs(graph, start, goal):
    #if goal(start), return cost=0
    if start == goal:
        return 0
    #else, insert(fringe)
    visited = list()
    fringe = [(0, start)]

    #while fringe not empty
    while fringe:
        cost, node = fringe.pop(0)
        visited.append(node)
        if node == goal:
            return cost

        for neighbor in graph.graph[node]:
            if neighbor not in visited:
                fringe.append( (cost+1, neighbor) )

    return -1


if __name__ == '__main__':

    #reading in from file
    infile = sys.stdin.readlines()
    info = [int(elem) for elem in infile[0].split()]
    edges = [[int(elem) for elem in infile[i].split()] for i in range(1,len(infile))]

    #build graph
    g = Graph(info[0]).addEdges(edges)
    shortest_path = [ bfs(g, 1, node) for node in g.graph ]

    print(*shortest_path)
