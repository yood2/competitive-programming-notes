'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# Intuition 1: Strip, then 2 pointers
def isPalindrome(s: str):
    stripped = ""
    for c in s:
        if c.isalnum():
            stripped += c.lower()
    
    start = 0
    end = len(stripped) - 1
    while start < end:
        if stripped[start] != stripped[end]:
            return False
        start += 1
        end -= 1
    return True

# Solution: Just 2 pointers
def isPalindrome(s: str):
    start = 0
    end = len(s) - 1

    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[end].lower() == s[start].lower():
            start += 1
            end -= 1
        else:
            return False
    return True