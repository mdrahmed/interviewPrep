"""
# Adjacency List Validation

Given an adjacency list, `graph`, write a function that returns whether `graph` is a _valid_ undirected graph, meaning that:

1. Every node is between `0` and `V-1`.
2. There are no _self-loops_: edges connecting a node to itself.
3. There are no _parallel edges_: two edges connecting the same two nodes.
4. If `node1` appears in `graph[node2]`, then `node2` also appears in `graph[node1]`.

Example 1: graph = [[1], [0]]
Output: True. This is a simple valid graph with two nodes connected by an edge.

Example 2: graph = [[2], [0]]
Output: False. Node index 2 is invalid since there are only 2 nodes.

Example 3: graph = [[0], []]
Output: False. Self-loop in node 0.

Example 4: graph = [[1, 1], [0, 0]]
Output: False. Parallel edges between nodes 0 and 1.

Example 5: graph = [[1], []]
Output: False. Node 0 has node 1 as a neighbor but not vice versa.

Constraints:

- `graph.length ≤ 1000`
- `graph[i].length ≤ 1000`


## Problem Solving Approach:
We can iterate through the adjacency list and check for all the conditions mentioned in the problem statement.
We can use a set to check for parallel edges and a dictionary to count the edges for symmetry check.
"""

## Calculate time & space
"""
TO: What about the total work across the entire graph. If we sum up the lengths of all the adjacency lists — len(graph[0]) + len(graph[1]) + ... + len(graph[V-1]) — what does that total time complexity equal in terms of V and E?
SO: node_set = O(V), edges = O(E), so, O(V+E)
"""
## TO & SO: O(V+E)
from collections import defaultdict


def is_valid_undirected_graph(adj):
    V = len(adj)
    edges = defaultdict(int)
    for i, graph in enumerate(adj):
        node_set = set()
        for node in graph:
            # valid node range check
            if node < 0 or node >= V:
                return False
            # self-loop check
            if i == node:
                return False
            # Check if parallel edges exist
            if node in node_set:
                return False
            else:
                node_set.add(node)

            # symmetry check
            edges[(min(i, node), max(i, node))] += 1

    for (i, node), val in edges.items():
        if val != 2:
            return False

    return True


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ([[1], [0]], True),
        # Example 2 from the book
        ([[2], [0]], False),
        # Example 3 from the book
        ([[0], []], False),
        # Example 4 from the book
        ([[1, 1], [0, 0]], False),
        # Example 5 from the book
        ([[1], []], False),
        # Additional test cases
        ([[1, 2], [0, 2], [0, 1]], True),  # Valid triangle graph
        ([[1], [0, 2], [1]], True),  # Valid line graph
        ([[], []], True),  # Valid graph with no edges
    ]

    for i, (graph, expected) in enumerate(tests):
        result = is_valid_undirected_graph(graph)
        print(
            f"Test {i + 1}: {result == expected} (Expected: {expected}, Got: {result})"
        )
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
