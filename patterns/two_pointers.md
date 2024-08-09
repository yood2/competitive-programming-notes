# Two Pointers
**Summary:** Two pointers is typically used to search for a set of elements that fulfill certain constraints in a sorted array. We basically consider each element with the first pointer and iterate through the remaining elements with the other pointer.

**Key Characteristics**
- Linked list or array
- Sorted
- Complexity of $O(n)$ where $n$ is number of elements in the array.


#### General Format
```python
def two_pointer(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        curr = arr[start] + arr[end]
        if curr == target:
            return [start,end]
        elif curr > target:
            end -= 1
        else:
            end += 1
```