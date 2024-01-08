from heapq import heappush, heappop
heap = []
check = set()
for i in range(int(input())):
    t = list(map(int, input().split()))
    
    if t[0] == 1:
        heappush(heap, t[1])
        check.add(t[1])  
    elif t[0] == 2:
        check.discard(t[1])
    else:
        while heap[0] not in check:
            heappop(heap)
        print(heap[0])
