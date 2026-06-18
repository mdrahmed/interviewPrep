'''
# Most Shared Account

You've compiled a list of IP addresses of all the clients connected to your service and the username associated with each one. Assume all IPs are unique and username lengths are between `1` and `30`. We say a username is being shared if it appears in two (or more) connections. Return the most shared username. In case of a tie, return any of them.

Example 1: connections = [("203.0.113.10", "mike"), ("208.51.100.25", "bob"), ("202.0.2.5", "mike"), ("203.0.113.15", "bob2")]
Output: "mike". User "mike" is connected twice, while other users are connected once.

Example 2: connections = [("1.1.1.1", "alice"), ("1.1.1.2", "bob"), ("1.1.1.3", "alice"), ("1.1.1.4", "bob")]
Output: "alice". Both "alice" and "bob" are connected twice, so either would be a valid output.

Example 3: connections = []
Output: None. There are no connections.

Constraints:

- The length of connections is at most `10^5`
- All IPs are unique
- Username lengths are between `1` and `30` characters
- All usernames contain only lowercase letters

'''



# TC: O(n) for traversing the ips and O(n) at worst case while traversing the hashmap
# SC: O(n) for the hashmap

import collections
def solution(ips):
  hm = collections.defaultdict(int)
  for ip, user in ips:
    hm[user] += 1
  
  max_appeared = 0
  res = None
  for user, appearance in hm.items():
    if appearance > max_appeared:
      max_appeared = appearance
      res = user 
  
  return res


### Testing Phase ###
def run_tests():
  tests = [
    # Example 1 from the book
    ([("203.0.113.10", "mike"), ("208.51.100.25", "bob"), ("202.0.2.5", "mike"), ("203.0.113.15", "bob2")], "mike"),
    # Example 2 from the book
    ([("1.1.1.1", "alice"), ("1.1.1.2", "bob"), ("1.1.1.3", "alice"), ("1.1.1.4", "bob")], "alice"),
    # Example 3 from the book
    ([], None),
  ]

  for i, (ips, expected) in enumerate(tests):
    result = solution(ips)
    assert (
      result == expected
    ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print(f"Test {i+1}: {result} (Expected: {expected}, Got: {result})")

    


if __name__ == "__main__":
    run_tests()
