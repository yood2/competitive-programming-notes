'''
General:
- Arrays or linked lists
- Sorted
- Typically used to search for pairs that meet a condition 
'''

def two_pointer(arr, target):
    start = 0
    end = len(arr - 1)

    while start < end:
        sum = arr[start] + arr[end]
        if sum == target:
            return [start, end]
        if sum > target:
            end -= 1
        if sum < target:
            start += 1