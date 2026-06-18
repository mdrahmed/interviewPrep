'''
# Is Reachable

Given an edge list, `edges`, representing an undirected graph, `V`, the number of nodes, and two distinct nodes, `node1` and `node2`, return whether `node2` is reachable from `node1`.

An edge list is a list of pairs, `(u, v)`, representing an edge between nodes `u` and `v`. For an undirected graph, each edge appears once in the list.

Example 1:
edges = [(0, 1), (1, 2), (1, 4), (1, 5), (2, 4), (2, 5), (4, 5)]
V = 6
node1 = 0
node2 = 4

0 - 1
1 - 2 4 5
2 - 4 5
4 - 5

Output: true
There is a path from node 0 to node 4, for example [0, 1, 4].

Example 2:
edges = [(0, 1), (1, 2), (1, 4), (1, 5), (2, 4), (2, 5), (4, 5)]
V = 6
node1 = 0
node2 = 3

Output: false
There is no path from node 0 to node 3.

Example 3:
edges = [(0, 1), (1, 2)]
V = 3
node1 = 0
node2 = 2

Output: true
There is a path from node 0 to node 2, for example [0, 1, 2].

Here is a drawing of the graph from Example 1:

https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/graph-path-1.png

Constraints:

- The number of nodes `V` is at most `10^3`
- The number of edges is at most `10^5`
- All nodes are integers between `0` and `V-1` (inclusive)
- `0 ≤ node1, node2 < V`
- `node1 != node2`
- There are no self-loops or parallel edges

'''



# TC:
# creating adj list = O(E)
# traversing the queue = O(V) => O(V+E)
# SC: queue = O(V), set = O(V), adj list = O(E) => O(V+E)

import collections

def solution(edges, node1, node2):
  if len(edges) == 0:
    return False

  adj_list = collections.defaultdict(list)
  for u,v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

  queue = collections.deque()
  visited = set()

  queue.append(node1)
  visited.add(node1)

  while queue:
    node = queue.pop()
    for v in adj_list[node]:
      if v not in visited:
        queue.append(v)
        visited.add(v)
        if v == node2:
          return True

  return False


### Testing Phase ###
def run_tests():
  tests = [
    # Example 1 from the book
    ([(0, 1), (1, 2), (1, 4), (1, 5), (2, 4), (2, 5), (4, 5)], 0, 4, True),
    # Example 2 from the book
    ([(0, 1), (1, 2), (1, 4), (1, 5), (2, 4), (2, 5), (4, 5)], 0, 3, False),
    # Example 3 from the book
    ([(0, 1), (1, 2)], 0, 2, True),
    # Edge case: no edges
    ([], 0, 1, False),
    # Edge case: disconnected graph
    ([(0, 1), (2, 3)], 0, 3, False),
    # Edge case: direct connection
    ([(0, 1)], 0, 1, True),
    # Edge case: self-loop
    ([(0, 0)], 0, 0, False)
  ]

  for i, (edges, node1, node2, expected) in enumerate(tests):
    result = solution(edges, node1, node2)
    assert (
        result == expected
    ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print(f"Test {i+1}: {result} (Expected: {expected}, Got: {result})")


if __name__ == "__main__":
  run_tests()