def sortByFreq(arr):
    hsh = {}

    for num in arr:
        if num in hsh:
            hsh[num] += 1
        else:
            hsh[num] = 1
    
    res = []
    for num in arr:
        res.append((num, hsh[num]))
    
    res.sort(key = lambda x : (-x[1], x[0]))

    return [tup[0] for tup in res]
