
def maxDepth(self, root):
    if root is None:
        return 0
    
    l = self.maxDepth(root.left)
    r = self.maxDepth(root.right)

    return max(l,r)+1
