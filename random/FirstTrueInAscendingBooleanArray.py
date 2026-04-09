"""
You are given a sorted ascending boolean array `arr` consisting of `False` and `True` values. Find the index of the first occurrence of `True` in the array. If no `True` exists, return -1.

Example 1:
Input:
arr = [False, False, False, True, True, True]
Output:
3
Explanation:
The first True occurs at index 3.

Example 2:
Input:
arr = [False, False, False, False]
Output:
-1
Explanation:
There are no True values in the array.

Example 3:
Input:
arr = [True, True, True]
Output:
0
Explanation:
The first True occurs at index 0.

Constraints:

- The array is sorted in ascending order (`False` comes before `True`)
- The array length is at most `10^5`
- Each element is either `True` or `False`

"""

### Edge Cases ###
"""
Edge cases I considered:
Works fine with these cases if just the loop => arr contains only true or false, if arr contains true or false, if arr contains only 1 true or 1 false, or if arr contains really large number of values to the range 10^ 5.

Edge cases I missed: 
What about empty array, first element being True, and the check before returning right. Also, if last element is false, we don’t need to run the loop. => Add conditions to fix these
"""


## TO: O(logn), SO: O(1)
def first_true(arr):
    n = len(arr)
    if n == 0 or not arr[n - 1]:
        return -1
    if arr[0]:
        return 0

    left, right = 0, n - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if not arr[mid]:
            left = mid
        else:
            right = mid

    return right if arr[right] else -1


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([False, False, False, True, True, True], 3),
        # Example 2 from the book
        ([False, False, False, False], -1),
        # Example 3 from the book
        ([True, True, True], 0),
        # Edge case: empty array
        ([], -1),
        # Edge case: first element is True
        ([False, False, True], 2),
        # Edge case: last element is False
        ([False, False, False], -1),
        # Edge case: large array with no True values
        ([False] * 10**5, -1),
        # Edge case: large array with all True values
        ([True] * 10**5, 0),
    ]

    for i, (arr, expected) in enumerate(tests):
        result = first_true(arr)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
