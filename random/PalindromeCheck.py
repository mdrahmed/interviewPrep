"""
Given a string `s`, return whether `s` is a _palindrome_. A palindrome is a string that reads the same forward and backward.

Example 1: s = "level"
Output: true

Example 2: s = "naan"
Output: true

Example 3: s = "hello"
Output: false

Constraints:

- The length of s is at most 10^6
- s consists of lowercase English letters

## Problem Solving Approach:
We can use two pointers, one starting from the beginning of the string and the other starting from the end of the string.
The left pointer is looping until the middle of the string and the right pointer is calculated based on the left pointer.
"""


# TO: O(n), SO: O(1)
def palindrome_check(s):
    n = len(s)
    for left in range(n // 2):
        right = n - left - 1
        if s[left] != s[right]:
            return False

    return True


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ("level", True),
        # Example 2 from the book
        ("naan", True),
        # Example 3 from the book
        ("hello", False),
        # Edge case: empty string
        ("", True),
        # Edge case: single character
        ("a", True),
        # Edge case: even length palindrome
        ("abba", True),
        # Edge case: odd length palindrome
        ("abcba", True),
        # Edge case: non-palindrome with similar characters
        ("abca", False),
    ]

    for i, (s, expected) in enumerate(tests):
        result = palindrome_check(s)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"palindrome_check('{s}') = {result}, expected: {expected}")
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
