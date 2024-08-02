'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

# Intuition: Check length, convert s into hash with occurance values, remove by occurence in t, check if hash is empty
def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False

    hash = {}

    for c in s:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    
    for c in t:
        if c not in hash.keys():
            return False
        elif hash[c] < 1:
            return False
        hash[c] -= 1
        if hash[c] == 0:
            hash.pop(c)
    
    return len(hash) == 0

# Solution: Counter Hash Algo
def isAnagram(s: str, t: str):
    sHash = defaultdict(int)
    tHash = defaultdict(int)

    for c in s:
        sHash[c] += 1
    
    for c in t:
        tHash[c] += 1

    return sHash == tHash