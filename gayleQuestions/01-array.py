'''
Given two arrays, sorted and distinct, how would find the number of elements in common.
My approach: 
    Optimal solution: 
        1. using two pointers
        2. using set, this can be done
    Brute-force approach:
        1. Using loops
'''

# Brute force approach:
print("Brute force approach: ")
arr1 = [1,2,5,7]
arr2 = [2,3,5,7,8]
ans = []
for i in arr1:
    for j in arr2:
        if i == j:
            ans.append(i)
print(ans)

# optimal solution 1: using set
print("Optimal solution 1 using set:")
arr1_set = set(arr1)
arr2_set = set(arr2)

print(arr1_set & arr2_set)

# optimal solution 2: using two pointers
print("Optimal solution 2 - using pointer: ")
l = 0
r = 0
while l < len(arr1) and r < len(arr2):
    if arr1[l] == arr2[r]:
        print(arr1[l])
        l += 1
        r += 1
    elif arr1[l] < arr2[r]:
        l += 1
    else:
        r += 1



