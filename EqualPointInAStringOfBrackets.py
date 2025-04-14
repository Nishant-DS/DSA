def findIndex(str):
    opening_braces = closing_braces = 0
    n = len(str)

    for i in range(n):
        if str[i] == ")":
            closing_braces += 1
    
    for i in range(n):
        if opening_braces == closing_braces:
            return i
        if str[i] == '(':
            opening_braces += 1
        
        elif str[i] == ')':
            closing_braces -= 1
    
    return -1

str = ')'

print(findIndex(str=str))
     
        