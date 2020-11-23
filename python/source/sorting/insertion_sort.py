def my_insertion_sort(arr):
    length = len(arr)
    i = 1
    while i < length:
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            print("Intermediate ---> ", arr)
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x
        i += 1
    return arr


def recrr_insertion_sort(arr, n):
    if n > 0:
        recrr_insertion_sort(arr, n - 1)
        x = arr[n]
        j = n - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x


if __name__ == '__main__':
    arr = [6, 4, 1]
    sortValue = my_insertion_sort(arr)
    print(sortValue)

    # recurrsion
    recrr_insertion_sort(arr, len(arr) - 1)
    print(arr)
