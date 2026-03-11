'''
# Topological Ordering
Given the adjacency list of a directed graph, `graph`, return a topological ordering of the nodes. If the graph contains a cycle, return an empty array.

A topological ordering is an ordering of nodes where for every directed edge `u -> v`, node `u` appears before node `v` in the ordering.

Example 1:
graph = [
  [1],        # Neighbors of node 0
  [],         # Neighbors of node 1
  [1],        # Neighbors of node 2
  [4],        # Neighbors of node 3
  [1, 2, 5],  # Neighbors of node 4
  [2]         # Neighbors of node 5
]

Output: [0, 3, 4, 5, 2, 1]
There can be multiple valid topological orderings.
[3, 4, 5, 2, 0, 1] is also a valid ordering.

Example 2:
graph = [
  [1],  # Neighbors of node 0
  [0],  # Neighbors of node 1
]

Output: []
There is a cycle.

Here is the graph from Example 1:

https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/topological-sort-8.png

Constraints:

- The number of nodes is at most `10^5`
- The number of edges is at most `10^6`
- Each node is labeled from `0` to `V-1`
'''

## Time & Space Complexity Analysis
'''
TO: O(n+m)
Why is it O(n+m), why not O(n x m)
Good question. Think about it this way: in the outer loop, you visit each of the n nodes once. Then for each node i, you look at its neighbors in adj[i]. How many neighbors does node 0 have? How many does node 1 have? If you add up all the neighbors across all nodes, what's the total?

SO: O(n+m)
nextAvailable => O(n)
pointedFrom => O(n + m)
topoOder => O(n)
So, total O(n+m)

Good analysis! Your pointedFrom structure stores at most m total elements across all sets (one entry per edge), and you have n keys, so O(n+m) is correct for that. The other structures are O(n). So overall O(n+m) space is right.
'''


import collections

## Needs revision, not sure if I am doing it right. Will try to implement it again after looking at the solution.
def topological_sort(adj_list):
  indegrees = [0] * len(adj_list)
  for neighbors in adj_list:
    for neighbor in adj_list[neighbors]:
      indegrees[neighbor] += 1
    
  queue = collections.deque()

  topoOrder = []
  for i in range(len(indegrees)):
    if indegrees[i] == 0:
      queue.append(i)
  
  while queue:
    node = queue.popleft()
    topoOrder.append(node)
    for neighbor in adj_list.get(node, []):
      indegrees[neighbor] -= 1
      if indegrees[neighbor] == 0:
        queue.append(neighbor)
  
  return topoOrder if len(topoOrder) == len(adj_list) else []


### Testing Phase ###
def run_tests():
  graph = {
    0: [1],
    1: [],
    2: [1],
    3: [4],
    4: [1, 2, 5],
    5: [2]
  }
  print(f'Graph: {graph}, Got: {topological_sort(graph)}, Expected: [0, 3, 4, 5, 2, 1]') # Expected: [0, 3, 4, 5, 2, 1]

  graph = {
    0: [1],
    1: [0]
  }
  print(f'Graph: {graph}, Got: {topological_sort(graph)}, Expected: []') # Expected: []
  
  # Additional test case: Linear graph 0 -> 1 -> 2
  graph = {
    0: [1],
    1: [2],
    2: []
  }
  print(f'Graph: {graph}, Got: {topological_sort(graph)}, Expected: [0, 1, 2]') # Expected: [0, 1, 2]
  
  # Additional test case: Single node
  graph = {
    0: []
  }
  print(f'Graph: {graph}, Got: {topological_sort(graph)}, Expected: [0]') # Expected: [0]


run_tests()