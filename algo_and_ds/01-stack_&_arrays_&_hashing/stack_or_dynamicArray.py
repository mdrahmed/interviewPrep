'''
Stack is LIFO - Last In First Out
All the operations of stack can be performed with the defaul array python.

3 major operations in stack,
    1. push => stack.append()
    2. pop => stack.pop() - this is will return the last item 
    3. peek/top => stack[0]

We can also do following operations in dynamic array or stack is following,
    1. arr.index(element, start, end) => check if element is present from this starting index to the ending index.
    2. arr.remove(element) => remove this element from the array
    3. arr.reverse() => reverse the list
    4. arr.sort() => sort the array
'''

darray = []
darray.append(1)
darray.append(2)
darray.append(3)
darray.append(4)
darray.append(5)
darray.append(6)

print("darray:",darray)
print("darray.pop(): ",darray.pop())
print("darray.index(element,start,end) => darray.index(4,0,4), index of element 4 from index 0 to 4 is: ", darray.index(4,0,4))

darray.remove(4)
print("darray.remove(4), after removing 4, new array is: ",darray)

darray.reverse()
print("darray.reverse(), after reversing the array, new array is: ", darray)

darray.sort()
print("darray.sort(), after sorting the array: ", darray)

