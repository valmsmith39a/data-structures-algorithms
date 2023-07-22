import unittest
from insert_interval import InsertInterval

class TestInsertInterval(unittest.TestCase):

    def setUp(self):
        self.ins = InsertInterval()

    def test_insert(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        self.assertEquals(self.ins.insert(intervals, newInterval), [[1,5],[6,9]])

        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        self.assertEquals(self.ins.insert(intervals, newInterval), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()
