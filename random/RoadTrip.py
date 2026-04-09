"""
BookChapter 40: Dynamic Programming: Road Trip

# Road Trip

We are driving down a road with `n` rest stops between us and our destination. For each rest stop, our mapping software tells us how long of a detour it would be to stop there. We start before the first rest stop and our destination is past the last one.

We are given an array of `n` positive integers, `times`, indicating the delay incurred to stop at each rest stop. If we don't want to go more than 2 rest stops without taking a break, what's the least amount of time we have to spend on detours?

Example 1:
times = [8, 1, 2, 3, 9, 6, 2, 4]
Output: 6. The optimal rest stops are: [8, *1*, 2, *3*, 9, 6, *2*, 4]

Example 2:
times = [8, 1, 2, 3, 9, 3, 2, 4]
Output: 5. The optimal rest stops are: [8, 1, *2*, 3, 9, *3*, 2, 4]

Example 3:
times = [10, 10]
Output: 0. We don't need to make any stops.

Example 4:
times = [10]
Output: 0. We don't need to make any stops.

Example 5:
times = []
Output: 0. We don't need to make any stops.

Check out the figure below for an illustration of the first example:

https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/road-trip-1.png

Constraints:

- `n` is at least `0` and at most `10^6`.
- `times[i]` is at least `1` and at most `10^3`.
"""

### Top Down Approach ###
"""
The final answer is min(f(0), f(1), f(2)), and each f(i) recursively explores f(i+1), f(i+2), f(i+3). You don't need to start from a different index. Does that make sense?

how can we recursively explore this if n is >= 3, is it following,
f(i) = times[i] + min(f(i+1), f(i+2), f(i+3))

Now let's think about the base cases. We have f(i) going forward (increasing i), so what happens when i is near the end of the array? And what should the final answer be — is it just f(0)?
"""

# TO: O(3^n) without cache and O(n) with cache, SO: O(n) both with and without cache as system stack space is O(n) in the worst case for recursion


def top_down(times):
    n = len(times)
    if n < 3:
        return 0

    cache = {}

    def minimal_break(i):
        if i >= n:
            return 0
        if i in cache:
            return cache[i]
        cache[i] = times[i] + min(
            minimal_break(i + 1), minimal_break(i + 2), minimal_break(i + 3)
        )
        return cache[i]

    return min(minimal_break(0), minimal_break(1), minimal_break(2))


### Bottom Up Approach ###
"""
At each call to minimal_break(i), you're making 3 recursive calls. Each of those makes 3 more, and so on. So the branching factor is 3 and the depth can be up to n. Whats the time complexity of that?
TO: O(3^n) without cache and O(n) with cache

We could hit a stack overflow with deep recursion at n = 10^6. One way to avoid that is to convert this to a bottom-up (tabulation) approach instead of top-down recursion.

The previous solution is top-down — you start from the beginning and recurse forward toward the end. Top-down means you start from the original problem and break it down into subproblems via recursion.
Bottom-up (tabulation) would mean you start from the end of the array and work backwards, filling in a table iteratively with no recursion at all. Since f(i) depends on f(i+1), f(i+2), and f(i+3), if we start from the end, those values will already be computed when we need them.
"""
# TO & SO: O(n) with dp array


def bottom_up(n, times):
    if n < 3:
        return 0

    dp = [0] * n
    dp[n - 1] = times[n - 1]
    dp[n - 2] = times[n - 2]
    dp[n - 3] = times[n - 3]

    for i in range(n - 4, -1, -1):
        dp[i] = times[i] + min(dp[i + 1], dp[i + 2], dp[i + 3])

    return min(dp[0], dp[1], dp[2])


"""
### Space Optimized Bottom Up Approach ###
TO: O(n) with dp array and O(1) without dp array, SO: O(n) with dp array and O(1) without dp array

Since f(i) only depends on the next 3 values, we don't need to keep the entire dp array in memory. We can just keep track of the last 3 computed values and update them as we iterate backwards through the array. This way, we can achieve O(1) space complexity.
"""
# TO: O(n), SO: O(1)


def space_optimized_bottom_up(n, times):
    if n < 3:
        return 0

    dp = [0] * 3
    dp[2] = times[n - 1]
    dp[1] = times[n - 2]
    dp[0] = times[n - 3]

    for i in range(n - 4, -1, -1):
        current = times[i] + min(dp[0], dp[1], dp[2])
        dp[2] = dp[1]
        dp[1] = dp[0]
        dp[0] = current

    return min(dp)


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([8, 1, 2, 3, 9, 6, 2, 4], 6),
        # Example 2 from the book
        ([8, 1, 2, 3, 9, 3, 2, 4], 5),
        # Example 3 from the book
        ([10, 10], 0),
        # Example 4 from the book
        ([10], 0),
        # Example 5 from the book
        ([], 0),
        # Additional test cases
        ([1, 1, 1], 1),
        ([1, 2, 3], 1),
        ([3, 2, 1], 1),
        ([5, 5, 5], 5),
    ]

    # top down approach
    for i, (times, expected) in enumerate(tests):
        result = top_down(times)
        print(
            f"Test {i+1}: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}"
        )
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All top down tests passed!\n")

    # bottom up approach
    for i, (times, expected) in enumerate(tests):
        result = bottom_up(len(times), times)
        print(
            f"Test {i+1}: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}"
        )
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All bottom up tests passed!\n")

    # space optimized bottom up approach
    for i, (times, expected) in enumerate(tests):
        result = space_optimized_bottom_up(len(times), times)
        print(
            f"Test {i+1}: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}"
        )
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All space optimized bottom up tests passed!")


if __name__ == "__main__":
    run_tests()
