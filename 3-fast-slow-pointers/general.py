'''
General:
- Arrays or linked lists
- Pointers move at different speeds
- Idea is that if there is a loop, the faster pointer will catch up to the slower one eventually
- Use when the problem will deal with a loop in a linked list or array
- Use when you need to know the position of a certain element or the overall length of the linked list.
'''
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
def fast_slow_pointers(head):
    fast = head
    slow = head

    while (slow and fast and slow.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False