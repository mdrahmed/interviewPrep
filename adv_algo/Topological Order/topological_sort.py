
import collections

# Topological sort using list of edges
def topological_order_edges(n, edges):
    topoOrder = []
    indegrees = [0] * n
    for u, v in edges:
        indegrees[v] += 1
    
    queue = collections.deque()
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)
    # Alternative way to add nodes with indegree 0 to the queue
    # queue.extend(i for i in range(len(indegrees)) if indegrees[i] == 0)
    
    while queue:
        node = queue.popleft()
        topoOrder.append(node)
        for u, v in edges:
            if u == node:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
    
    return topoOrder if len(topoOrder) == n else []


# Topological sort using adjacency list
def topological_order_adj_list(n, graph):
    topoOrder = []
    indegrees = [0] * n
    for u in graph:
        for v in graph[u]:
            indegrees[v] += 1
    
    queue = collections.deque()
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)
    # queue.extend(i for i in range(len(indegrees)) if indegrees[i] == 0)
    
    while queue:
        node = queue.popleft()
        topoOrder.append(node)
        for u in graph:
            for v in graph[u]:
                if u == node:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        queue.append(v)
    
    return topoOrder if len(topoOrder) == n else []

### Testing Phase ###
def run_tests_list_of_edges():
    # Test case 1: Valid topological order
    edges = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]
    print(f'Edges:{edges}, Got: {topological_order_edges(5, edges)}, Expected: [0, 1, 3, 4, 2]') # Expected: [0, 1, 3, 4, 2]

    # Test case 2: Cycle detection
    edges = [(0, 1), (1, 0)]
    print(f'Edges:{edges}, Got: {topological_order_edges(2, edges)}, Expected: []') # Expected: []
    # Test case 3: Linear chain
    edges = [(0, 1), (1, 2), (2, 3)]
    print(f'Edges:{edges}, Got: {topological_order_edges(4, edges)}, Expected: [0, 1, 2, 3]') # Expected: [0, 1, 2, 3]

    # Test case 4: Multiple starting points
    edges = [(0, 2), (1, 2), (2, 3)]
    print(f'Edges:{edges}, Got: {topological_order_edges(4, edges)}, Expected: [0, 1, 2, 3] or [1, 0, 2, 3]') # Expected: [0, 1, 2, 3] or [1, 0, 2, 3]

    # Test case 5: No edges (all nodes independent)
    edges = []
    print(f'Edges:{edges}, Got: {topological_order_edges(3, edges)}, Expected: [0, 1, 2] or any permutation') # Expected: [0, 1, 2] or any permutation

    # Test case 6: Another cycle
    edges = [(0, 1), (1, 2), (2, 0)]
    print(f'Edges:{edges}, Got: {topological_order_edges(3, edges)}, Expected: []') # Expected: []


def run_tests_adj_list():
    # Test case 1: Valid topological order
    graph = {
        0: [1],
        1: [2, 3],
        2: [],
        3: [2, 4],
        4: []
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(5, graph)}, Expected: [0, 1, 3, 4, 2]') # Expected: [0, 1, 3, 4, 2]

    # Test case 2: Cycle detection
    graph = {
        0: [1],
        1: [0]
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(2, graph)}, Expected: []') # Expected: []
    # Test case 3: Linear chain
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(4, graph)}, Expected: [0, 1, 2, 3]') # Expected: [0, 1, 2, 3]

    # Test case 4: Multiple starting points
    graph = {
        0: [2],
        1: [2],
        2: [3],
        3: []
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(4, graph)}, Expected: [0, 1, 2, 3] or [1, 0, 2, 3]') # Expected: [0, 1, 2, 3] or [1, 0, 2, 3]

    # Test case 5: No edges (all nodes independent)
    graph = {
        0: [],
        1: [],
        2: []
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(3, graph)}, Expected: [0, 1, 2] or any permutation') # Expected: [0, 1, 2] or any permutation

    # Test case 6: Another cycle
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    print(f'Graph:{graph}, Got: {topological_order_adj_list(3, graph)}, Expected: []') # Expected: []

if __name__ == "__main__":
    print("Topological order using list of edges")
    run_tests_list_of_edges()

    print("\nTopological order using adjacency list")
    run_tests_adj_list()
