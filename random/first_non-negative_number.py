"""
Given a sorted array of integers (duplicates allowed), find the index of the first occurrence of a non-negative number (a number greater than or equal to `0`). If no such number exists, return `-1`.

Example 1:
Input:
arr = [-21, -15, -9, -5, -5, -1, -1, 0, 0, 4, 7, 12, 21]
Output:
7
Explanation:
The first non-negative number is 0, which occurs at index 7.

Example 2:
Input:
arr = [-5, -4, -3, -2, -1]
Output:
-1
Explanation:
There are no non-negative numbers in the array.

Example 3:
Input:
arr = [0, 1, 2, 3, 4, 5]
Output:
0
Explanation:
The first non-negative number is 0, which occurs at index 0.

Constraints:

- The array is sorted in ascending order
- The array length is at most `10^5`
- Each element is an integer in the range `[-10^9, 10^9]`

Idea:
This is a binary search problem. The left pointer points to negative values and right pointer porints to positive values. The first positive number would be present when left and right are next to each other so, condition is check until right - left > 1. At the end, if right pointer contains the positive value then it's the result otherwise -1

Edge cases to consider:
1. Empty array: []
2. Array with only zero: [0]
3. Array with only negative numbers: [-1, -2, -3]
4. Array with first element being non-negative: [0, 1, 2, 3, 4]
"""


# TO: O(logn), SO: O(1)
def binary_search(arr):
    n = len(arr)
    if not arr:
        return -1
    if arr[0] >= 0:
        return 0

    left, right = 0, n - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if arr[mid] < 0:
            left = mid
        else:
            right = mid

    return right if arr[right] >= 0 else -1


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([-21, -15, -9, -5, -5, -1, -1, 0, 0, 4, 7, 12, 21], 7),
        # Example 2 from the book
        ([-5, -4, -3, -2, -1], -1),
        # Example 3 from the book
        ([0, 1, 2, 3, 4, 5], 0),
        # Additional test cases
        ([], -1),
        ([0], 0),
        ([-1], -1),
        ([-1, -2, -3], -1),
        ([0, 1, 2], 0),
    ]

    for i, (arr, expected) in enumerate(tests):
        result = binary_search(arr)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: expected {expected}, got {result}")
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
