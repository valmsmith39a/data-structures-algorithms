import unittest
from max_depth_binary_tree import MaxDepthBinaryTree, TreeNode

class MaxDepthBinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.md = MaxDepthBinaryTree()

    def test_max_depth_binary_tree(self):
        node = None 
        self.assertEquals(self.md.max_depth(node), 0)

        node = TreeNode(1)
        self.assertEquals(self.md.max_depth(node), 1)

        node.left = TreeNode(2)
        node.right = TreeNode(3)
        self.assertEquals(self.md.max_depth(node), 2)

        node.left.left = TreeNode(4)
        node.left.right = TreeNode(5)
        self.assertEquals(self.md.max_depth(node), 3)

if __name__ == "__main__":
    unittest.main()
