import unittest 
from top_k_frequent_elements import TopKFrequentElements

class TestTopKFrequentElements(unittest.TestCase):

    def setUp(self):
        self.tk = TopKFrequentElements()

    def test_top_k_frequent(self):
        self.assertEquals(self.tk.top_k_frequent([1,1,1,2,2,3], 2), [1,2])
        
if __name__ == '__main__':
    unittest.main()
    