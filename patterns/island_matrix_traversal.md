# Island Pattern (Matrix Traversal)
## Summary
Many problems involve traversing 2D arrays (aka matrix or grid). Island pattern describes all the efficient ways to traverse a matrix.
## Key Characteristics
- Can use DFS or BFS
## General Implementation
```python
def dfs(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        # not a valid cell (out of bounds)
        return 
    if matrix[x][y] == 0:
        # water cell
        return
    matrix[x][y] = 0 # similar to marking a cell as visited

    # recursively check surrounding cells
    dfs(matrix, x+1, y)
    dfs(matrix, x-1, y)
    dfs(matrix, x, y+1)
    dfs(matrix, x, y-1)


def countIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                totalIslands += 1
                dfs(matrix, i, j)
    
    return totalIslands
```