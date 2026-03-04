# Common ideas

## Python Quick-check
**Core DS & techniques to quick check**
Hashmap, Hashset, PrefixSum

**Python functions that requires to remember:**
```
ch.lower(), str.lower()
ch.isalpha(), str.isalpha()
```

Other functions:
```
str.isalnum(), ch.isalnum()
str.upper(), ch.upper()
```
To convert string into lowercase by removing punctuation, commas and spaces:
`str = ""join(ch for ch in s if(ch.isalpha())`

Actually, strings in Python are immutable. When you remove punctuation or convert to lowercase, you are creating new strings. So, Space complexity to remove or checking if its palindrome with `s == s[::-1]` is creating new string, so, `SO = O(n)`

In python,
```
    while not s[start].isalpha(): start += 1
    while not s[end].isalpha(): end -= 1
```

## Time complexity
**arr.sort()**
Python uses Timsort and this sorting has `O(nlogn)` time complexity.

**Binary search**
The time complexity of a tree is the no of branches raised to the power of heights.
If height is h and the branches are 2 then time complexity is O(2^h)

## Basics
Reverse for loop python,
```
for t in range(len(temperatures)-1, -1, -1):
    print(temperatures[i])

for item in my_list[::-1]:
    print item
```

## strings
Get the character index,
```
index = ord(word[i]) - ord('a')
```

**Count the total number of chars appeared**
```
from typing import Counter
cnts = Counter("Beehove")
for c in cnts.keys():
    print(c,":", cnts[c])
```

## Arrays
Convert array to set,
arrSet = set(arr)
