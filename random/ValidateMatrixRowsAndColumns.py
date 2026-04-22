"""
A square matrix of size `n x n` is considered valid if every row and every column includes all the integers from `1` to `n`, with no missing or duplicate values.

Write a function that takes an `n x n` integer matrix as input and returns `true` if the matrix satisfies this condition. Otherwise, return `false`.

Example 1:
Input: matrix = [
  [2, 3, 1],
  [1, 2, 3],
  [3, 1, 2]
]
Output: true
Explanation: Each row and column contains the values 1, 2, and 3 exactly once.

Example 2:
Input: matrix = [
  [4, 4, 4],
  [2, 1, 3],
  [3, 2, 1]
]
Output: false
Explanation: The first row and first column are missing some values between 1 and 3, and there are duplicates.

Example 3:
Input: matrix = [
  [1]
]
Output: true
Explanation: A 1x1 matrix containing only 1 is valid.

Constraints:

- `0 <= matrix.length <= 100`
- `matrix.length == matrix[i].length`
- `-10^9 <= matrix[i][j] <= 10^9`

We can traverse each row and column separately. Each time we add values to a set and for each value we check whether it's within range 1 <= mat[i][j] <= n

## Edge cases: it must be a square matrix
[] => valid
[
  []
] => invalid (not a square matrix)
[
  [1]
] => valid
[
  [],[]
  [],[]
] => invalid


## Problem Solving Approach:
Iterate the matrix row by row and column by column, and for each row and column.
And use a set to check for duplicates and if not within valid range (1 to n) then return false.


Note:
- As it’s square matrix and if we use n = len(mat) for everything, then for [[]], n would be 1, and we’d try to access mat[0][0] — but mat[0] is an empty list, so we’d get an index out of bounds error.
    For matrix, the first guard is always what happens when matrix is empty. For square matrix add another guard to check if matrix is not square e.g., if len(mat) != len(mat[0])
- Think about edge case after approach is defined to add guards/conditions at the beginning of the function to handle those edge cases.

"""

# TO: O(n*n) + O(n*n) => O(n^2)
# SO: O(n) + O(n) => O(n)


def solution(mat):
    if not mat:
        return True
    if len(mat) != len(mat[0]):
        return False

    n = len(mat)

    # Check row
    for r in range(n):
        numSet = set()
        for c in range(n):
            if mat[r][c] in numSet or mat[r][c] < 1 or mat[r][c] > n:
                return False
            numSet.add(mat[r][c])

    # Check column
    for c in range(n):
        numSet = set()
        for r in range(n):
            if mat[r][c] in numSet or mat[r][c] < 1 or mat[r][c] > n:
                return False
            numSet.add(mat[r][c])

    return True


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        (
            [
                [2, 3, 1],
                [1, 2, 3],
                [3, 1, 2],
            ],
            True,
        ),
        # Example 2 from the book
        (
            [
                [4, 4, 4],
                [2, 1, 3],
                [3, 2, 1],
            ],
            False,
        ),
        # Example 3 from the book
        ([[1]], True),
        # Additional test cases
        ([], True),
        ([[]], False),
        ([[1], [2]], False),
    ]

    for i, (mat, expected) in enumerate(tests):
        result = solution(mat)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"solution({mat}) = {result}, expected: {expected}")
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
