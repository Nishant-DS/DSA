def reverseWords(s):
    n = len(s)
    res = ""
    str = ""
    for i in range(n):
        
        if s[i] == " ":
            if res == "":
                res = str if str != "" else res
            else:
                res = str + " " +res if str != "" else res
            str = ""
            
        else:
            str += s[i]
    
    if res == "":
        res = str if str != "" else res
    else:
        res = str + " " +res if str != "" else res
    
    return res
