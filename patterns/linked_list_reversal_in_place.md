# linked List Reversal In Place
## Summary
Some problems ask to reverse the links between a set of nodes. Often, the constraint will be to do this in place (without using extra memory). This pattern accomplishes that.
## Key Characteristics
- Can reverse entire list or a portion of it if you speciy start and end positions.
- Time is $O(n)$ where $n$ is number of nodes in the list.
- Space is $O(1)$ as it is done in place.
## General Format
```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(arr):
    prev = None
    current = head

    while current is not None:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
```
## Reversing a Sublist
Lot harder than reversing the entire list. You need to find the start and end nodes of the sublist. Then reverse the sublist and connect the start and end nodes to the reversed sublist.
```python
def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    prev = None
    curr = head

    # Move to the start of the sublist
    for _ in range(left - 1):
        prev = curr
        curr = curr.next

    # Save the node before sublist and the start of sublist
    start_prev = prev
    start = curr

    # Reverse the sublist. We are using right - left to determine how many traversals we do.
    for _ in range(right - left + 1):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # Connect the reversed sublist back to the main list
    if start_prev:
        start_prev.next = prev
    else:
        head = prev
    start.next = curr

    return head
```
