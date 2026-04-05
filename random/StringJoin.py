'''
BookChapter 26: String Manipulation: String Join

# String Join

Without using a built-in string join method, implement a `join(arr, s)` method, which receives an array of strings, `arr`, and a string, `s`, and returns a single string consisting of the strings in `arr` with `s` in between them.

Example 1: arr = ["join", "by", "space"], s = " "
Output: "join by space"

Example 2: arr = ["b", "", "k", "", "p", "r n", "", "d", "d!!"], s = "ee"
Output: "beeeekeeeepeer neeeedeed!!"

Example 3: arr = [], s = "x"
Output: ""

If strings in your language are immutable, assume that you have access to a function `array_to_string(arr)`, which takes an array of individual characters and returns a string with those characters in `O(len(arr))` time.

Constraints:

- 0 <= s.length <= 500
- 0 <= arr.length <= 10^5
- 0 <= arr[i].length <= 10^5
- the sum of the lengths of the strings in `arr` is at most 10^5

'''

## TO: O(n * m), SO: O(n) where n is the total length of the resulting string and m is the length of the string s.

def string_join(arr, s):
  res = []
  for i, ele in enumerate(arr):
    if i != 0:
      for c in s:
        res.append(c)
    for c in ele:
      res.append(c)
  return array_to_string(res)


def array_to_string(arr):
  return ''.join(arr)


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        (["join", "by", "space"], " ", "join by space"),
        # Example 2 from the book
        (["b", "", "k", "", "p", "r n", "", "d", "d!!"], "ee", "beeeekeeeepeer neeeedeed!!"),
        # Example 3 from the book
        ([], "x", ""),
        # Additional test cases
        (["a", "b", "c"], "-", "a-b-c"),
        (["hello", "world"], ", ", "hello, world"),
        (["foo"], "bar", "foo"),
        (["x", "", "y"], "*", "x**y"),
        (["", "", ""], "z", "zz"),
        (["single"], "", "single"),
        (["multiple", "strings", "test"], " | ", "multiple | strings | test")
    ]
    
    for i, (arr, s, expected) in enumerate(tests):
        result = string_join(arr, s)
        print(f"Test case {i+1}: arr={arr}, s='{s}', expected='{expected}', got='{result}'")
        assert result == expected, f"Test case {i+1} failed: expected '{expected}', got '{result}'"
    print("All test cases passed!")


if __name__ == "__main__":  run_tests()
