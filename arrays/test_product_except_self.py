import unittest
from product_except_self import ProductExceptSelf

class ProductExceptSelfTest(unittest.TestCase):

    def setUp(self):
        self.pes = ProductExceptSelf()

    def test_product_except_self(self):
        self.assertEqual(self.pes.product_except_self([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.pes.product_except_self([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == '__main__':
    unittest.main()
