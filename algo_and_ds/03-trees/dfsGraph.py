'''
     5
    / \
   3   7
  /\    \
 2  4 -> 8

DFS of this graph is 5,3,2,4,8,7
[link](https://favtutor.com/blogs/depth-first-search-python)
'''

graph = {
            '5' : ['3', '7'],
            '3' : ['2', '4'],
            '7' : ['8'],
            '2' : [],
            '4' : ['8'],
            '8' : []
        }

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

print("Depth-first search of the graph is: ", dfs(visited, graph, '5'))
