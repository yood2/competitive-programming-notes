'''
Normal Queue using Lists:
Basically you add to back and pop from front.
'''
queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

'''
Dequeue (Double-ended):
Add through the front. We can "dequeue" from the front or back.
'''
dequeue = []

dequeue.insert(0, 'a')
dequeue.insert(0, 'b')
dequeue.insert(0, 'c')

print("\nInitial dequeue")
print(dequeue)

print("\nElements dequeued from front")
print(dequeue.pop(0))
print(dequeue.pop(0))

print("\nElements dequeued from back")
print(dequeue.pop())

print("\nDequeue after removing elements")
print(dequeue)
