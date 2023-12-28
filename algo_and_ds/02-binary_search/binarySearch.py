


def binarysearch(arr, target):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2
        if target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return mid
    return -1

