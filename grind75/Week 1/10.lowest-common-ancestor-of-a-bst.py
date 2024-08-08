'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recursive(root, p, q)

    def recursive(self, curr, p, q):
        # Base case: If the current node is None, return None
        if curr is None:
            return None
        
        # If we find either p or q, return the current node
        if curr == p or curr == q:
            return curr
        
        # Recursively search in the left and right subtrees
        left = self.recursive(curr.left, p, q)
        right = self.recursive(curr.right, p, q)

        # If both left and right are not None, the current node is the LCA
        if left is not None and right is not None:
            return curr
        
        # Otherwise, return the non-None child
        if left is not None:
            return left
        else:
            return right