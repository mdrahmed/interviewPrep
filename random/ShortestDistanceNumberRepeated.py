"""
# Shortest Distance Number Repeated

You are given an array of integers. Your task is to find the smallest distance between any two identical numbers in the array. If there are no repeated numbers, return `-1`.

The distance between two positions is calculated as the absolute difference between their indices.

Example 1:
Input: numbers = [1, 2, 3, 4, 2, 5, 3]
Output: 3
Explanation: The number 2 appears at index 1 and index 4, with a distance of 3. The number 3 appears at index 2 and index 6, with a distance of 4. The smallest distance is 3.

Example 2:
Input: numbers = [7, 8, 9]
Output: -1
Explanation: Since no number is repeated in the array, the output is -1.

Example 3:
Input: numbers = [1, 1, 2, 3]
Output: 1
Explanation: The number 1 appears at adjacent positions, giving a minimum distance of 1.

Example 4:
Input: numbers = [1, 1, 2, 1]
Output: 1
Explanation: The number 1 appears at positions 0, 1, and 3. The minimum distance is 1 (between positions 0 and 1).

Constraints:

- The length of numbers is at most `10^5`
- Each element in numbers is an integer between `-10^9` and `10^9`
"""

"""
### Problem Solving Approach
Sol 1: using a hashmap and storing the indices for each number. For same number the distance will be calculated and then minimum distance will be found.
  - the keys are the numbers from the array
  - the values are the indices.
  - To compute distance, if same number is found then abs(i - hm[num]) will provide the distance. Then minimum distance will be updated if smaller then min_dist
  - This hm[num] value will also be updated to current index

Edge cases:
- If the array is empty
- No identical numbers
"""

# TC: Traverses array once, so, O(n)
# SC: Hashmap stores all values in worst case, so, O(n)


def solution(nums):
    hm = {}
    min_dist = float("inf")
    for i, val in enumerate(nums):
        if val in hm:
            min_dist = min(i - hm[val], min_dist)
        hm[val] = i

    return min_dist if min_dist != float("inf") else -1


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([1, 2, 3, 4, 2, 5, 3], 3),
        # Example 2 from the book
        ([7, 8, 9], -1),
        # Example 3 from the book
        ([1, 1, 2, 3], 1),
        # Example 4 from the book
        ([1, 1, 2, 1], 1),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = solution(nums)
        print(f"Test {i+1}: {result} == {expected} -> {result == expected}")
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
