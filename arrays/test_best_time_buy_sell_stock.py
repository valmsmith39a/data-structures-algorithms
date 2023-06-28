import unittest 
from best_time_buy_sell_stock import BestTimeBuySellStock

class BestTimeBuySellStockTest(unittest.TestCase):

    def setUp(self):
        self.bt = BestTimeBuySellStock()

    def test_empty(self):
        self.assertEquals(self.bt.max_profit([]), 0)

    def test_max_profit(self):
        self.assertEquals(self.bt.max_profit([7,1,5,3,6,4]), 5)
        self.assertEquals(self.bt.max_profit([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()
