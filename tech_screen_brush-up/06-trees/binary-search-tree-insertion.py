class Node:
    def insert(self, val):
        #Enter you code here.
        if self.root is None:
            self.root = Node(val)
            return 
        cur = self.root
        while cur:
            if val < cur.info:
                if cur.left is None:
                    cur.left = Node(val)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(val)
                    return
                cur = cur.right
 
