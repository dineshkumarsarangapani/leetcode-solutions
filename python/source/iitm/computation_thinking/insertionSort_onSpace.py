def insertion_sort(arr):
    def sortedList(l, x):
        newList = []
        inserted = False
        for z in l:
            if not inserted:
                if x<z:
                    newList.append(x)
                    inserted = True
            newList.append(z)
        if not inserted:
            newList.append(x)
        return newList
    sortedArr = []
    for a in arr:
        sortedArr = sortedList(sortedArr, a)
    return sortedArr

if __name__ == '__main__':
    a = [4,5,6,25,66,15,66]
    print(insertion_sort(a))