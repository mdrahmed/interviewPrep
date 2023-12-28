# Common ideas

## Time complexity
**arr.sort()**
Python uses Timsort and this sorting has `O(nlogn)` time complexity.

**Binary search**
The time complexity of a tree is the no of branches raised to the power of heights.
If height is h and the branches are 2 then time complexity is O(2^h)

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
