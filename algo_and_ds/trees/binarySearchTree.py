'''
Binary search tree has a sorted property.
    Sorted property: 
        1. Every single node on left should be smaller then root
        2. Every single node on right should be greater than root
        3. There is no duplicates

        2
       / \ 
      1   3
           \  
            4
It searches any value at O(logn) time.

*********************************************************************
Balanced binary search tree: For every single subtree, the heights of left and right subtrees differ by 1 at max.
    Suppose, in the above BST, 
        1. Height of left and right subtree of root 2 has 1 on left and 2 on right. So, they differ by 1.
        2. Height of left and right subtree of root 1 has no left and right child. So, they differ by 0.
        3. Height of left of right subtree of root 3 has 1 left child and no right child. So, they differ by 1

So, this is a balanced binary tree and searching any node there will take O(logn) times.

Question: We can use binary search in a sorted array with time complexity O(logn) then why do we need this complex data structure?
Ans: Because insertion and deletion of a sorted array will take O(n) because we need to push/pull every single value in worst case. 
But in a balanced binary search tree, we can get the insertion and deletion done by O(logn) time.

'''

def search(root, val):
    if not root:
        return False 
    if val < root.val:
        return search(root.left, val)
    elif val > root.val:
        return search(root.right, val)
    else:
        return True

