def hasTripletSum(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n):
        l = i+1
        r = n-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == target:
                return True
            elif arr[i] + arr[l] + arr[r] < target:
                l += 1
            else:
                r -= 1
    
    return False
