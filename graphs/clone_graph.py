
class CloneGraph:

    def clone_graph(self, node: 'Node') -> Node:
        if node is None:
            return None 
        
        queue = []
        clones = {}

        queue.append(node)
        clones[node] = Node(node.val, [])

        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]


class Node:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        