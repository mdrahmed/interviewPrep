# The mistake usually people make here is they check the data, data can be same in 2 different nodes. 
# But it will form a cycle if a node is visited twice. So, check the memory location. 
# I used 2 pointers, one will move 2 steps and other 1 step at a time. So, if both of the location of the pointers are same then its a cycle.
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0

# Time complexity: O(n)
