"""
BookChapter 27: Two Pointers: 2-Sum

# 2-Sum

Given a sorted array of integers, `arr`, return whether there are two _distinct_ indices, `i` and `j`, such that `arr[i] + arr[j] = 0`.

Example 1:
Input: arr = [-5, -2, -1, 1, 1, 10]
Output: true
Explanation: The elements -1 and 1 sum to zero.

Example 2:
Input: arr = [-3, 0, 0, 1, 2]
Output: true
Explanation: The two 0s sum to zero.

Example 3:
Input: arr = [-5, -3, -1, 0, 2, 4, 6]
Output: false
Explanation: No two elements sum to zero.

Constraints:

- arr is sorted in ascending order
- 0 ≤ arr.length ≤ 10^6
- -10^9 ≤ arr[i] ≤ 10^9


Idea:
We can have 3 different approach for this problem:
1. Using nested loops, with 2 loops we can find the indices => TO: O(n^2)
2. Using hashmap we can keep one value and then check if any other value adds to 0 => TO: O(n)
3. As the array is sorted, we can traverse the array with 2 pointers, start and end
  - If sum is greater than 0 then it means, we need to reduce the sum so we move left. 
  - If the sum is less than 0 then we move the start pointer to right so that the sum gets closer to 0. => TO: O(n)
"""

def twoSum(nums):
  start, end = 0, len(nums) - 1
  while(start < end):
    if (nums[start] + nums[end] > 0):
      end -= 1
    elif (nums[start] + nums[end] < 0):
      start += 1
    else:
      return True
  
  return False


### Testing Phase ###
def run_tests():
  tests = [
      # Example 1 from the book
      ([-5, -2, -1, 1, 1, 10], True),
      # Example 2 from the book
      ([-3, 0, 0, 1, 2], True),
      # Example 3 from the book
      ([-5, -3, -1, 0, 2, 4, 6], False),
      # Edge case: empty array
      ([], False),
      # Edge case: array with one element
      ([0], False),
      # Edge case: array with two elements that sum to zero
      ([-1, 1], True),
      # Edge case: array with two elements that do not sum to zero
      ([-1, 2], False),
      # Edge case: array with multiple pairs that sum to zero
      ([-2, -1, 0, 1, 2], True)
  ]

  for i, (nums, expected) in enumerate(tests):
    result = twoSum(nums)
    print(f"twoSum({nums}) = {result}, expected: {expected}")
    assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
  
  print("All test cases passed!")

run_tests()