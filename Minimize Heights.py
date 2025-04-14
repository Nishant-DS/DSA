def getMinDiff(k, arr):
    n = len(arr)
    arr.sort()
    min_diff = arr[n - 1] - arr[0]
    
    for i in range(n - 1):
        curr_min = max(arr[i] + k, arr[n - 1] - k) - min(arr[0] + k, arr[i + 1] - k)
        min_diff = min(min_diff, curr_min)
    
    return min_diff