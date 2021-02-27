import sys

INF = float("inf")

def createMatrix(n, m):
    a = {}
    for i in range(0, n):
        a[i] = {}
        for j in range(0, m):
            a[i][j] = INF
    return a


# A utility function to print the solution
def printSolution(graph):
    V = len(graph)
    for i in range(V):
        for j in range(V):
            if graph[i][j] == INF:
                print("%7s   " % ("∞∞"), end =" "),
            else:
                print("%7d\t" % (graph[i][j]), end =" "),
            if j == V - 1:
                print("")


def floydWarshall(graph):
    V = len(graph)
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                graph[i][j] = min(graph[i][j],
                                  graph[i][k] + graph[k][j]
                                  )
    printSolution(graph)


if __name__ == '__main__':
    g = createMatrix(5, 5)
    g[0][1] = 1
    g[1][2] = 3
    g[1][4] = -1
    g[2][1] = 3
    g[2][0] = -4
    g[4][2] = 4
    g[4][3] = 3
    (floydWarshall(g))
