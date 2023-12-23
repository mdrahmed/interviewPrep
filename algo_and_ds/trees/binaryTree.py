'''
        2
       / \ 
      1   3
     /
    4

In a binary tree, 
    There will be at max 2 child - left, right
    There will be leaf nodes for sure - leaf nodes are those nodes that doesn't have any children
    There will be no cycle.
    All nodes are connected

Siblings - same parent
Height - Going down to the descendents
    height of 1 is 2
    height of 3 is 1
    height of 2 is 3
Depth - Going up to the ancestor
    depth of 2 is 1
    depth of 1 is 2
    depth of 4 is 3
'''

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.right = None
        self.left = None


