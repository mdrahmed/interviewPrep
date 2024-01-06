def isBalanced(s):
    # Using stack and hashmap 
    stack = []
    hm = {'(':')', '{':'}', '[':']'}
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if stack:
                if hm[stack.pop()] != c:
                    return "NO"
            else:
                return "NO"
    if stack:
        return "NO"
    return "YES"


#Time complexity: O(n)
