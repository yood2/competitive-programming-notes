'''
For stacks in Python, just use a list and commit to only popping the end off.
This acts as LIFO.
'''
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# Removing elements from the stack
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
