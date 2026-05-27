"""
A _nested array_ is an array where each element is either:

1. An integer, or
2. A nested array (note that this is a recursive definition).

The _sum_ of a nested array is defined recursively as the sum of all its elements.
Given a nested array, `arr`, return its sum.

Example 1: arr = [1, [2, 3], [4, [5]], 6]
Output: 21

Example 2: arr = [[[[1]], 2]]
Output: 3

Example 3: arr = []
Output: 0

Example 4: arr = [[], [1, 2], [], [3]]
Output: 6

Example 5: arr = [-1, [-2, 3], [4, [-5]], 6]
Output: 5

Constraints:

- The array can be nested to depth at most 500
- Each integer in the array is between -10^9 and 10^9
- The total number of integers in the array (counting nested ones) is at most 10^5

"""

# TO: O(n) as all integers are processed once
# SO: O(d), d is the max depth of recursive calls


def recursive_sol(arr):
    if not arr:
        return 0
    res = 0
    for val in arr:
        if isinstance(val, int):
            res += val
        else:
            res += recursive_sol(val)

    return res


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([1, [2, 3], [4, [5]], 6], 21),
        # Example 2 from the book
        ([[[[1]], 2]], 3),
        # Example 3 from the book
        ([], 0),
        # Example 4 from the book
        ([[], [1, 2], [], [3]], 6),
        # Example 5 from the book
        ([-1, [-2, 3], [4, [-5]], 6], 5),
    ]

    for i, (arr, expected) in enumerate(tests):
        result = recursive_sol(arr)
        assert result == expected, f"Test case {i + 1} failed"
        print(
            f"Test case {i + 1}: {result == expected} (Expected: {expected}, Got: {result})"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
