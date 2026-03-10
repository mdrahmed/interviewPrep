'''
A topological ordering is an ordering of nodes where for every directed edge `u -> v`, node `u` appears before node `v` in the ordering.

Using Kahn's algorithm, we can find a topological ordering of the nodes in a directed graph. The algorithm works as follows:
1. Compute the in-degree (number of incoming edges) for each node.
2. Initialize a queue with all nodes that have an in-degree of 0 (i.e., nodes with no dependencies).
3. While the queue is not empty:
   a. Remove a node from the queue and add it to the topological ordering.
   b. For each of its neighbors, decrease their in-degree by 1. If any neighbor's in-degree becomes 0, add it to the queue.
4. If the topological ordering contains all the nodes, return it. Otherwise, return an empty array (indicating a cycle in the graph).
'''

### Indegree Calculation
'''
## calculate in-degrees from list of edges
You are given a graph with n nodes, where each node has an integer value from 0 to n - 1.
The graph is represent by a list of edges, where edges[i] = [u, v] is a directed edge from node u to node v. Write a function to calculate the indegree of each node in the graph.
Example
Input:
edges = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]
'''

# If graph given as a list of edges, we can calculate in-degrees as follows:
def calculate_indegrees_from_edges(n, edges):
    indegrees = [0] * n
    for u, v in edges:
        indegrees[v] += 1
    
    return indegrees


'''
## Calculate in-degrees from adjacency list

You are given a graph with n nodes, where each node has an integer value from 0 to n - 1.
The graph is represent by an adjacency list, where each node i is mapped to a list of nodes that have a directed edge from node i to them. Write a function to calculate the indegree of each node in the graph.
Example
Input:
edges = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
n = 5

Output:
[0, 1, 2, 1, 1]
'''
# If graph given as an adjacency list, we can calculate in-degrees as follows:
def calculate_indegrees_from_adjacency_list(n, adj_list):
    indegrees = [0] * n
    
    for u in adj_list:
        for v in adj_list[u]:
            indegrees[v] += 1
    
    return indegrees

if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]
    print("In-degrees from edges:", calculate_indegrees_from_edges(5, edges))

    adj_list = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
    print("In-degrees from adjacency list:", calculate_indegrees_from_adjacency_list(5, adj_list))
