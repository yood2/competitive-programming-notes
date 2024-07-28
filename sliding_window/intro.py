'''
Given an array, find the average of all contiguous subarrays of size 'K' in it.
'''

def brute_force(K, arr):
    res = []
    for i in range(len(arr)-K+1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
        res.append(sum / K)
    return res

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
    print(brute_force(5, [1,2,3,4,5,6,7,8,9]))
    print(sliding_window(5, [1,2,3,4,5,6,7,8,9]))

main()