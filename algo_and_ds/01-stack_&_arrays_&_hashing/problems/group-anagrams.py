# link: https://leetcode.com/problems/group-anagrams/

# Brute-force solution: sorting each value and then comparing with the rest
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        for w in range(len(strs)):
            s = ''.join(sorted(strs[w]))
            res = []
            if strs[w] != "-1": 
                res.append(strs[w])
                strs[w] = "-1"
                for j in range(w+1, len(strs)):
                    k = ''.join(sorted(strs[j]))
                    if s == k:
                        res.append(strs[j])
                        strs[j] = "-1"
                ans.append(res)
        return ans


# Optimal Solution: Using hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for w in strs:
            sorted_w = ''.join(sorted(w))
            if sorted_w in hashmap.keys():
                hashmap[sorted_w].append(w)
            else:
                # Add a list [w] 
                hashmap[sorted_w] = [w]
        return hashmap.values()

# Optimal solution: Using default dictionary
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for w in strs:
            sorted_w = ''.join(sorted(w))
            hashmap[sorted_w].append(w)
        return hashmap.values()

