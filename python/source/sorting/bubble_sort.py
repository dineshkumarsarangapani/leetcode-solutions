def bubble_sort(arr):
    length = len(arr)
    while True:
        swapped = False
        for i in range(1, length - 1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
        else:
            print(arr) # print and see how sort is working
    return arr


if __name__ == '__main__':
    arr = [5, 2, 1, 3, 4]
    sortedVal = bubble_sort(arr)
    print(sortedVal)
