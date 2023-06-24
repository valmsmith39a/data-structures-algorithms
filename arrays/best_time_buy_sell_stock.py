from typing import List

class BestTimeBuySellStock:
    """
    Problem: Best Time Buy Sell Stock (LeetCode #121)

    Key Insight:
    At each step, find the min price and max profit. 

    Time Complexity: O(n) time bc iterate through list of prices once.
    Space Complexity: O(1) space bc only track min price and max profit 
    """

    def max_profit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
