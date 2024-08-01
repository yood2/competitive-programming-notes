'''
Problem:
Given an array of positive numbers and a positive number "k", find the maximum sum of any contiguous subarray of size "k".

Ex 1.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Ex 2.
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_subarray_of_size_k(K, arr):
    max, sum, windowStart = 0
    
    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]
        if windowEnd >= K-1:
            if sum > max:
                max = sum
            sum -= arr[windowStart]
            windowStart += 1

    return max


def main():
    print(max_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_subarray_of_size_k(2, [2, 3, 4, 1, 5]))

main()

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''