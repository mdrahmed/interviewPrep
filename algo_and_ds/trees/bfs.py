#     4
#    / \
#   3   6
#  /    /\
# 2    5  7
# bfs traverses level wise
# bfs = 4,3,6,2,5,7

# queue = [4]
# queue = [3,6] = 4
# queue = [6,2] = 4,3
# queue = [2,5,7] = 4,3,6
# queue = [5,7] = 4,3,6,2
# queue = [7] = 4,3,6,2,5
# queue = [] = 4,3,6,2,5

from collections import deque

def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level = 0
    while(len(queue) > 0):
        print("level:",level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

