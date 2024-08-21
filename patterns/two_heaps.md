# Two Heaps
## Summary
In problems where we are given a set of elements that we can divide into two parts. To solve, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern uses two Heaps to solve these problems: a min heap to find smallest element and a max heap to find biggest element.
## Finding Median
```python
from heapq import *

max_heap, min_heap = [], []

'''
1. If number is less than biggest in max_heap, insert into max_heap (smaller half of numbers)
2. If max_heap is greater than len(min_heap) + 1, imbalanced - pop from max_heap and put into min_heap
'''
def insertNum(num):
    if not max_heap or -max_heap[0] >= num:
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heappush(max_heap, -heappop(min_heap))

'''
1. If max_heap and min_heap equal, even number of elements. Therefore, return average (no median).
2. If not equal, return max_heap root (should be the larger heap).
'''
def findMedian:
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) / 2.0
    return -max_heap[0] / 1.0
```
