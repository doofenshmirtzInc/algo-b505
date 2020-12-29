class NodeDistance:
    def __init__(self, name, dist):
        self.name = name
        self.dist = dist


class Graph:

    def __init__(self, node_count):
        self.edgelist = dict()
        self.node_count = node_count


    def addEdge(self, src, node_dist):
        if src not in self.edgelist:
            self.edgelist[src] = list()
        self.edgelist[src].append(node_dist)


    def dijkstras(self, source):

        #initialize distance of all nodes from source to infinity
        distance = [float('inf')] * self.node_count

        #distance of souce to itself = 0
        distance[source] = 0

        #create dict of {node, dist-from-source}
        dict_node_length = {source: 0}

        while dict_node_length:

            #get key for smallest value in dictionary
            #ie. get node with shortest distance from the shource
            source_node = min(dict_node_length, key=lambda k: dict_node_length[k])
            del dict_node_length[source_node]

            for node_dist in self.edgelist[source_node]:
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                #edge relaxation
                if distance[adjnode] > distance[source_node] + length_to_adjnode:
                    distance[adjnode] = distance[source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]


        for i in range(self.node_count):
            print('Source Node (' + str(source) ') -> Destination Node (' + str(i) + ')  : ' + str(distance[i]))




def main():
    pass


if __name__ == "__main__":
    main()



