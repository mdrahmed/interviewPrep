'''
Queue is First In First Out
=> [7, 3, 9] 
Now, if we pop the values then we will get this order => 7 then 3 then 9

PRIORITY QUEUE/HEAP WILL PROVIDE DATA MIN VALUE IF ITS MIN HEAP, IT WILL PROVIDE MAX VALUE IF ITS MAX HEAP
In python, heapq.heapify(minHeap) will create min heap. There is no max heap in python but we can make values negative if we want max heap.

For this array,
=> [7,3,9] 
A min heap will give us the values in order -> 3, 7, 9
'''


'''
problem: k-closest-points-to-origin
https://leetcode.com/problems/k-closest-points-to-origin/

*********************************************************
To use min heap, just do following on the array
heapq.heapify(<array name>)

To push into array do this,
heapq.heappush(<array name>, value)

To pop a value do this,
heapq.heappop(<array name>)
'''

minHeap = []
for x,y in points:
    dist = (x ** 2) + (y ** 2)
    minHeap.append( [dist, x, y] )
heapq.heapify(minHeap)
ans = []
while k > 0:
    dist, x, y = heappop(minHeap)
    ans.append([x,y])
    k -= 1
return ans


