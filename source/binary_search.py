def binary_search(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid + 1
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
        else:
            return binary_search(array, mid + 1, high, x)
    else:
        return -1