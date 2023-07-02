
class BinaryTree: 
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
