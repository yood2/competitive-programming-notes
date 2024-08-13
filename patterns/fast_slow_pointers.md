# Fast & Slow Pointers
## Summary
Pointer algorithm that uses two pointers whicm move through the array (or linked list) at different speeds. Useful for cyclic Linked Lists or arrays.
## Key Characteristics
- One pointer goes .next while second pointer goes .next.next
- If there is a cycle the fast pointer will catch up to the slow pointer
- Once slow pointer enters a cycle, fast pointer will meet the slow pointer in the same loop, thus making it $O(n)$ time.
## General Format
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
## Other "Cyclic" Questions
You can use the idea of fast/slow iterators to solve other questions. For example, with the happy number question, you want to see if the number square summed every becomes 1 or if it is a eternal cycle.
```python
def isHappy(self, n: int) -> bool:
    if n == 1:
        return True

    def calculate(n):
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n = n // 10
        return total

    fast = n
    slow = n

    while True:
        fast = calculate(calculate(fast))
        slow = calculate(slow)
        if fast == 1:
            return True
        elif fast == slow:
            return False
```
## LinkedList questions where you need to find the middle
If a fast pointer at 2x speed of a slow pointer, we can assume the slow pointer will be at the middle when the fast pointer reaches the end. This is useful for some questions.
```python
def isPalindrome(self, head):
# find middle
fast, slow = head, head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

# reverse middle linkedlist?!?!?!
prev = None
while slow:
    next_node = slow.next
    slow.next = prev
    prev = slow
    slow = next_node

left, right = head, prev
while right:
    if left.val != right.val:
    return False
    left = left.next
    right = right.next

return True
```
