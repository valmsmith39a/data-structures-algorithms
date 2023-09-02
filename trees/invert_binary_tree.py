
class BinaryTree: 
    """
    Problem: Invert Binary Tree #226

    Key Insights: 
    1. Pre-order operation (swap-first) Depth-first Search

    Time Complexity: O(n)

    Space Complexity: 
    1. Balanced Tree: O(log n)
    2. Skewed Tree: O(n) 
    """
    def invert_binary_tree(self, node):
        if (node == None):
            return
        node.left, node.right = node.right, node.left 
        self.invert_binary_tree(node.left)
        self.invert_binary_tree(node.right)

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None  
