'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
def isValid(self, s: str) -> bool:
    closing = {')':'(', '}':'{', ']':'['}
    stack = []

    for c in s:
        if c not in closing.keys():
            stack.append(c)
        elif len(stack) == 0 or stack.pop(c) != closing[c]:
            return False
        
    if len(stack) == 0:
        return True