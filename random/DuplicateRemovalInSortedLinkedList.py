"""

Given the head of a singly linked list with **sorted** integer values, `head`, remove duplicates **in place**.

Example 1:
head = 1 -> 1 -> 1 -> 3 -> 5 -> 5 -> null
Output: 1 -> 3 -> 5 -> null

Example 2:
head = 1 -> 1 -> 1 -> 1 -> 1 -> null
Output: 1 -> null

Example 3:
head = null
Output: null

Constraints:

- You have to create the `Node` class with an integer `val` field and a `next` pointer.
- The list can contain up to `10^5` nodes.

### Problem Solving Approach:
Iterate list and for each node, check if the next node has the same value.
If same, keep moving the next pointer until a different value.
Then, skip all the duplicates by updating the current node's next pointer.

"""

# TO: O(n)
# SO: O(1)


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def remove_duplicates(head):
    cur = head
    while cur and cur.next:
        dup = cur
        while dup.next and dup.val == dup.next.val:
            dup = dup.next
        cur.next = dup.next
        cur = cur.next
    return head


### Testing Phase ###
def build_linked_list(values):
    """Helper function to build a linked list from a list of values"""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def run_tests():
    # Example 1 from the book
    head = build_linked_list([1, 1, 1, 3, 5, 5])

    result = remove_duplicates(head)
    expected_values = [1, 3, 5]
    got = []
    for expected in expected_values:
        assert result.val == expected, f"Expected {expected}, got {result.val}"
        got.append(result.val)
        result = result.next
    assert result is None, "Expected end of list, but got more nodes"
    print(f"Test case 1 passed: got {got}, expected {expected_values}")

    # Example 2 from the book
    head = build_linked_list([1, 1, 1, 1])

    result = remove_duplicates(head)
    got = []
    while result:
        got.append(result.val)
        result = result.next
    assert got == [1], f"Expected [1], got {got}"
    print(f"Test case 2 passed: got {got}, expected [1]")

    # Example 3 from the book
    head = None
    result = remove_duplicates(head)
    assert result is None, "Expected None for empty list"
    print("Test case 3 passed: got None, expected None")

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
