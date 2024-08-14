# Stacks
## Summary
Stacks are linear data structures that follow particular order of operations (LIFO).

## Key Characteristics
- Main operations include Push, Pop, Peek, IsEmpty.
- All operations can be done with $O(1)$ time complexity.
- Can be implemented using arrays or linked lists.
- Might need to handle overflow and underflow (not enough space vs popping no elements)
- Useful for DFS algorithms since we "stack" the nodes to visit.
## Array Implementation
```python
class Stack:
    def __init__(self, size):
        # Initialize the stack with a specified size
        self.stack = [None] * size
        # Initialize the top pointer to -1, indicating an empty stack
        self.top = -1

    def push(self, data):
        # Check if the stack is full
        if self.top == len(self.stack) - 1:
            raise Exception('Stack is full')
        # Increment the top pointer
        self.top += 1
        # Add the data to the stack at the current top position
        self.stack[self.top] = data

    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # Retrieve the data from the top of the stack
        data = self.stack[self.top]
        # Remove the data from the stack by setting it to None
        self.stack[self.top] = None
        # Decrement the top pointer
        self.top -= 1
        # Return the popped data
        return data

    def peek(self):
        # Check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # Return the data at the top of the stack without removing it
        return self.stack[self.top]

    def isEmpty(self):
        # Check if the stack is empty by examining the top pointer
        return self.top == -1
```
## Linked List Implementation
```python
class Stack:
    class Node:
        def __init__(self, data):
            self.data = data  # Store the data in this node
            self.next = None  # Initialize the next node as None

    def __init__(self):
        self.top = None  # Initialize the top of the stack as None

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")  # Raise exception if the stack is empty
        item = self.top.data  # Store the top item's data
        self.top = self.top.next  # Update the top to be the next node
        return item  # Return the popped item

    def push(self, item):
        t = self.Node(item)  # Create a new node with the provided data
        t.next = self.top  # Set the next of this new node to be the current top
        self.top = t  # Update the top to be the new node

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")  # Raise exception if the stack is empty
        return self.top.data  # Return the top item's data

    def is_empty(self):
        return self.top is None  # Return True if the stack is empty, False otherwise
```
