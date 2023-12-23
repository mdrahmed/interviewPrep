
## Time complexity
Python uses Timsort and this sorting has `O(nlogn)` time complexity.

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

