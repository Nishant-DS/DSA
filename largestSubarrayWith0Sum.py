def maxlen(arr):
    n = len(arr)
    hsh = {0:-1}
    mx_len = 0
    sum = 0

    for i in range(n):
        sum += arr[i]
        if sum not in hsh:
            hsh[sum] = i
        else:
            mx_len = max(i - hsh[sum], mx_len)
    
    return mx_len
    
