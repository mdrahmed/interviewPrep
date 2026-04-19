"""
Given `n > 1`, find the number of different ways to cover a `1xn` floor with `1x1` and `1x2` tiles.

Example 1: n = 4
Output: 5

Example 2: n = 1
Output: 1

The following image shows the 5 different ways to cover a `1x4` floor with `1x1` and `1x2` tiles.

https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/recursion-fig9.png

Constraints:

- `1 ≤ n ≤ 45`
- Assume that the solution will fit in a signed `64`-bit integer.
"""


## Top-down approach - without cache, TO: O(2^n) & SO: O(1)
# For without cache:
# Making 2 recursive calls, so branching factor is 2 and depth could be upto n. So, TO: O(2^n) & SO: O(1). We could hit stack overflow with deep recursion at n = 10^6. So, I added memoization.
def ways_to_tile_1(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    return ways_to_tile_1(n - 1) + ways_to_tile_1(n - 2)


## Top-down approach - with cache, TO: O(n) and SO:O(n)
cache = {}


def ways_to_tile_2(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n in cache:
        return cache[n]
    cache[n] = ways_to_tile_2(n - 1) + ways_to_tile_2(n - 2)
    return cache[n]


## Bottom-up approach => with array, SO: O(n), TO: O(n)
def ways_to_tile_3(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


## Bottom-up approach => with constant space, TO: O(n), SO: O(1)
def ways_to_tile_4(n):
    dp = [0] * 2
    dp[0] = 1
    dp[1] = 2

    for i in range(3, n + 1):
        cur = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1] = cur

    return dp[1] if n >= 2 else dp[0]


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        (4, 5),
        # Example 2 from the book
        (1, 1),
        # Additional test cases
        (2, 2),
        (3, 3),
        (5, 8),
        (10, 89),
        (20, 10946),
        # (30, 832040),
    ]

    for i, (n, expected) in enumerate(tests):
        result = ways_to_tile_1(n)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("Top-down without cache test cases passed!")

    for i, (n, expected) in enumerate(tests):
        result = ways_to_tile_2(n)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("Top-down with cache test cases passed!")

    for i, (n, expected) in enumerate(tests):
        result = ways_to_tile_3(n)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("Bottom-up with array test cases passed!")

    for i, (n, expected) in enumerate(tests):
        result = ways_to_tile_4(n)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("Bottom-up with constant space test cases passed!")


if __name__ == "__main__":
    run_tests()
