#     4
#    / \
#   3   6
#  /    /\
# 2    5  7
# dfs traverses in depth

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)
# left, root, right
# 2,3,4,5,6,7

def preorder(root):
    if not root:
        return None
    print(root.val)
    preorder(root.left)
    preorder(root.right)
# root, left, right
# 4,3,2,6,5,7

def postorder(root):
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val)
# left, right, root
# 2,3,5,7,6,4

def reverseorder(root):
    if not root:
        return None
    reverseorder(root.right)
    print(root.val)
    reverseorder(root.left)

# Time Complexity
# As we are traversing each node, its O(n)

# insertion into a binary tree is O(logn), for a balanced tree
# Building the entire tree is O(n)
# For sorting its O(nlogn)
