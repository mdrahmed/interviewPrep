'''
PRIORITY QUEUE/HEAP WILL PROVIDE DATA MIN VALUE IF ITS MIN HEAP, IT WILL PROVIDE MAX VALUE IF ITS MAX HEAP
In python, heapq.heapify(minHeap) will create min heap. There is no max heap in python but we can make values negative if we want max heap.

For this array,
=> [7,3,9] 
A max heap will give us the values in order -> 9, 7, 3
'''
import heapq
def maxHeap(arr):
    for i in range(len(arr)):
        arr[i] = -1 * arr[i]
    heapq.heapify(arr)
    print("Array after max heap:", arr)
    print("Origial values: ")
    for i in arr:
        print(-1 * i)

maxHeap([7,3,9])
