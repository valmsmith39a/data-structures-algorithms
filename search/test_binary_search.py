import unittest 
from binary_search import BinarySearch

class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch()
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_search_recursive(self):
        # Target found 
        target = 2
        expected_idx = 1
        self.assertEqual(self.bs.search(self.arr, target), expected_idx)

        target2 = 6
        expected_idx2 = 5
        self.assertEqual(self.bs.search(self.arr, target2), expected_idx2)
        
        # Target not found 
        target3 = 12
        expected_idx3 = -1
        self.assertEqual(self.bs.search(self.arr, target3), expected_idx3)

    def test_search_iterative(self):
        # Target found
        target = 2
        expected_idx = 1
        self.assertEqual(self.bs.search_iterative(self.arr, target), expected_idx)

        target2 = 6
        expected_idx2 = 5
        self.assertEqual(self.bs.search_iterative(self.arr, target2), expected_idx2)

        # Target not found
        target3 = 12
        expected_idx3 = -1
        self.assertEqual(self.bs.search_iterative(self.arr, target3), expected_idx3)

if __name__ == '__main__':
    unittest.main()
