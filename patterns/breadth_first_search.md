# Breadth First Search
## Summary
BFS is a technique to traverse a tree. Any problem involving traversal of a tree in a level-by-level order can be solved using this approach.
For BFS, we will use a queue to keep track of all the nodes of a level before we jump onto the next level.
## Key Characteristics
- BFS is usually used to find the shortest path in a graph.
- Time complexity is O(V + E) where V is the number of vertices and E is the number of edges.
- Space complexity is O(V) where V is the number of vertices.
## General Format
General idea is that we make a queue and put every node we will visit into the queue. First node we pop is the head. We add all the children, than pop to the next in queue (which should be a child of the head). Next, we add all those children, and so forth. Next few we pop will all be on the same level.
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
