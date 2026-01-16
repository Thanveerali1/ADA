def linear_search(arr, key):
    for i, x in enumerate(arr):
        if x == key:
            return i    # index where found
    return -1         # not found
