'''
It can be difficult to implement again, need to go through the logic again. 
    1. Adjaceny part is the initialization part
    2. Check and understand the bfs part properly
link: https://www.hackerrank.com/challenges/bfsshortreach/problem
'''
from collections import deque
def bfs(n, m, edges, s):
    # Inititalization part
    # Need adjacency list for the graph
    graph = [[] for _ in range(n+1)]
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
    # To mark levels visited
    visited = [False] * (n+1)
    distances = [-1] * (n+1)
    # initializing the queue with starting point
    q = deque([(s,0)])
    distances[s] = 0
    visited[s] = True
    
    # bfs part
    while q:
        node, weight = q.popleft()
        for v in graph[node]:
            if visited[v] == False:
                distances[v] = weight+6
                visited[v] = True
                q.append((v, distances[v]))
    
    distances.remove(0)
    return distances[1:]
