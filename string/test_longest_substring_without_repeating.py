import unittest
from longest_substring_without_repeating import LongestSubstringWithoutRepeatingChars

class TestLongestSubstringWithoutRepeatingChars(unittest.TestCase):

    def setUp(self):
        self.ls = LongestSubstringWithoutRepeatingChars()
    
    def test_longest_substring(self):
        self.assertEquals(self.ls.len_of_longest_substring("abcabcbb"), 3)
        self.assertEquals(self.ls.len_of_longest_substring("bbbbb"), 1)
        self.assertEquals(self.ls.len_of_longest_substring("pwwkew"), 3)
     
if __name__ == '__main__':
    unittest.main()
