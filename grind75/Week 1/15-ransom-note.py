'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
# Inutition: Make a hash, put all chars and occurences in hash, go through chars in ransomNote and see if it fits
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        for c in magazine:
            if c not in hash.keys():
                hash[c] = 0
            hash[c] += 1
        
        for c in ransomNote:
            if c not in hash.keys() or hash[c] == 0:
                return False
            hash[c] -= 1
        
        return True

# Solution: Similar to intuition, just more efficient. Use defaultdict to set default value
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = defaultdict(int)
        for c in magazine:
            hash[c] += 1
        
        for c in ransomNote:
            if hash[c] == 0:
                return False
            hash[c] -= 1
        
        return True