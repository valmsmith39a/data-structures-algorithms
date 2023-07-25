import unittest
from pacific_atlantic import PacificAtlantic

class TestPacificAtlantic(unittest.TestCase):

    def setUp(self):
        self.pa = PacificAtlantic()

    def test_pacific_atlantic(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        self.assertEquals(self.pa.pacific_atlantic(heights), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

if __name__ == '__main__':
    unittest.main()
