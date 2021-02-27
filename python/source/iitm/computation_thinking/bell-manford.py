
masterGraph = []

def addEdge(src_v, des_v, weight):
    masterGraph.append([src_v, des_v, weight])


def bellManFord(no_of_vertex, graph, source):
    ## mark all the distance as inf
    dist = [float("Inf")] * no_of_vertex
    dist[source] = 0
    #print(dist)

    for _ in range(no_of_vertex-1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w


    ## Check for negative cycles
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph has negative cycles");
            return
    return dist


if __name__ == '__main__':
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

   # print(masterGraph)
    dis = bellManFord(8, masterGraph, 0)
    print(dis)
