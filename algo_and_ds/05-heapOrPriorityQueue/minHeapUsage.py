'''
To understand heap, solve this problem with the heapify function of python,
QHEAP1: https://www.hackerrank.com/challenges/qheap1/problem
'''


'''
PRIORITY QUEUE/HEAP WILL PROVIDE DATA MIN VALUE IF ITS MIN HEAP, IT WILL PROVIDE MAX VALUE IF ITS MAX HEAP
In python, heapq.heapify(minHeap) will create min heap. There is no max heap in python but we can make values negative if we want max heap.

In min heap, the all roots will be smaller than its child
For this array,
=> [7,3,9] 
A min heap will give us the values in order -> 3, 7, 9

Most common functions,
    1. heapq.heapify(<array name>)
    2. heapq.heappush(<array name>, value)
    3. heapq.heappop(<array name>)
'''

import heapq
def minHeap(arr):
    heapq.heapify(arr)
    print(arr)


minHeap([7,3,9])
