"""
Given a matrix dist[][] of size n x n, where dist[i][j] represents the weight of the edge from node i to node j.

If there is no direct edge, dist[i][j] is set to INF (a large value i.e., 108).
The diagonal entries dist[i][i] are 0, since the distance from a node to itself is zero.
The graph may contain negative edge weights, but it does not contain any negative weight cycles.
Determine the shortest path distance between all pair of nodes in the graph.

Example:

Input: dist[][] = [[0, 4, INF, 5, INF],
                    [INF, 0, 1, INF, 6],
                    [2, INF, 0, 3, INF],
                    [INF, INF, 1, 0, 2],
                    [1, INF, INF, 4, 0]]
"""


## TO: O(V^3) for Floyd-Warshall algorithm, SO: O(1) for in-place updates.
class Solution:
    def floydWarshall(self, dist):
        n = len(dist)

        # Pick intermediate vertices one by one
        for k in range(n):
            # Pick all vertices as source one by one
            for i in range(n):
                # Pick all vertices as destination for the above picked source
                for j in range(n):
                    if dist[i][k] != int(1e8) and dist[k][j] != int(1e8):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist


### Testing Phase ###
def run_tests():
    sol = Solution()
    # Test case 1: Basic test case with positive weights
    dist = [
        [0, 4, int(1e8), 5, int(1e8)],
        [int(1e8), 0, 1, int(1e8), 6],
        [2, int(1e8), 0, 3, int(1e8)],
        [int(1e8), int(1e8), 1, 0, 2],
        [1, int(1e8), int(1e8), 4, 0],
    ]
    print(
        f"Input: {dist}, \nGot: {sol.floydWarshall(dist)}, \nExpected: [[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]"
    )  # Expected: [[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]


if __name__ == "__main__":
    run_tests()
