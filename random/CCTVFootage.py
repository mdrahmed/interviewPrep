'''
# CCTV Footage

You are given an API called `is_stolen(t)` which takes a timestamp as input and returns `True` if the bike is missing at that timestamp and `False` if it is still there. You're also given two timestamps, `t1` and `t2`, representing when you parked the bike and when you found it missing. Return the timestamp when the bike was first missing, minimizing the number of API calls. Assume that `0 < t1 < t2`, `is_stolen(t1)` is `False`, and `is_stolen(t2)` is `True`.

https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/binary-search-fig2.png

Example 1: t1 = 1, t2 = 5, is_stolen = lambda t: t >= 3
Output: 3. The bike was stolen at timestamp 3.

Example 2: t1 = 1, t2 = 10, is_stolen = lambda t: t >= 7
Output: 7. The bike was stolen at timestamp 7.

Example 3: t1 = 5, t2 = 10, is_stolen = lambda t: t >= 8
Output: 8. The bike was stolen at timestamp 8.

Constraints:

- `0 < t1 < t2 ≤ 10^6`
- The API call `is_stolen(t)` takes `O(1)` time
'''

### TO : O(logn), SO: O(1)

def binarySearch(t1, t2, is_stolen):
  left, right = t1, t2
  while (right - left > 1):
    mid = left + (right - left) // 2
    if is_stolen(mid):
      right = mid
    else: 
      left = mid
  
  return right


### Testing Phase ###
def run_tests():
  tests = [
      # Example 1 from the book
      (1, 5, lambda t: t >= 3, 3),
      # Example 2 from the book
      (1, 10, lambda t: t >= 7, 7),
      # Example 3 from the book
      (5, 10, lambda t: t >= 8, 8),
      # Additional test cases
      (1, 100, lambda t: t >= 50, 50),
      (1, 1000, lambda t: t >= 999, 999),
      (1, 1000000, lambda t: t >= 500000, 500000),
      (1, 10, lambda t: t >= 2, 2),
      (1, 10, lambda t: t >= 9, 9),
      (1, 10, lambda t: t >= 5, 5),
      (1, 10, lambda t: t >= 6, 6),
      (1, 10, lambda t: t >= 4, 4),
      (1, 10, lambda t: t >= 3, 3),
      (1, 10, lambda t: t >= 7, 7),
      (1, 10, lambda t: t >= 8, 8)
  ]
  for i, (t1, t2, is_stolen, expected) in enumerate(tests):
    result = binarySearch(t1, t2, is_stolen)
    print(f"Case {i+1}: t1={t1}, t2={t2}, stolen_at>={expected}, expected={expected}, got={result}")
    assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
  print("All test cases passed!")   

if __name__ == "__main__":
  run_tests()