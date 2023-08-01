import unittest 
from graph_valid_tree import GraphValidTree

class TestGraphValidTree(unittest.TestCase):

    def setUp(self):
        self.gvt = GraphValidTree()

    def test_graph_valid_tree(self):
        self.assertEquals(self.gvt.valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]), True)
        self.assertEquals(self.gvt.valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]), False)

if __name__ == '__main__':
    unittest.main()
