def longestCommonPrefix(strs):
    n = len(strs)
    if len(strs[0]) == 0:
        return ""
    
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if len(strs[j]) == i:
                return strs[0][0:i]
            if strs[j][i] != c:
                return strs[0][0:i]
        
        if i == len(strs[0])-1:
            return strs[0]
        
        
    
        
        
