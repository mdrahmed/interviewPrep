'''
In quick sort, we get a random value and compare it with the other values.
I use the rightmost value as the pivot value.
    1. We have 2 pointers left and right
    2. Place the values less than or equal to pivot to the left most side.
    3. Right pointer will iterate thorough the array 
    4. If a value is smaller than pivot value then it right pointer value will be swaped with the left pointer value
    5. Then left pointer will move forward
    6. Now, swap the pivot value with left pointer value. 
        Because all the value before left pointer is less than pivot value and all values at right of left pointer is greater.
    7. Now, run quicksort on left and right side of pivot value.

Time complexity is O(nlogn) on average but its O(n^2) in worst case.
'''

def quicksort(arr, s, e):
    if e-s+1 <= 1:
        return
    pivot = arr[e]
    left = s
    for i in range(s,e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    quicksort(arr, s, left-1)
    quicksort(arr, left+1, e)
    
    return arr
