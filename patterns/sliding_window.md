# Sliding Window
## Summary
Useful for problems where we are asking to find or calculate something among all subarrays (or sublists) of a given size. Basic idea is that we can add one and remove one element at a time instead of recalculating a whole subarray (this is more efficient).
## Key Characteristics
- Generally require finding subarray/substrings which satisfy some specific condition.
- Size of subarry or substring `k` will be given in some problems.
- Problems can easibly be solved in $O(n^2)$ time using nested loops but sliding window makes these into $O(n)$ time.
## General Format
```python
def sliding_window(K, arr):
    res = []
    windowStart = 0
    windowSum = 0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            res.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1
    return res
```