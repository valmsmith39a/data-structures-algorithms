import unittest 
from alien_dictionary import AlienDictionary

class TestAlienDictionary(unittest.TestCase):

    def setUp(self):
        self.ad = AlienDictionary()
        

    def test_alien_order(self):
        self.assertEquals(self.ad.alien_order(["wrt","wrf","er","ett","rftt"]), "wertf")

if __name__ == '__main__':
    unittest.main()
