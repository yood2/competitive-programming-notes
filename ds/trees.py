class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(Node(data))

class Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def add(self, data):
        self.root.add_child(data)

'''
DFS = Depth First Search
'''
def dfs(self, target):
    stack = [self.root]
    while stack:
        current_node = stack.pop()
        if current_node.data == target:
            return True
        stack.extend(current_node.children)
    return False

'''
BFS = Breadth First Search
'''
def bfs(self, target):
    queue = [self.root]
    while queue:
        current_node = queue.pop(0)
        if current_node.data == target:
            return True
        queue.extend(current_node.children)
    return False
