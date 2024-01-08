# Link: https://www.hackerrank.com/challenges/insertionsort1/problem

# In insertion sort part 1,
# Take last element and put it into its correct position
# Assuming all the elements before it are sorted
def insertionSort1(n, arr):
    # Write your code here
    last_ele = arr[-1]
    i = n-1
    while i > 0 and arr[i-1] > last_ele:
        arr[i] = arr[i-1]
        i -= 1
        print(*arr) # asterisk is used to print elements with space
    arr[i] = last_ele
    print(*arr)
