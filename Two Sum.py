def twoSum(arr, target):
    n = len(arr)
    hsh = {}

    for i in range(n):
        if target - arr[i] in hsh:
            return True
        else:
            hsh[arr[i]] = i
    
    return False

arr = [1, 4, 45, 6, 10, 8]
target = 16
print(twoSum(arr, target))
