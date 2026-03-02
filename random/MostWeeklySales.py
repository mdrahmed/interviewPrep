'''
BookChapter 38: Sliding Windows: Most Weekly Sales

Question:
# Most Weekly Sales

Given an array, `sales`, find the most sales in any 7-day period.

Example 1: sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]
Output: 44
The 7-day period with the most sales is [5, 0, 1, 0, 15, 12, 11].

Example 2: sales = [0, 3, 7, 12]
Output: 0
There is no 7-day period.

Example 3: sales = [1, 2, 3, 4, 5, 6, 7]
Output: 28
The only 7-day period is the entire array.

Constraints:

- The length of `sales` is at most `10^6`
- Each element in `sales` is a non-negative integer less than `10^3`

'''

# Process: Keep a sliding window of size 7, max total will give us the most sales.
# TO: O(n), SO: O(1)

## Test & edge cases
# 1. [] empty array
# 2. [1,2,3] array less than 7 values
# 3. Check if there is no numbers
# 4. [0,0,0,0,0,0,0,0] array consists of only zeros

def most_weekly_sales(sales):
  if (len(sales) < 7):
    return 0

  total = 0
  for i in range(7):
    total += sales[i]
  
  maxSales = total
  for i in range(7, len(sales)):
    total += sales[i]
    total -= sales[i - 7]
    maxSales = max(total, maxSales)
  
  return maxSales



### Testing Phase ###
def run_tests():
  tests = [
      # Example 1 from the book
      ([0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1], 44),
      # Example 2 from the book
      ([0, 3, 7, 12], 0),
      # Edge case - empty array
      ([], 0),
      # Edge case - exactly 7 days
      ([1, 2, 3, 4, 5, 6, 7], 28),
      # Edge case - all zeros
      ([0, 0, 0, 0, 0, 0, 0, 0], 0),
  ]
  for sales, want in tests:
    got = most_weekly_sales(sales)
    print(f"most_weekly_sales({sales}): got: {got}, want: {want}")
    assert got == want, f"\nmost_weekly_sales({sales}): got: {
        got}, want: {want}\n"

run_tests()