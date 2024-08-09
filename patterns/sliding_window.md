# Sliding Window
**Summary:** Sliding Window can be used for problems in which a fixed or variable size window is moved through a data structure (like an array or string). 

**Key Characteristics**
- Generally require finding subarray/substrings which satisfy some specific condition.
- Size of subarry or substring `k` will be given in some problems.
- Problems can easibly be solved in $O(n^2)$ time using nested loops but sliding window makes these into $O(n)$ time.

#### General Format
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