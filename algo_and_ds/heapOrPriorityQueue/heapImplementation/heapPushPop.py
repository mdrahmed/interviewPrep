'''
A heap should maintain 2 properties
1. Structure property: Insertion should be made from left to right
2. Order property: For a min heap, the root should be smaller than its child
    left child = 2*i
    right child = 2*i+1
    parent = i/2
'''

# Min Heap
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        # append value to the left
        self.heap.append(val)
        i = len(self.heap) - 1
        
        # now, check if this value is smaller then its root
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i//2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        # move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # go down because the minimum value is present at root so, ensure new root value is smaller than its child
        
        while 2 * i < len(self.heap):
            if(2 * i + 1 < len(self.heap)) 
                and self.heap[2 * i + 1] < self.heap[2 * i] 
                and self.heap[i] > self.heap[2 * i + 1]:
                
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i +1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break 
        return res





