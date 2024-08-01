'''
Problem:
Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.

Ex 1.
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Ex 2.
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''

def pair_with_target_sum(arr, target):
    start = 0
    end = len(arr) - 1

    while start != end:
        sum = arr[start] + arr[end]
        if sum == target:
            return [start, end]
        elif sum > target:
            end -= 1
        elif sum < target:
            start += 1

    return -1

def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))

main()