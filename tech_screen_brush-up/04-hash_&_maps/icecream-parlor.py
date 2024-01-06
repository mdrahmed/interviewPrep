# icecream-parlor or two sum
# Basic solution: using 2 loops
def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1,j+1]

# Time complexity: O(n^2)

 
# Optimized solution using hashmap
def icecreamParlor(m, arr):
    hm = {}
    for i in range(len(arr)):
        if m-arr[i] in hm:
            return [hm[m-arr[i]], i+1]
        else:
            hm[arr[i]] = i+1

# Time Complexity: O(n) 
