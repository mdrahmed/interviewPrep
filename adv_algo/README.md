

### Algo 1: Topological Ordering
A topological ordering is an ordering of nodes where for every directed edge `u -> v`, node `u` appears before node `v` in the ordering. 

#### Usage of this algorithm
1. How system decides what to compile first
2. How schedular decides which task to run before others

**Two important things to note:**
1. The graph must be acyclic
2. There can be more than 1 valid orderings, depends of the data structure we use e.g., Queue or Stack

**Kann's Algorithm**
Using Kahn's algorithm, we can find a topological ordering of the nodes in a directed graph. The algorithm works as follows:
1. Compute the in-degree (number of incoming edges) for each node.
2. Initialize a queue with all nodes that have an in-degree of 0 (i.e., nodes with no dependencies).
3. While the queue is not empty:
   a. Remove a node from the queue and add it to the topological ordering.
   b. For each of its neighbors, decrease their in-degree by 1. If any neighbor's in-degree becomes 0, add it to the queue.
4. If the topological ordering contains all the nodes, return it. Otherwise, return an empty array (indicating a cycle in the graph).

**Calculate Indegrees from edges:**
```
# If graph given as a list of edges, we can calculate in-degrees as follows:
def calculate_indegrees_from_edges(n, edges):
    indegrees = [0] * n
    for u, v in edges:
        indegrees[v] += 1
    
    return indegrees
```

**Calculate Indegrees from adjacency list:**
```

# If graph given as an adjacency list, we can calculate in-degrees as follows:
def calculate_indegrees_from_adjacency_list(n, adj_list):
    indegrees = [0] * n
    
    for u in adj_list:
        for v in adj_list[u]:
            indegrees[v] += 1
    
    return indegrees
```

TO: `O(n+m)`, SO: `O(n+m)`

## Single source shortest path algorithms
### Algo 1: Bellman-ford
Bellman-Ford is a single source shortest path algorithm. It effectively works in the cases of negative edges and is able to detect negative cycles as well. It works on the principle of relaxation of the edges.
    - Relaxation means updating the shortest distance to a node if a shorter path is found through another node e.g., update `distance[v]` if `distance[v] > distance[u] + w`
    - This process is repeated (V-1) times.
        - A shortest path between two vertices can have at most (V - 1) edges, it's **not possible to find shortest path with more that (V-1) edges.**

#### Usage of this algorithm
Bellman ford is suitable,
- to find single source shortest path even when graph contains negative edges.
- designed for directed graph but can be used for undirected graphs.

If we need to find **single source shortest path**, we can either use **Dijkstra or, bellman ford**.
**Dijkstra** is not suitable when,
    - Graph contains negative edges as it doesn't revisit the nodes 
    - It can't detect cycles (neither general cycles nor negative cycles)

Again, **shortest path doesn't exist** when graph contains **negative weight cycle**,
    - The **negative weight cycle** is the total accumulated weight of edges is less than zero.

#### Limitations
Bellmand ford can detect negative weight cycle but **not general cycle.**

**Algorithm:**
1. Create a distance array with V values containing `int(1e8)`
2. Go through edges (V - 1) times
    1. Relax dist edges if dist[v] > dist[u] + wt
3. Now, go through only edges, if any edge relaxation is possible then there is a negative weight cycle.
```
TO: O(V * E) for Bellman-Ford algorithm, SO: O(V) for distance array.
```

### Algo 2: Dijkstra


## All-pairs shortest path algorithms
### Algo 1: Floyd Warshall
This algorithm
- Works on 2-dimensional array
- Finds shortest path from all pair of nodes
- Works on both directed and undirected graphs
- Can handle graph with both positive and negative edges
- Does not work on graphs with negative cycles (cycle in graph whose sum of edges is negative)
- Works better for dense graphs (no of edges are significantly higher than vertices), for sparse graph (less edges) Johnson'a algorithm is better
- TO: O(V^3) always, no matter how many edges are there

The algorithm relies on the principle that,
- If the shortest path from i to j passes through some vertex k, then the path from i to k and path from k to j must also be shortest path.

**Algorithm:**
- For every pair (i,j) of the source and destination vertices, there are 2 possible cases
    - k is not an intermediate vertex between i and j, `dist[i][k]` & `dist[k][j]` are INF
    - k is an intermediate vertex between i and j then we update `dist[i][j]` as `dist[i][k] + dist[j][k]`, if `dist[i][k] + dist[j][k] < dist[i][j]`

