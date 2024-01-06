'''
Given a list of valid English words, build an anagram server that can spit out all the anagrams of a word
Solution: Sort each string and check with the given word which is also sorted.
Time complexity: O(nlogn)
'''

strr = "rates"
strs = ['aster', 'stare', 'tears', 'tears', 'abc', 'efg']
ans = []
sorted_s = ''.join(sorted(strr))
for w in strs:
    sorted_w = ''.join(sorted(w))
    if sorted_w == sorted_s:
        ans.append(w)

print(ans)

