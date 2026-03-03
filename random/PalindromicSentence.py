"""
BookChapter 27: Two Pointers: Palindromic Sentence

# Palindromic Sentence

Given a string `s`, return whether its letters form a palindrome ignoring punctuation, spaces, and casing.

Example 1:
Input: s = "Bob wondered, 'Now, Bob?'"
Output: true
Explanation: Considering only letters and ignoring case, we get "bobwonderednowbob" which is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: Considering only letters and ignoring case, we get "raceacar" which is not a palindrome.

Constraints:

- 0 ≤ s.length ≤ 10^6
- s consists of printable ASCII characters
"""

# TO: O(n), SO: O(1)

'''
Python functions that requires to remember:
ch.lower(), str.lower()
ch.isalpha(), str.isalpha()

Other functions:
str.isalnum(), ch.isalnum()
str.upper(), ch.upper()

To convert string into lowercase by removing punctuation, commas and spaces:
str = ""join(ch for ch in s if(ch.isalpha())

Actually, strings in Python are immutable. When you remove punctuation or convert to lowercase, you are creating new strings. So, Space complexity to remove or checking if its palindrome with s == s[::-1] is creating new string, so, SO = O(n)

In python,
    while not s[start].isalpha(): start += 1
    while not s[end].isalpha(): end -= 1
'''


def checkPalindrome(s):
  start, end = 0, len(s) - 1
  while (start <= end):
    while(start <= end and not s[start].isalpha()): start += 1
    while(start <= end and not s[end].isalpha()): end -= 1
    if (start <= end and s[start].lower() != s[end].lower()):
      return False
    start += 1
    end -= 1
  
  return True


### Testing Phase ###
def run_tests():
  tests = [
      # Example 1 from the book
      ("Bob wondered, 'Now, Bob?'", True),
      # Example 2 from the book
      ("race a car", False),
      # Edge case: empty string
      ("", True),
      # Edge case: string with only non-alphanumeric characters
      ("!!!", True),
      # Edge case: string with only spaces
      ("   ", True),
      # Edge case: string with only one character
      ("a", True),
      # Edge case: string with mixed case and punctuation that forms a palindrome
      ("A man, a plan, a canal: Panama", True),
      # Edge case: string with mixed case and punctuation that does not form a palindrome
      ("This is not a palindrome!", False),
  ]
  for s, expected in tests:
    result = checkPalindrome(s)
    print(f"checkPalindrome({s}) = {result}, expected: {expected}")
    assert result == expected, f"checkPalindrome({s}) = {result}, expected: {expected}" 

run_tests()