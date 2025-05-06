def longestConsecutive(arr):
    n = len(arr)
    hsh = {}
    max_len = 1

    for i in range(n):
        hsh[arr[i]] = i
    
    for i in range(n):
        if arr[i] - 1 not in hsh:
            l = 1
            curr = arr[i] + 1
            while curr in hsh:
                l += 1
                curr += 1
            max_len = max(max_len, l)
    
    return max_len

arr = [15, 13, 12, 14, 11, 10, 9]
print(longestConsecutive(arr))