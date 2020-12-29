#author: jack mcshane (jamcshan)
#date: 11/9/20
#Applied Algorithms

##prompt:
#given: graph in edge list format
#determine: number of strongly connected components in a graph
import sys


class Graph:

    #initializes empty graph object with {nodes} nodes
    #
    def __init__(self, nodes):
        self.graph = dict()
        for node in range(1, nodes + 1):
            self.graph[node] = list()
        #number of nodes in the graph
        self.nodes = nodes


    def addEdge(self, n1, n2):
        self.graph[n1].append(n2)


    #performs a recursive dfs of graph structure from the passed node
    #--a node is added to the stack once all of its successors have been explored
    #
    def dfs(self, node, visited, stack):
        visited.append(node)

        #loop runs as long as node has successors and those successors have not
        #yet been visited
        for succ in self.graph[node]:
            if succ not in visited:
                self.dfs(succ, visited, stack)

        stack.append( node )


    #returns the transpose of the calling graph obj
    #--transpose of a graph contains the same number of nodes, but the direction
    #the directed edges is reversed
    #
    def getTranspose(self):
        gt = Graph(self.nodes)
        for node in self.graph:
            for elem in self.graph[node]:
                gt.addEdge(elem, node)

        return gt




    #determines number of strongly connected components of calling graph
    #returns: number of SCCs
    #
    def getSCC(self):
        visited = list()
        stack = list()
        for node in self.graph:
            if node not in visited:
                self.dfs(node, visited, stack)


        ###compute Gt
        gt = self.getTranspose()

        ###search Gt by descending order of the finish times of the nodes of G
        num_sccs = 0
        #clear visited struct before starting new dfs
        visited.clear()
        #while stack non-empty
        while stack:
            node = stack.pop()
            if node not in visited:
                num_sccs+=1
                gt.dfs(node, visited, list())

        return num_sccs







###########################################
################DRIVER CODE################
###########################################
#reading in from file
infile = sys.stdin.readlines()
info = [int(elem) for elem in infile[0].split()]
edges = [[int(elem) for elem in infile[i].split()] for i in range(1,len(infile))]

#building graph
g = Graph(info[0])
for initial, terminal in edges:
    g.addEdge(initial, terminal)

print(g.getSCC())
