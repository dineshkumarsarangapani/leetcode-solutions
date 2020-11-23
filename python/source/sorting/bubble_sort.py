def bubble_sort(arr):
    length = len(arr)
    while True:
        swapped = False
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
        else:
            pass
           # print(arr) # print and see how sort is working
    return arr


if __name__ == '__main__':
    arr = [6, 4, 1]
    sortedVal = bubble_sort(arr)
    print(sortedVal)
