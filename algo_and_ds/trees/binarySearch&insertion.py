
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def search(root,val):
    if not root:
        return None
    if val < root.val:
        return search(root.left, val)
    if val > root.val:
        return search(root.right, val)
    else:
        return True

root = TreeNode(6)

insert(root,4)
insert(root,7)
print("Ans:", search(root,5))

'''
# In class search

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Insert a new node and return the root of the BST.
    def insert(self, val):
        if not self.val:
            return TreeNode(val)
        
        if val > self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.insert(val)
        elif val < self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.insert(val)
        return root

    def search(self, target):
        if not root:
            return False
        
        if target > self.val:
            if self.left is None:
                return None 
            return self.left.search(target)
        elif target < self.val:
            if self.right is None:
                return None 
            return self.right.search(target)
        else:
            return True


root = TreeNode(6)

root.insert(4)
root.insert(7)

print("Ans:", root.search(5))
'''
