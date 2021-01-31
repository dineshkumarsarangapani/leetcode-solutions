def dfs(graph, parents, sequence, i):
    sequence.append(i)
    for j in graph.keys():
        if graph[i][j] == 1 and j not in parents.keys():
            parents[j] = i
            parents, sequence = dfs(graph, parents, sequence, j)

    return parents, sequence


def createMatrix(n, m):
    a = {}
    for i in range(0, n):
        a[i] = {}
        for j in range(0, m):
            a[i][j] = 0
    return a


if __name__ == '__main__':
    graph = createMatrix(6, 6)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[0][3] = 1
    graph[3][0] = 1
    graph[1][4] = 1
    graph[4][1] = 1
    graph[2][1] = 1
    graph[1][2] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[2][5] = 1
    graph[5][2] = 1
    p ={}
    s =[]
    start = 3
    p[start] = -1
    p, s = dfs(graph, p, s, start)
    #print(s)
    #print(p)
    #print(p.keys())
    sorted_v = list(p.keys())
    sorted_v.sort()
    #print(sorted_v)
    b = createMatrix(6, 6)
    for i in p.keys():
        if i != 3:
            parent= p[i]
            b[parent][i] = 1
    pp, ss = dfs(b, p, s, start)
    print(pp)

