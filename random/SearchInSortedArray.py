'''
BookChapter 29: Binary Search: Search in Sorted Array

# Search in Sorted Array

Given a sorted array of integers, `arr`, and a target value, `target`, return the target's index if it exists in the array or `-1` if it doesn't.

Example 1: arr = [-2, 0, 3, 4, 7, 9, 11], target = 3
Output: 2. The target 3 is at index 2.

Example 2: arr = [-2, 0, 3, 4, 7, 9, 11], target = 2
Output: -1. The target 2 is not in the array.

Example 3: arr = [1, 2, 3], target = 1
Output: 0. The target 1 is at index 0.

Constraints:

- `0 ≤ arr.length ≤ 10^6`
- `-10^9 ≤ arr[i], target ≤ 10^9`
- `arr` is sorted in ascending order, without duplicates
'''

# Idea: Use binary search to find the target in the sorted array.
# TO: O(logn), SO: O(1)

def binarySearch(arr, target):
  left = 0
  right = len(arr) - 1
  while(left <= right):
    mid = left + (right - left) // 2
    if(arr[mid] < target):
      left = mid + 1
    elif(arr[mid] > target):
      right = mid - 1
    else:
      return mid
  
  return -1


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([-2, 0, 3, 4, 7, 9, 11], 3, 2),
        # Example 2 from the book
        ([-2, 0, 3, 4, 7, 9, 11], 2, -1),
        # Example 3 from the book
        ([1, 2, 3], 1, 0),
        # Edge case - empty array
        ([], 1, -1),
        # Edge case - target not in array
        ([1, 2, 3], 4, -1),
        # Edge case - target is the last element
        ([1, 2, 3], 3, 2)
    ]
    for i, (arr, target, expected) in enumerate(tests):
        result = binarySearch(arr, target)
        print(f"Test case {i+1}: arr={arr}, target={target}, expected={expected}, got={result}")
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")

run_tests()