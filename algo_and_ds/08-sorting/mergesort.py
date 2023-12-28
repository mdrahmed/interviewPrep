'''
Merge sort is a divide and conquer technique to sort the array. It divides the array into halves and then sort those halves recursively.
Time complexity of merge sort is O(nlogn)
'''

def mergesort(arr, s, e):
    if e-s+1 <= 1:
        return arr
    m = (s+e)/2
    mergesort(arr,s,m)
    mergesort(arr,m+1,e)
    merge(arr,s,m,e)
    return arr

# merging two sorted arrays into original array
def merge(arr,s,m,e):
    L, R = arr[s:m+1], arr[m+1:e+1]
    i=0
    j=0
    k=s
    while i<len(L) and j<len(R):
        if L[i] <= R[i]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # If one half has any element left
    while i<len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j<len(R):
        arr[k] = R[i]
        j += 1
        k += 1

