'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''
# Key to solving this is to first sort our array so we can use the two pointer pattern!
def search_triplets(arr):
    arr.sort()
    res = []
    
    for start in range(len(arr) - 2):
        if start > 0 and arr[start] == arr[start - 1]:
            continue

        curr = arr[start]
        left = start + 1
        right = len(arr) - 1

        while left < right:
            sum = curr + arr[left] + arr[right]
            if sum == 0:
                res.append([[curr],arr[left],arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif sum < 0:
                left += 1
            else:
                right -= 1
    
    return res
                

def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))

main()