# Depth First Search
## Summary
DFS is a technique to traverse a tree. Use recursion to keep track of all the previous nodes while traversing.
## Key Characteristics
- Since it uses recursion, space complexity will be $O(h)$ where $h$ is maximum height.
## General Format
```python
def dfs(root, sum):
    # base case
    if not root:
        return False

    # checking if we have a path FROM ROOT TO LEAF with sum
    if root.val == sum and not root.left and not root.right:
        return True
    
    # recursively call to left OR right child with sum - root.val
    return self.hasPath(root.left, sum - root.val) or self.hasPath(root.right, sum - root.val)
```