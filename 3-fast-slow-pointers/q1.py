'''
Problem:
Given the head of a singly linkedlist, write a function to determine if the list has a cycle in it or not.
'''

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
def has_cycle(head):
    fast = head
    slow = head

    while (slow and fast and slow.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has cycle: {str(has_cycle(head))}")

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {str(has_cycle(head))}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {str(has_cycle(head))}")

main()