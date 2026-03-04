'''
BookChapter 29: Binary Search: Race Overtaking

# Race Overtaking

You are given two arrays of positive integers, `p1` and `p2`, representing players in a racing game. The two arrays are sorted, non-empty, and have the same length, `n`. The `i`-th element of each array corresponds to where that player was on the track at the `i`-th second of the race. We know that:

1. Player 1 started ahead (`p1[0] > p2[0]`)
2. Player 2 overtook player 1 _once_.
3. Player 2 remained ahead until the end (`p1[n - 1] < p2[n - 1]`).

Assume the arrays have no duplicates, and that `p1[i] != p2[i]` for any index.

Return the index at which player 2 overtook player 1.

Example 1: p1 = [2, 4, 6, 8, 10], p2 = [1, 3, 5, 9, 11]
Output: 3. At index 3, p2 (9) becomes greater than p1 (8).

Example 2: p1 = [2, 3, 4, 5, 6], p2 = [1, 2, 3, 6, 7]
Output: 3. At index 3, p2 (6) becomes greater than p1 (5).

Example 3: p1 = [3, 4, 5], p2 = [2, 5, 6]
Output: 1. At index 1, p2 (5) becomes greater than p1 (4).

Constraints:

- `2 ≤ p1.length = p2.length ≤ 10^6`
- `0 ≤ p1[i], p2[i] ≤ 10^9`
- `p1` and `p2` are strictly increasing
- There is exactly one point where `p2` overtakes `p1`

'''



# TO: O(logn), SO: O(1)

def binarySearch(p1, p2):
  l, r = 0, len(p2) - 1
  while (r - l > 1):
    mid = l + (r - l) // 2
    if p2[mid] < p1[mid]:
      l = mid
    elif p2[mid] > p1[mid]: # or, we can use else because =>  Assume the arrays have no duplicates, and that `p1[i] != p2[i]` for any index.
      r = mid
  
  return r

'''
## Example Trace
p1 = [2, 4, 6, 8, 10], p2 = [1, 3, 5, 9, 11]

l = 0, r = 5, mid = 2, p2[mid] = 5 < p1[mid] = 6, so, l = mid = 2
l = 2, r = 5, mid = 3, p2[mid] = 9 > p1[mid] = 8, so, r = mid = 3
l = 2 & r = 3 => l + 1 == r or r-l == 1, so, we stop loop
now return r = 3
'''

### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([2, 4, 6, 8, 10], [1, 3, 5, 9, 11], 3),
        # Example 2 from the book
        ([2, 3, 4, 5, 6], [1, 2, 3, 6, 7], 3),
        # Example 3 from the book
        ([3, 4, 5], [2, 5, 6], 1),
        # Edge case: minimum length arrays
        ([1, 2], [0, 3], 1),
        # Edge case: large values
        ([10**9 - i for i in range(10)], [10**9 - i - 1 for i in range(10)], list(range(10)).index(9)),
        # Edge case: overtaking at the last index
        ([1, 2, 3], [0, 1, 4], 2)
    ]
    for i, (p1, p2, expected) in enumerate(tests):
        result = binarySearch(p1, p2)
        print(f"Test {i + 1}: {result == expected} (Expected: {expected}, Got: {result})")
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
