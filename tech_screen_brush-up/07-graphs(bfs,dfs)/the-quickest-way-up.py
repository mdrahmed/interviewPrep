# Link: https://www.hackerrank.com/challenges/the-quickest-way-up/problem
# Didn't work - Need to check the code

from collections import deque
def quickestWayUp(ladders, snakes):
    graph = {}
    for x,y in ladders+snakes:
        graph[x] = y
        
    q = deque([(1,0)])
    visited = [False] * 101
    
    while q:
        node,rolls = q.popleft()
        if node == 100:
            return rolls
        visited[node] = True
        for i in range(1,7):
            nextNode = node + i
            if nextNode <= 100 and visited[nextNode] == False:
                if nextNode in graph:
                    q.append((graph[nextNode], rolls+1))
                else:
                    q.append((nextNode, rolls + 1))
        return -1
