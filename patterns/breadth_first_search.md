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

NOTE: You can use a list but dequeues are optimized to have $O(n)$ pops/appends from either side.
```python
def bfs(head):
    queue = deque([head])

    while queue:
        node = queue.popleft()
        if not node:
            continue
        queue.append(node.left)
        queue.append(node.right)
```
## Level Order Traversal with BFS
General idea is to keep track of each level you are on.
```python
def bfs(head):
    queue = deque([head])
    levels = []

    while queue:
        curr_level = []
        curr_level_length = len(queue)
        for _ in range(curr_level_length):
            curr = queue.popleft()
            if not curr:
                continue
            queue.append(curr.left)
            queue.append(curr.right)
            curr_level.append(curr.val)
        levels.append(curr_level)
    
    return levels
```
