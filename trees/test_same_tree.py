import unittest
from same_tree import SameTree, TreeNode

class SameTreeTest(unittest.TestCase):

    def setUp(self):
        self.st = SameTree()

    def test_same_tree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        self.assertTrue(self.st.is_same_tree(p, q))

    def test_not_same_tree(self):
        # Node values are different
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        q = TreeNode(1)
        q.left = TreeNode(5)
        q.right = TreeNode(3)

        self.assertFalse(self.st.is_same_tree(p, q))

        # Tree structures are different 
        p.left.left = TreeNode(4)
        p.left.right = TreeNode(5)

        self.assertFalse(self.st.is_same_tree(p, q))

if __name__ == "__main__":
    unittest.main()
