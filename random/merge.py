'''
BookChapter 27: Two PointersMerge Two Sorted Arrays


# Merge Two Sorted Arrays

Given two sorted arrays of integers, `arr1` and `arr2`, return a new array that contains all the elements in `arr1` and `arr2` in sorted order, including duplicates.

Example 1:
Input:
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 4]
Output: [1, 2, 3, 4, 4, 4, 5]
Explanation: All elements are merged in sorted order.

Example 2:
Input:
arr1 = [-1]
arr2 = []
Output: [-1]
Explanation: When one array is empty, the result is just the other array.

Example 3:
Input:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Constraints:

- arr1 and arr2 are sorted in ascending order
- 0 ≤ arr1.length, arr2.length ≤ 10^6
- -10^9 ≤ arr1[i], arr2[i] ≤ 10^9
'''

# # Edge cases,
# 1. empty arrays
# 2. 1 element in 1 array and other empty
# 3. both array has 1 element
# 4. both array has same elements
# 5. 1 array is strictly smaller than the other array

# TO & SO: O(m+n)


def merge(arr1, arr2):
  res = []
  p1 = p2 = 0
  while (p1 < len(arr1) and p2 < len(arr2)):
    if arr1[p1] < arr2[p2]:
      res.append(arr1[p1])
      p1 += 1
    else:
      res.append(arr2[p2])
      p2 += 1
  
  while (p1 < len(arr1)):
    res.append(arr1[p1])
    p1 += 1
  
  while (p2 < len(arr2)):
    res.append(arr2[p2])
    p2 += 1
  
  return res

### Testing Phase ###
def run_tests():
  tests = [
      # Example from the book
      ([1, 3, 4, 5], [2, 4, 4], [1, 2, 3, 4, 4, 4, 5]),
      # Additional test cases
      ([], [], []),
      ([-1], [], [-1]),
      ([1], [2], [1, 2]),
      ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
      ([1, 2], [3, 4], [1, 2, 3, 4]),
      ([1, 2], [1, 2], [1, 1, 2, 2]),
      ([1], [1], [1, 1]),
      ([1], [0], [0, 1]),
      ([0], [1], [0, 1]),
      ([1], [-1], [-1, 1]),
      ([-1], [1], [-1, 1]),
      ([0], [-1], [-1, 0]),
      ([-1], [0], [-1, 0]),
      ([1000000000], [-1000000000], [-1000000000, 1000000000])
  ]
  for arr1, arr2, want in tests:
    got = merge(arr1, arr2)
    print(f"merge({arr1}, {arr2}): got: {got}, want: {want}")
    assert got == want, f"\nmerge({arr1}, {arr2}): got: {got}, want: {want}\n"

run_tests()