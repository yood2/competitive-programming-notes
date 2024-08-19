'''
PROPERTIES
- Complete Binary Tree = all levels of tree are fully filled except the last level which is filled from LEFT TO RIGHT.
- Heap Property: min or max element is always at the root of the tree.
- Parent-Child Relationship: Parent at index 'i', left child at index '2i+1', right child at index '2i+2'.
- Efficient Insertion and Removal: Insertion and removal are efficient. New elements inserted at next available in bottom right, heap property 'heapifies up'.
- Efficient access to extreme elements: Min or max always at root with constant-time access.
'''
class MaxHeap:
    arr = []
    max_size = 0
    heap_size = 0

    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None] * max_size
        self.heap_size = 0
    
    '''
    HEAPIFY
    Process to rearrange elements to maintain property of heap.
    Start from root. Compare root to left and right children.
    If either child is larger, swap root with child.
    Recursively call for the index of the child you swapped with.
    $O(log n)$ to balance the tree.
    '''
    def MaxHeapify(self, i):
        l = (2 * i + 1)
        r = (2 * i + 2)
        largest = i
        if l < self.heap_size and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)
    '''
    INSERTION
    Insert new element into bottom rightmost spot (end of array).
    Perform heapify to fix heap property.
    Also $O(log n)$.
    '''
    def Insert(self, x):
        if self.heap_size == self.max_size:
            # Heap is full
            return
        
        self.heap_size += 1
        i = self.heap_size - 1
        self.arr[i] = x

        # while not at root and parent is less than curr val
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            # swap parent and curr val
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
    
    def parent(i):
        return (i-1) // 2
    '''
    DELETION
    Deleting root element is $O(1)$.
    Put rightmost leaf node at the root temporarily.
    Call heapify to fix heap property.
    Total time ios $O(log n)$.
    '''
    def RemoveMax(self):
        if self.heap_size <= 0:
            return None
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.MaxHeapify(0)

        return root
    '''
    GETMAX/GETMIN
    Just get the first element. $O(1)$ time.
    '''
    def GetMax(self):
        return self.arr[0]

    