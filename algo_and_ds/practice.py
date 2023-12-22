
from typing import Counter

cnts = Counter("Beehove")
print("chars: ",cnts) 
for c in cnts.keys():
    print(c, cnts[c])
