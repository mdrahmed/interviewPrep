'''
Given two strings, s and b, find all permutations of s within b
'''
def findAllPermutation(s,b):
    ans = []
    sorted_s = ''.join(sorted(s))
    for i in range(len(b) - len(s)+1):
        new_per = b[i:i+len(s)]
        sorted_new_per = ''.join(sorted(new_per))
        if sorted_new_per == sorted_s:
            ans.append(new_per)
    return ans

s = "cba"
b = "aaabccbabbacbbacklllbcacabcba"
print(findAllPermutation(s,b))
