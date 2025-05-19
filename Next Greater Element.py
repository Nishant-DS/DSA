def nextLargerElement(arr):
    n = len(arr)
    stack = []
    res = []

    for i in range(n-1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        
        greater = stack[-1] if len(stack) > 0 else -1
        res.append(greater)
        stack.append(arr[i])

    return res[::-1]


arr = [4, 5, 2, 9, 7, 8, 6, 10]

print(nextLargerElement(arr))


#[5, 9, 9, 10, 8, 10, 10, -1]
