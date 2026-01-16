def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])
    res = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    res.extend(L[i:]); res.extend(R[j:])
    return res
