# Graphs
## Summary
A graph is a data structure that consists of a set of vertices/nodes and a bunch of edges connecting these vertices. 
## Key Characteristics
- Used to model relationships and connections between entities.
- Can be represented using Adjacency Matrix or Adjacency List.
- Can traverse a Graph using DFS or BFS.
## Common Terminology
- Adjacent Nodes: if edge connects nodes directly.
- Directed Graph/Digraph: directed graph, or graph where edges have a direction.
- Loop in Graph: edge that connects node to itself.
- Degree of a node: number of edges connected to it.
- Weighted Graph: edge is associated with a weight.
- Connected Graph: graph where there is a path between every pair of vertices (nodes).
- Disconnected Graph: two or more subgraphs with no direct connection between components.
- Strongly Connected Graph: directed graph in which there is a directed path from every vertext to every other vertex.
## Adjacency Matrix Representation
Basically a square matrix where the rows and columns represent the vertices of the graph, with entries that indicate whether there is an edge between the vertices.
#### Adjacency Matrix for Directed/Undirected Graphs
Undirected matrix will just be a N x N matrix. Each entry will have value of 1 or 0 (1 if there is a edge present).

Directed matrix is similar but the corresponding vertice combination might have a 0. Eg. A[i][j] might be a 1 but A[j][i] will be a 0.
## Adjacency List Representation
Adjacency list is basically a list where the key is the vertice you want to check. The value of the key is going to be a list with all the nodes it is connected.

If it is directed, the list will consist of the vertices it is directed to.
## ADT Implementation
```python
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex):
        # check if vertex already exists
        # add by inserting new key-value pair
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return 
        self.adjacency_list.pop(vertex)
        for neighbors in self.adjacency_list.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        
    def get_vertices(self):
        return list(self.adjacency_list.keys())
        
    def get_edges(self):
        edges = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if vertex < neighbor:
                    edges.append((vertex, neighbor))
        return edges
    
    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def is_adjacent(self, vertex1, vertex2):
        return vertex2 in self.adjacency_list[vertex1]
    
    def get_vertex_count(self):
        return len(self.adjacency_list)
    
    def get_edge_count(self):
        count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return count // 2
```
## Graph Traversal
Graph traversal involves visiting all nodes following a specific strategy or order. During traversal, visited nodes are usually marked to avoid revisiting. We usually traverse with DFS or BFS.
#### DFS
Explores all nodes by visiting as far as possible before backtracking. Operates on both directed and undirected and is implemented using recursion or stack.
1. Initialize with a starting node and a data structure to keep track of visisted nodes. Mark the starting node as visited.
2. Visit the current node (perform the operation you need to do).
3. Recursive Approach: for each unvisited neighbor, recursively call DFS and mark the neighbor as visited.
3. Stack Approach: Push starting node onto stack. While stack not empty, pop a node (curr), process curr, for each unvisited neighbor push the unvisisted and mark as visited.
4. Backtracking. If no more unvisisted neighbors for current node, backtrack by returning (recursive) or popping nodes from stack.
5. Terminate algorithm when all nodes reachable have been visited.
```python
# implying we have a int var with number of vertices
# implying we have a adjList in graph already
def dfs(start):
    visisted = [False] * vertices
    stack = []
    stack.append(start)
    visited[start] = True
    while stack:
        curr = stack.pop()
        
        # Visit function here
        print(curr) 

        for neighbor in adjList[curr]:
            if not visisted[neightbor]:
                stack.append(neighbor)
                visited[neighbor] = True
```
#### BFS
BFS explores vertices level by level. Starts from a selected node and moves outware to visit all nodes at same distance from source.

BFS is particularly useful for finding the shortest path in unweighted graphs and for systematically exploring graphs.
1. Use a queue to keep track of nodes to be visisted.
2. Initialize by selecting a source node (put in queue) and mark source as visisted.
3. While queue is not empty, dequeue node from front, process/visit, enqueue all unvisited neighbors, mark each enqueued as visited.
4. Terminate algo when queue becomes empty.
```python
def bfs(start):
    visited = [False] * vertices
    q = deque()

    visisted[startVertex] = True
    q.append(startVertex)

    while q:
        currentVertex = q.popleft()
        print('Visit function here')

        for neighbor in self.adjList[currentVertex]:
            if not visisted[neighbor]:
                visisted[neighbor] = True
                q.append(neighbor)
```