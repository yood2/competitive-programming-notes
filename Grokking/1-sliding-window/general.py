'''
General:
- Array or linked list
- When we need to find subarrays according to a given set of conditions
'''

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

def main():
    print(sliding_window(5, [1,2,3,4,5,6,7,8,9]))

main()