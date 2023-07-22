import unittest 
from merge_intervals import MergeIntervals

class TestMergeIntervals(unittest.TestCase):

    def setUp(self):
        self.mi = MergeIntervals()

    def test_merge_intervals(self):
        self.assertEquals(self.mi.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEquals(self.mi.merge([[1,4],[4,5]]), [[1,5]])

if __name__ == '__main__':
    unittest.main()
