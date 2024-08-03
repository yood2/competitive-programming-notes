'''
Given a binary tree, determine if it is 
height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root) != -1
    def recursive(self, curr):
        # Base case: If the current node is None, return height 0
        if curr is None:
            return 0

        # Recursively check the height of the left subtree
        left_height = self.recursive(curr.left)

        # Recursively check the height of the right subtree
        right_height = self.recursive(curr.right)

        # Check if the current node is balanced
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1  # Current node is imbalanced

        # Return the height of the current node
        return max(left_height, right_height) + 1