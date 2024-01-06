def insertNodeAtPosition(llist, data, position):
    head = llist
    tmp = SinglyLinkedList()
    tmp.data = data
    i = 0 
    while llist:
        if position-1 == i:
            tmp.next = llist.next
            llist.next = tmp
        i += 1
        llist = llist.next
    return head
