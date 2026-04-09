"""
# RemoveSandwichedNegatives

Given an array that alternates between positive and negative numbers, modify it in-place to remove any negative number that is preceded and followed by the same positive value. Return the new length of the array.

As a result of the deletions, the array may be shorter. However, don't modify the actual size of the array. Simply return the new size. It doesn't matter what the array contains after the new size.

Example 1:
Input: [3, -1, 3, 4, -2, 5]
Output: 5
Explanation: -1 is removed because it's between two 3s. Final array: [3, 3, 4, -2, 5]

Example 2:
Input: [2, -3, 4, -5, 4]
Output: 4
Explanation: -5 is between two 4s, so it's removed. Final array: [2, -3, 4, 4]

Example 3:
Input: [1, -1, 1]
Output: 2
Explanation: -1 is removed because it's between two 1s. Final array: [1, 1]

Constraints:

- Array alternates between positive and negative numbers
- `1 ≤ arr.length ≤ 10^5`
- `-10^9 ≤ arr[i] ≤ 10^9 (arr[i] ≠ 0)`

"""


# TO: O(n), SO: O(1)
def remove_sandwiched_negatives(arr):
    left = 1
    cnt = 0
    while left < len(arr) - 1:
        if arr[left] < 0 and (arr[left - 1] == arr[left + 1]):
            cnt += 1
            right = left + 1
            while right < len(arr):
                arr[right - 1] = arr[right]
                right += 1
        left = left + 1

    return len(arr) - cnt


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([3, -1, 3, 4, -2, 5], 5),
        # Example 2 from the book
        ([2, -3, 4, -5, 4], 4),
        # Example 3 from the book
        ([1, -1, 1], 2),
        # Additional test cases
        ([5, -2, 5], 2),
        ([10, -5, 10], 2),
        ([7, -3, 7], 2),
        ([8, -4, 8], 2),
        ([9, -6, 9], 2),
        ([6, -1, 6], 2),
        ([4, -7, 4], 2),
        ([11, -8, 11], 2),
    ]

    for i, (arr, expected) in enumerate(tests):
        result = remove_sandwiched_negatives(arr)
        print(f"Case {i+1}: arr={arr}, expected={expected}, got={result}")
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
