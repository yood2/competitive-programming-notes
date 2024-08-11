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
## Sliding Window + Hash
We can use this technique with hash maps to solve problems where we need to find a subarray with a specific sum or count of elements.
```python
def sliding_window_hash(K, arr):
    res = []
    windowStart = 0
    windowSum = 0.0
    freq = {}

    for windowEnd in range(len(arr)):
        if arr[windowEnd] not in freq:
            freq[arr[windowEnd]] = 0
        freq[arr[windowEnd]] += 1
        windowSum += arr[windowEnd]

        if windowEnd >= K-1:
            res.append(windowSum/K)
            windowSum -= arr[windowStart]
            freq[arr[windowStart]] -= 1

            if freq[arr[windowStart]] == 0:
                del freq[arr[windowStart]]
            windowStart += 1

    return res
```
