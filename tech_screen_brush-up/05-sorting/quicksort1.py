# Take the 1st element as pivot and compare with every element if it it smaller then put it to left array otherwise right.

def quickSort(arr):
    left = []
    right = []
    pivot = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    return left + [pivot] + right
