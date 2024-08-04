'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API. 

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 231 - 1
'''
# Inutitive: I was thinking check if mid bad, then check if mid-1 is good, thus mid is first bad
# This is NOT a good approach since the first bad is either mid or before mid
# Easier to just keep binary searching until left == right
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # use binary search to get version in O(log n)
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if isBadVersion(mid-1) == False:
                    return mid
                right = mid + 1
            else:
                left = mid - 1

#Solution: O(log n) time
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # Check if this is the first bad version by looking at the previous one
                # but no need to explicitly check mid-1
                right = mid  # Move the right pointer to mid
            else:
                # If mid is not bad, then the first bad version is after mid
                left = mid + 1

        # At this point, left == right, pointing to the first bad version
        return left
