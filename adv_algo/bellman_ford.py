'''
Given an weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], where edges[i] = [u, v, w] represents a direct edge from node u to v having w edge weight. You are also given a source vertex src.

Your task is to compute the shortest distances from the source to all other vertices. If a vertex is unreachable from the source, its distance should be marked as 108. Additionally, if the graph contains a negative weight cycle, return [-1] to indicate that shortest paths cannot be reliably computed.

Examples:

Input: V = 5, edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0

Output: [0, 5, 6, 6, 7]
Explanation: Shortest Paths:
For 0 to 1 minimum distance will be 5. By following path 0 → 1
For 0 to 2 minimum distance will be 6. By following path 0 → 1  → 2
For 0 to 3 minimum distance will be 6. By following path 0 → 1  → 2 → 4 → 3 
For 0 to 4 minimum distance will be 7. By following path 0 → 1  → 2 → 4
Input: V = 4, edges[][] = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], src = 0

Output: [-1]
Explanation: The graph contains a negative weight cycle formed by the path 1 → 2 → 3 → 1, where the total weight of the cycle is negative.
'''

## TO: O(V * E) for Bellman-Ford algorithm, SO: O(V) for distance array.

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [int(1e8)] * V
        dist[src] = 0
        
        # Relaxation step (V-1) times
        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != int(1e8) and dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    
        # If there is shorter path for dist[v] after V-1 iterations, that means there is a negative weight cycle.
        for u,v,wt in edges:
            if dist[u] != int(1e8) and dist[v] > dist[u] + wt:
                return [-1]
        
        return dist
    

### Testing Phase ###
def run_tests():
    sol = Solution()
    # Test case 1: Basic test case with positive weights
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    src = 0
    print(f'V:{V}, edges:{edges}, src:{src}, Got: {sol.bellmanFord(V, edges, src)}, Expected: [0, 5, 6, 6, 7]') # Expected: [0, 5, 6, 6, 7]

    # Test case 2: Graph with a negative weight cycle
    V = 4
    edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
    src = 0
    print(f'V:{V}, edges:{edges}, src:{src}, Got: {sol.bellmanFord(V, edges, src)}, Expected: [-1]') # Expected: [-1]

    # Test case 3: Graph with unreachable vertices
    V = 4
    edges = [[0, 1, 2], [1, 2, 3]]
    src = 0
    print(f'V:{V}, edges:{edges}, src:{src}, Got: {sol.bellmanFord(V, edges, src)}, Expected: [0, 2, 5, int(1e8)]') # Expected: [0, 2, 5, int(1e8)]

    # Test case 4: Graph with all vertices reachable and no negative weights
    V = 3
    edges = [[0, 1, 1], [1, 2, 2], [0, 2, 4]]
    src = 0
    print(f'V:{V}, edges:{edges}, src:{src}, Got: {sol.bellmanFord(V, edges, src)}, Expected: [0, 1, 3]') # Expected: [0, 1, 3]

    # Test case 5: Graph with a single vertex
    V = 1
    edges = []
    src = 0
    print(f'V:{V}, edges:{edges}, src:{src}, Got: {sol.bellmanFord(V, edges, src)}, Expected: [0]') # Expected:


if __name__ == "__main__":    run_tests()