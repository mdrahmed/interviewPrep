
from collections import deque
def height(root):
    queue = deque()
    if root:
        queue.append(root)
    h = 0
    while(len(queue) > 0):
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        h += 1
    return h-1
