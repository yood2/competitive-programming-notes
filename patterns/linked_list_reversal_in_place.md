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
