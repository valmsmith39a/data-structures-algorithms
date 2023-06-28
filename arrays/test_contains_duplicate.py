import unittest
from contains_duplicate import ContainsDuplicate

class ContainsDuplicateTest(unittest.TestCase):

    def setUp(self):
        self.cd = ContainsDuplicate()

    def test_empty(self):
        self.assertFalse(self.cd.contains_duplicate([]))

    def test_has_no_duplicates(self):
        self.assertFalse(self.cd.contains_duplicate([1,2,3,4]))

    def test_has_duplicates(self):
        self.assertTrue(self.cd.contains_duplicate([1,2,3,1]))
        self.assertTrue(self.cd.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == '__main__':
    unittest.main()
