

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

### Algo 2: Bellman-ford

### Algo 3: Dijkstra
