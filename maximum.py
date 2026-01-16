def find_max(arr):
    if not arr:
        raise ValueError("Empty array")
    mx = arr[0]
    for x in arr[1:]:
        if x > mx:
            mx = x
    return mx
