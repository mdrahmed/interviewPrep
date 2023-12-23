
## Brute force
#def threeSumZero(arr):
#    for i in range(len(arr)-2):
#        for j in range(i+1, len(arr)-1):
#            for k in range(j+1, len(arr)):
#                if arr[i] + arr[j] + arr[k] == 0:
#                    return [arr[i], arr[j], arr[k]]
#    return None
#
#

#Time complexity - O(n^3)
#
### Solution: 2 pointers
#[0, 1, -1, 2, -2]
#[0, -1, 1, 2, 3]
#0

'''

'''

def threeSumZero(arr):
    arr.sort()
    for i in range(len(arr)):
        l = i+1
        r = len(arr)-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == 0:
                return [arr[i], arr[l], arr[r]]
            elif arr[i] +arr[l] + arr[r] > 0:
                r -= 1
            else:
                l += 1
    return None


print(threeSumZero([0,1,-1,2,-2]))
print(threeSumZero([4,1,-1,2,-2]))
print(threeSumZero([]))
