'''
A hashtable doesn't allow keys or values to set to null but a hashmap does allow it.
In python a default dictionary is a hashtable - dict = {}
Common ops in dict python,
    1. Insert => hashtable["key"] = "value"
    2. Remove => hashtable.pop("item") - don't forget to provide the key names for removing the values
                 hashtable.popitem() - this will return the most last item
    3. search => hashtable["key"]
        Using loop:
            for k in hashtable: => it will give only keys
            for k in hashtable.keys() => give only keys
            for value in hashtable.values() => give only values
            for k,v in hashtable.items() => gives both keys and values

But a defaultdict(list) is a hashmap. 
    1. all same as hashtable  
'''
from collections import defaultdict

# hashtable
print("Hashtable:\n")
thisdict =	{}
thisdict["color"] = "red"
thisdict["value1"] = "a"
thisdict["value2"] = "b"
print(thisdict)
print(thisdict.pop("value2"))
print(thisdict.popitem())
thisdict["value3"] = "c"
thisdict["value4"] = "d"
for k,v in thisdict.items():
    print(k,v)

#hashmap - defaultdict
hashmap = defaultdict(list)
hashmap["v1"] = "a"
hashmap["v2"] = "b"
hashmap["v3"] = "c"
print("hashmap:\n",hashmap)
print(hashmap.pop("v2"))
print(hashmap.popitem())
for k,v in hashmap.items():
    print(k,v)

''' - PROBLEM - GROUP ANAGRAMS - TRY SOLVING THIS WITH A GAP OF 1 DAY
from collections import defaultdict

defaultdict

ans = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]
for s in strs:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord("a")] += 1
    ans[tuple(count)].append(s)

print(ans.values())
'''
