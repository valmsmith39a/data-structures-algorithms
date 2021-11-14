class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.children = [n2, n3]
n2.children = [n4, n5]
n4.children = [n6]
n5.children = [n7]

array = []

print(n1.depthFirstSearch(array))

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

n0 = BinaryTree(0)
n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
 # 3
print(height(n0))
                                         
