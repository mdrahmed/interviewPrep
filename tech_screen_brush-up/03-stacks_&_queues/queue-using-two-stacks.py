'''
Link: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
While adding element to queue, add it to one stack.
While removing element from queue, add all elements of 1st stack to the 2nd stack. Then pop from 2nd stack.
'''

q = int(input())
stackEnqueue = []
stackDeque = []
for i in range(q):
    t = list(input().split())
    if t[0] == '1':
        stackEnqueue.append(t[1])
    elif t[0] == '2':
        if not stackDeque:
            while stackEnqueue:
                stackDeque.append(stackEnqueue.pop())
        stackDeque.pop()
    else:
        if not stackDeque:
            while stackEnqueue:
                stackDeque.append(stackEnqueue.pop())
        print(stackDeque[-1])   
        
#Time Complexity: O(n)
