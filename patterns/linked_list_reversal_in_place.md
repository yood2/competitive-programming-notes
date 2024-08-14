# linked List Reversal In Place
## Summary
Some problems ask to reverse the links between a set of nodes. Often, the constraint will be to do this in place (without using extra memory). This pattern accomplishes that.

The actual reversal is pretty easy but it gets difficult if they ask you to reverse a specific sublist (nodes from a-b, or every kth node). For these questions I recommend having a separate reverse helper function and only implement the logic where it creates these "sublists", reverses them, then reconnects them.
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
def reverse_sublist(head, p, q):
    # BASE CASE
    if p == q or head is None:
        return head

    # LOOP THROUGH P-1 TIMES, KEEPING TRACK OF CURR AND PREV
    current, previous = head, None
    i = 0
    while current and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # AFTER P-1 LOOPS, CURR IS START OF SUBLIST (WE WILL ITERATE TILL ITS THE END OF SUBLIST)
    # PREV IS LAST NODE OF THE LIST BEFORE THE SUBLIST
    last_node_of_first_part = previous
    last_node_of_sub_list = current

    # WE WILL REVERSE LINKEDLIST Q-P+1 TIMES
    tmp = None
    i = 0
    while current is not None and i < q - p + 1:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
        i += 1

    # CHECK IF THERE ARE ANY NODES BEFORE SUBLIST. CONNECT IF YES, ELSE SET TO HEAD
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous
    else:
        head = previous

    # CONNECT SUBLIST WITH THE REMAINDER OF THE LIST (WHERE WE LEFT OFF AT CURRENT)
    last_node_of_sub_list.next = current
    return head
```
## Reversing every K nodes
```python
def reverse(head, k):
    # BASE CASE
    if k <= 1 or head is None:
        return head

    # LOOP THROUGH, KEEP TRACK OF CURR AND PREV
    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        next = None

        # BASICALLY, WE REVERSE K NODES
        i = 0
        while current and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
        i += 1

        # CONNECT PREVIOUS NODES IF THEY EXIST, ELSE PREV IS HEAD
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # CONNECT REVERSED SUBLIST TO REST OF THE LIST (NODES AFTER)
        last_node_of_sub_list.next = current

        # END THE LOOP ONCE WE REACH NONE
        if current is None:
            break

        # IMPORTANT TO CONNECT FINAL SUBLIST TO REST OF LIST
        previous = last_node_of_sub_list

    return head
```
