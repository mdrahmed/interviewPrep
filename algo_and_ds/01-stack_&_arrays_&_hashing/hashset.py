'''
set() stores unique elements in python.
Common ops in set,
    1. Insert - hashset.add(element)
    2. Intersaction - hashset1.intersaction(hashset2) or, hashset1 & hashset2
    3. Difference - hashset1.difference(hashset2) or, hashset1 - hashset2
        It will get the elements of hashset1 which is present in hashset2
hashset.clear() to remove all elements in set.
'''

set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)
 
# Intersection using
# intersection() function
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)
# Intersection using "&" operator
set3 = set1 & set2 
print("\nIntersection using '&' operator")
print(set3)


# Difference of two sets
# using difference() function
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)
# Difference of two sets using '-' operator
set3 = set1 - set2 
print("\nDifference of two sets using '-' operator")
print(set3)
