import unittest 
from longest_repeating_char_replacement import LongestRepeatingCharReplacement

class TestLongestRepeatingCharReplacement(unittest.TestCase):

    def setUp(self):
        self.lr = LongestRepeatingCharReplacement()

    def test_longest_repeating_char_replacement(self):
        self.assertEquals(self.lr.character_replacement("ABAB", 2), 4)
        self.assertEquals(self.lr.character_replacement("AABABBA", 1), 4)

if __name__ == '__main__':
    unittest.main()
