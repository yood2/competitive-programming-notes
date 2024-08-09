# Fast & Slow Pointers
**Summary:** Pointer algorithm that uses two pointers whicm move through the array (or linked list) at different speeds. Useful for cyclic Linked Lists or arrays.

**Key Characteristics**
- One pointer goes .next while second pointer goes .next.next
- If there is a cycle the fast pointer will catch up to the slow pointer
- Once slow pointer enters a cycle, fast pointer will meet the slow pointer in the same loop, thus making it $O(n)$ time.

#### General Format
```python
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def fast_slow(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True # found cycle
    return False
```