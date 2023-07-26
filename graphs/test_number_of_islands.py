import unittest 
from number_of_islands import NumberOfIslands

class TestNumberOfIslands(unittest.TestCase):

    def setUp(self):
        self.ni = NumberOfIslands()

    def test_number_of_islands(self):
        grid =  [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEquals(self.ni.numberOfIslands(grid), 1)
        
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEquals(self.ni.numberOfIslands(grid), 3)

if __name__ == '__main__':
    unittest.main()
