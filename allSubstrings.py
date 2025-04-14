def getSubstr(s, i):
    if i == len(s)-1:
        return [[s[i]]]
    res = []
    substr = getSubstr(s, i+1)
    for a in substr[0]:
        res.append(s[i]+a)
    res.append(s[i])
    res = [res]
    for a in substr:
        res.append(a)
    print(res)
    return res

def allSubstrings(s):
    res = []
    for a in getSubstr(s,0):
        res += a
    return res
print(allSubstrings("abc"))