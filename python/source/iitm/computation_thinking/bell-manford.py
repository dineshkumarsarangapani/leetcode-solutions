
masterGraph = []

def addEdge(src_v, des_v, weight):
    masterGraph.append([src_v, des_v, weight])


def bellManFord(no_of_vertex, graph, source):
    ## mark all the distance as inf
    dist = [float("Inf")] * no_of_vertex
    dist[source] = 0
    #print(dist)

    for i in range(no_of_vertex-1):
        print(i)
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                print("Source:", u, " dest:", v, " dist:", dist)


    ## Check for negative cycles
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph has negative cycles");
            return
    return dist


def add_sample_edge():
    masterGraph = []
    addEdge(0, 1, 10)
    addEdge(0, 7, 6)
    addEdge(0, 4, 4)
    addEdge(1, 2, 1)
    addEdge(2, 7, -8)
    addEdge(2, 5, -10)
    addEdge(5, 6, 1)
    addEdge(5, 4, 5)
    addEdge(7, 6, -2)
    addEdge(6, 3, 4)
    addEdge(3, 2, 20)
    addEdge(3, 4, -3)
    return 8


def add_aq3(x):
    masterGraph = []
    addEdge(0, 1, 6)
    addEdge(0, 2, 5)
    addEdge(1, 3, 1)
    addEdge(1, 4, x)
    addEdge(2, 1, 3)
    addEdge(4, 2, 4)
    return 5



if __name__ == '__main__':
    #no_of_vertex = add_sample_edge()
    #For what values of x can we use the Bellman-Ford algorithm to find the shortest path from a source vertex 0
    # to every other vertex in the graph given below?
    # the value of x must be (-7, inf) open braces
    no_of_vertex = add_aq3(-1)
   # print(masterGraph)
    dis = bellManFord(no_of_vertex, masterGraph, 0)
    print(dis)
