def rotLeft(a, d):
    # Write your code here
    arr1 = a[:d]
    arr2 = a[d:]
    return arr2+arr1
