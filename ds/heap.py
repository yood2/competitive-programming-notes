'''
PROPERTIES
- Complete Binary Tree = all levels of tree are fully filled except the last level which is filled from LEFT TO RIGHT.
- Heap Property: min or max element is always at the root of the tree.
- Parent-Child Relationship: Parent at index 'i', left child at index '2i+1', right child at index '2i+2'.
- Efficient Insertion and Removal: Insertion and removal are efficient. New elements inserted at next available in bottom right, heap property 'heapifies up'.
- Efficient access to extreme elements: Min or max always at root with constant-time access.

HEAPIFY UP
Process to rearrange elements to maintain property of heap.
Start from element at index i. Compare to parent. If larger/smaller,
swap. Continue until at index 0 or until parent is no longer
larger/smaller.

INSERTION
Insert new element into bottom rightmost spot (end of array).
Perform heapify up to fix heap property.
Also $O(log n)$.

HEAPIFY DOWN
Process to rearrange elements to maintain property of heap.
Start from root. Compare root to left and right children.
If either child is larger, swap root with child.
Recursively call for the index of the child you swapped with.
$O(log n)$ to balance the tree.

POP
Deleting root element is $O(1)$.
Put rightmost leaf node at the root temporarily.
Call heapify down to fix heap property.
Total time ios $O(log n)$.

PEEK
Just get the first element. $O(1)$ time.
'''
class BinaryHeap:
    def __init__(self):
        self._heap = []

    def _heapify_up(self, i):
        while (i-1)//2 >= 0:
            parent = (i-1) // 2
            if self._heap[i] < self._heap[parent]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            i = parent

    def insert(self, item):
        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)

    def _heapify_down(self, i):
        while 2 * i + 1 < len(self._heap):
            smaller_child = self._get_min_child(i)
            if self._heap[i] > self._heap[smaller_child]:
                self._heap[i], self._heap[smaller_child] = (
                    self._heap[smaller_child],
                    self._heap[i],
                )
            else:
                break
            i = smaller_child
            
    def _get_min_child(self, i):
        # only left child exists
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        # left child smallest
        if self._heap[2 * i + 1] < self._heap[2 * i + 2]:
            return 2 * i + 1
        # right child smallest
        return 2 * i + 2

    def pop(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._heapify_down(0)
        return result

    def peek(self):
        return self._heap[0]
'''
HEAPQ
Collections module provides an implementation of the heap queue algorithm.
'''
from collections import heapq

heap = []
x = 1
heapq.heappush(heap, x)
heapq.heappop(heap)