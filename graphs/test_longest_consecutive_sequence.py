import unittest 
from longest_consecutive_sequence import LongestConsecutiveSequence

class TestLongestConsecutiveSequence(unittest.TestCase):

    def setUp(self):
        self.lcs = LongestConsecutiveSequence()

    def test_longest_consecutive_sequence(self):
        self.assertEquals(self.lcs.longest_consecutive([100,4,200,1,3,2]), 4)
        self.assertEquals(self.lcs.longest_consecutive([0,3,7,2,5,8,4,6,0,1]), 9)

if __name__ == '__main__':
    unittest.main()
