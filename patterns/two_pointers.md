# Two Pointers
## Summary
Useful when we need to find a set of elements in a sorted array/list that fulfill a certain constraint. Set of elements could be a pair, triplet, or even subarray.
## Key Characteristics
- Linked list or array
- Sorted
- Complexity of $O(n)$ where $n$ is number of elements in the array.
## General Format
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
## Triplet Questions
Sometimes you will be asked to find triplets that meet a certain condition. You can use the principal of two pointer (using two pointers to iterate through different combinations of an array) while using an additional pointer to check the elements in between.
```python
def searchTriplets(self, arr):
    triplets = []
    arr = sorted(arr) # sort array if not yet sorted

    for i in range(len(arr) - 2): # i is like the starting point of our two pointer algorithm
        if i != 0 and arr[i] == arr[i-1]:
        continue
        
        left = i + 1
        right = len(arr) - 1

        while left < right: # this is basically just a normal two pointer algorithm
        curr = arr[i] + arr[left] + arr[right]
        if curr == 0:
            triplets.append([arr[i], arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left-1]: # make sure that left and right pointers are not pointing at duplicates
            left += 1
            while left < right and arr[right] == arr[right+1]:
            right -= 1

        elif curr > 0: # use sorted characteristic of array to make these decisions
            right -= 1
        else:
            left += 1

    return triplets
```