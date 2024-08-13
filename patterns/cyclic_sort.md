# Cyclic Sort
## Summary
Cyclic Sort is an in-place sorting algorithm for sorting a range of numbers given the range. Mainly used when dealing with arrays containing numbers from 1 to n (n is size of array) or a known range.

Basically, iterate through array, check if element in correct position, if not swap with element at correct position, continue until all elements are sorted.
## Key Characteristics
- Time complexity is O(n) since we are iterating through the array once.
- Space complexity is O(1) since we are not using any extra space.
- Useful in problems where you need to find mising numbers in array with known range.
- Useful for finding duplicate numbers in a known range.
- ONLY good at its specific usecase. General purpose sorting algorithms are better for other things.
## General Format
```python
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        # calculate the correct index element should be at
        correct_position = arr[i] - 1

        # if not at correct index, swap. Else, go to next elem.
        if arr[i] != arr[correct_position:
            arr[i], arr[correct_position] = arr[correction_position], arr[i]
        else:
            i += 1
    return arr
```
## Finding Missing Number
The idea is that we sort first, than we iterate through and check that every number is in the correct place.
```python
def missing_num(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        correct = nums[i]
        if correct < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return n
```
