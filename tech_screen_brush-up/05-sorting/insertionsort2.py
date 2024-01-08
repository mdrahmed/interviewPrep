# Insertion sort 2 is just using the idea of insertion sort 1 and do it for every element

def insertionSort2(n, arr):
    # As the 0th position is already sorted, I started from index 1
    for j in range(1, len(arr)):
        # getting last index value within i & j
        last_ele = arr[j]
        i = j # performing insertion sort within the subarray i & j
        while i > 0 and arr[i-1] > last_ele:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = last_ele
        print(*arr) # asterisk is used to print elements with space

# Time complexity: O(n^2)
