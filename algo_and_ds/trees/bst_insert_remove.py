#     4
#    / \
#   3   [] 
# insert(root,6)

# BST doesn't contain duplicates. 
# So, search first then insert the node
# If its less than root then go left otherwise right

def insert(root, val):
    if not root:
        # if no root then create node with this val
        return TreeNode(val)
    
    if val > root.val:
        # if val greater than root then insert on right subtree
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root
# Time complexity = O(height) or, O(logn)


# We need minimum node on rightsubtree to remove a node
def minValueNode(root):
    curr = root
    # goto the the left leaf node
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None

    # if value to remove is greater than root go right
    if val > root.val:
        root.right = remove(root.right, val)
    # if value is less than root then go left
    elif val < root.val:
        root.left = remove(root.left, val)
    # otherwise, this is the root we need to remove
    else:
        # if no node on left than return right
        if not root.left:
            return root.right
        # if no node on right than return left
        if not root.right:
            return root.left
        # otherwise, get minimum on right and replace value and than remove that minimum
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root
# Time complexity = O(logn)




