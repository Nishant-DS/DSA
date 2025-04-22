def areKAnagrams(s1, s2, k):
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 != n2:
        return False
    hsh1 = {}
    hsh2 = {}
    cnt = 0
    for i in range(n1):
        if s1[i] not in hsh1:
            hsh1[s1[i]] = 1
        else:
            hsh1[s1[i]] += 1
    
    for i in range(n2):
        if s2[i] not in hsh2:
            hsh2[s2[i]] = 1
        else:
            hsh2[s2[i]] += 1
        if s2[i] not in hsh1 or hsh2[s2[i]] > hsh1[s2[i]]:
                cnt += 1
                if cnt > k:
                    return False
    
    
    return True
