
# BookChapter 27: Two Pointers: Dutch Flag Problem
# TO: O(n), SO: O(1)
# TO: O(3) + O(n) + O(3) => O(n), SO: O(3) => O(1)

import collections
def sort_colors(arr):
  # using a hashmap -- # SO: O(3) => O(1)
  count = collections.defaultdict(int)

  # TO: O(3) => O(1)
  for i, color in enumerate(arr):
    count[color] += 1
  
  # TO: O(3) + O(n) => O(n)
  def fill_array_in_place(color, ind):
    # TO: O(3) => O(1)
    for c, cnt in count.items():
      if(c == color):
        limit = ind + cnt
        # TO: O(n) in worst case when all elements are of the same color
        while(ind < limit and ind < len(arr)):
          arr[ind] = color
          ind += 1
    return ind
        
  ind = 0
  # TO: O(3) => O(1)
  for color in ["R","W","B"]:
    ind = fill_array_in_place(color, ind)


### Testing Phase ###
def run_tests():
  tests = [
      # Example from the book
      (list("RWBBWRW"), list("RRWWWBB")),
      # Additional test cases
      ([], []),
      (list("R"), list("R")),
      (list("W"), list("W")),
      (list("B"), list("B")),
      (list("RW"), list("RW")),
      (list("WR"), list("RW")),
      (list("RWB"), list("RWB")),
      (list("RRRWWBBB"), list("RRRWWBBB")),
      (list("BBBWWRRR"), list("RRRWWBBB")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since function modifies in place
    sort_colors(arr_copy)
    print(f"sort_colors({arr}): got: {arr_copy}, want: {want}")
    assert arr_copy == want, f"\nsort_colors({arr}): got: {
        arr_copy}, want: {want}\n"

run_tests()