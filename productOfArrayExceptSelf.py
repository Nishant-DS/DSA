def productExceptSelf(arr):
    n = len(arr)
    prod = 1
    pre_prod = [0]*n
    suff_prod = [0]*n
    res = [0]*n

    for i in range(n):
        prod *= arr[i]
        pre_prod[i] = prod
    
    prod = 1
    for i in range(n-1, -1, -1):
        prod *= arr[i]
        suff_prod[i] = prod
    res[0] = suff_prod[1]
    res[n-1] = pre_prod[n-2]

    for i in range(1,n-1):
        res[i] = pre_prod[i-1]*suff_prod[i+1]
    
    return res
