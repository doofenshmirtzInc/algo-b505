

import sys


# Edge class:
# placeholder used to represent an edge from a source node to a given terminal node
#
class Edge:

    def __init__(self, term, cost):
        self.term = term
        self.cost = cost


# Graph class:
# init function takes an argument in edgelist format
# - i.e. the first element of the edgelist argument should be a list containing the number of nodes and the number of edges in suggested order
# -- the rest of the elements of the edgelist should in themselves be lists, detailing the edges of the graph in the form: src, terminal, cost
#
class Graph:

    # builds graph from the given edgelist
    #
    def __init__(self, edgelist):
        self.nodecount = edgelist.pop(0)[0]
        self.edgelist = dict()
        self.addEdges(edgelist)
        for i in range(1, self.nodecount + 1):
            if i not in self.edgelist:
                self.edgelist[i] = list()


    # fleshes out the edgelists of each node of the graph according to the given list
    #
    def addEdges(self, edgelist):
        for edge in edgelist:
            if len(edge) != 2 and len(edge) != 3:
                raise Exception('Improper format for edgelist! Try ( source, terminal, cost )')
            if len(edge) == 3:
                src, term, cost = edge
                self.addEdge(src, Edge(term, cost))
            else:
                src, term = edge
                self.addEdge(src, Edge(term, 1))


    # adds passed edge to the edgelist of the given source node
    #
    def addEdge(self, src, edge):
        if src not in self.edgelist:
            self.edgelist[src] = list()
        self.edgelist[src].append(edge)


    # an implementation of Dijkstra's algorithm for finding shortest path from a given source node
    # - input: source node given as an integer
    # - returns: a list of distances for each node from the start node
    #
    def dijkstra(self, source):

        # initializing table of shortest distances
        distances = [float('inf')] * self.nodecount
        distances[source - 1] = 0

        # initializing unvisited structure
        unvisited = {source:0}

        while unvisited:
            # get node with minimun cost path and remove from *un*visited
            curr = min(unvisited, key = lambda x: unvisited[x])
            del unvisited[curr]

            for edge in self.edgelist[curr]:
                # if new shortest path, adjust know cost, add back to unvisited with new path cost/length
                if distances[edge.term - 1] > distances[curr - 1] + edge.cost:
                    distances[edge.term - 1] = distances[curr - 1] + edge.cost
                    unvisited[edge.term] = distances[edge.term - 1]

        # replace inf vals with -1's for the nodes that cannot be reached from the source
        while distances.count(float('inf')):
            distances[ distances.index(float('inf')) ] = -1

        # return table
        return distances


    def isBipartite(self, src):

        self.colors = dict.fromkeys( self.edgelist.keys(), None )
        self.colors[src] = 'red'
        q = [src]

        while q:

            node1 = q.pop()
            for edge in self.edgelist[node1]:
                node2 = edge.term
                if self.colors[node1]  == None:

                    if self.colors[node1] == 'red':
                        self.colors[node2] = 'blue'
                        q.append(node2)
                    else:
                        self.colors[node2] = 'red'
                        q.append(node2)

                    if self.colors[node1] == self.colors[node2]:
                        return -1

        return 1



#####END GRAPH DEF


# reads in edgelist from given file
# - input: /path/to/filename
# - output: list of lists
# -- each internal list is a line of the file given as the tokenized elements contained in that particular line
#
def read_file(filename):
    with open(filename, "r") as file:
        f = [line for line in file]
        edgelists = [ [ [int(item) for item in line.split()] for line in group.split('\n') ] for group in ''.join( [f[i] for i in range(2, len(f))] ).split('\n\n') ]
        edgelists[-1].pop()
        return edgelists

# prints contents to file
# - input: /path/to/filename
# - output: the contents of a list printed on a single line
#
def write_file(filename, contents):
    with open(filename, 'w') as file:
        print(*contents, file=file)




def main():

    edgelists = read_file( sys.argv[1] )

    ###### GUTS OF PROGRAM
    graphs = [Graph(edgelist) for edgelist in edgelists]
    ans = [graph.isBipartite(1) for graph in graphs]

    #######################

    write_file( sys.argv[2], ans )



if __name__ == "__main__":

    if( len(sys.argv) != 3 ):
        raise Exception('usage: ./dijk.py input-file output-file')

    main()








