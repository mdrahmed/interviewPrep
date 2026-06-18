'''

# Word Expansion Class

Implement a class, `Checker`, that receives a string `s` upon initialization. The class must support a method, `expands_into(s2)`, which takes another string and checks if `s2` can be formed by adding exactly one letter to `s1` and reordering the letters. All letters in both strings are lowercase alphabetical characters.

Example 1:
checker = Checker("tea")
print(checker.expands_into("tea"))   # returns False
print(checker.expands_into("team"))  # returns True
print(checker.expands_into("seam"))  # returns False

Example 2:
checker = Checker("on")
print(checker.expands_into("nooo"))  # returns False
print(checker.expands_into("not"))   # returns True
print(checker.expands_into("now"))   # returns True

Example 3:
checker = Checker("")
print(checker.expands_into("a"))     # returns True
print(checker.expands_into(""))      # returns False
print(checker.expands_into("ab"))    # returns False

Constraints:

- The length of `s` and `s2` is at most `10^5`
- All characters are lowercase English letters

Cases: s = “aab”, s2 = “aabb” => s could contain duplicates as well.
'''


# TC: O(len(s2)) + O(len(s1)) + O(26) => O(len(s2)) => O(n)
# SC: O(26) = O(1)

import collections
class Checker:
  def __init__(self, s1):
    self.s1 = s1
    # self.cnt = collections.Counter(s1)
    self.cnt = {}
    for ch in self.s1:
      self.cnt[ch] = 1 + self.cnt.get(ch, 0)

  def expands_into(self, s2):
    if len(s2) > len(self.s1) + 1 or len(s2) <= len(self.s1):
      return False 

    self.freq = [0] * 26
    for ch in s2:
      self.freq[ord(ch) - ord('a')] += 1
    
    for ch, count in self.cnt.items():
      self.freq[ord(ch) - ord('a')] -= count
    
	
    # return self.freq.count(1) == 1 and self.freq.count(0) == 25
    total = 0
    for i in range(26):
      if not 0 <= self.freq[i] <= 1:
        return False 
      total += self.freq[i]

    return True if total == 1 else False


### Testing Phase ###
def run_tests():
  tests = [
    # Example 1 from the book
    (Checker("tea"), "tea", False),
    (Checker("tea"), "team", True),
    (Checker("tea"), "seam", False),
    # Example 2 from the book
    (Checker("on"), "nooo", False),
    (Checker("on"), "not", True),
    (Checker("on"), "now", True),
    # Example 3 from the book
    (Checker(""), "a", True),
    (Checker(""), "", False),
    (Checker(""), "ab", False),
  ]

  for i, (checker, s2, expected) in enumerate(tests):
    result = checker.expands_into(s2)
    assert (
      result == expected
    ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print(f"Test {i+1}: {result} (Expected: {expected}, Got: {result})")



if __name__ == "__main__":
    run_tests()