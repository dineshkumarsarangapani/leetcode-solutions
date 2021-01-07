def insertList(l, x):
    newList = []
    inserted = False
    for z in l:
        if not inserted and x < z:
            newList.append(x)
            inserted = True
        newList.append(z)
    if not inserted:
        newList.append(x)
    return newList


if __name__ == '__main__':
    l = [5,4,3,2,1]
    l = insertList(l, 5)
    l = insertList(l, 4)
    l = insertList(l, 3)
    l = insertList(l, 2)
    l = insertList(l, 1)
    print(l)
