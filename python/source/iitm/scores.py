def scores(D):
    A=0
    B=0
    for y in D.keys():
        if B==D[y]:
            A = A+1
        if B > D[y]:
            A = 1
            B = D[y]
    print(A)
    print(B)

if __name__ == '__main__':
    D = {"chennai":50, "mad":54, "coim":12, "ddd":99, "xx":0}
    scores(D)

