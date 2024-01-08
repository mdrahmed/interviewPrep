# link: https://www.hackerrank.com/challenges/quicksort2/problem
results = []
def quickSort(arr):
    if len(arr) < 2:
        return arr
    global results
    left = []
    right = []
    pivot = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    left = quickSort(left)
    right = quickSort(right)
    results.append(left + [pivot] + right)
    return left + [pivot] + right

# Time Complexity: O(nlogn)
