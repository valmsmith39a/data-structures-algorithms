from collection import deque 

class Graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, node1, node2):
        if node1 not in self.graph: 
            self.graph[node1] = [node2]
        else:
            self.graph[node1].append(node2)

    def dfs(self, start):
        visited = set()

        def dfs_recursive(node):
            if node not in visited: 
                    visited.add(node)
                    print(node, end=' ')
                    for neighbor in self.graph[node]:
                        dfs_recursive(neighbor)
        
        dfs_recursive(start)
    
    def bfs(self, start): 
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited: 
                visited.add(node)
                print(node, end=' ')
                queue.extend(self.graph[node])

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    