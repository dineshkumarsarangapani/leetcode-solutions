def scores(D):
    A = 0
    B = 100
    for y in D.keys():
        if B == D[y]:
            A = A + 1
        if B > D[y]:
            A = 1
            B = D[y]
    print(A)
    print(B)

def marks(m):
    key = -1
    value = 0
    for i in m.keys():
        if m[i] > value:
            value = m[i]
            key = i
    return key


if __name__ == '__main__':
    #D = {"chennai": 50, "mad": 54, "coim": 12, "ddd": 99, "xx": 10, "yy": 10}
    #scores(D)
    m = {64:2, 100:1, 44:1}
    print(marks(m))
   #    STN[station_name][monday]