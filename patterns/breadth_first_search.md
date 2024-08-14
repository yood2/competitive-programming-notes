# Breadth First Search
## Summary
BFS is a technique to traverse a tree. Any problem involving traversal of a tree in a level-by-level order can be solved using this approach.

For BFS, we will use a queue to keep track of all the nodes of a level before we jump onto the next level.
## Key Characteristics
- BFS is usually used to find the shortest path in a graph.
- Time complexity is O(V + E) where V is the number of vertices and E is the number of edges.
- Space complexity is O(V) where V is the number of vertices.
## General Format
```python
def bfs(head):
    queue = deque(head)
    visited = set(head)

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left not in visited:
            visited.add(node.left)
            queue.append(node.left)
        if node.right not in visited:
            visited.add(node.right)
            queue.append(node.right)
```
