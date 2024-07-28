'''
Problem:
Given an array of positive numbers and a positive number "S", 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to "S". 
Return 0, if no such subarray exists.

Ex 1.
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Ex 2.
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Ex3.
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

def smallest_subarray_with_given_sum(S, arr):
    min = len(arr)+1
    size = 0
    sum = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]
        size += 1
        while sum >= S: # has to keep shrinking!
            if min > size:
                min = size
            sum -= arr[windowStart]
            size -= 1
            windowStart += 1
    
    return min

def main():
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum(7, [3, 4, 1, 1, 6]))

main()