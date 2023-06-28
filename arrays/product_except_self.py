from typing import List

class ProductExceptSelf:
    """
    Problem: Product Except Self

    Constraints:
    1. Must be O(n) time, try O(1) space where result array does not count 
    2. Cannot use division operator 

    Key Insights: 
    1. Compute prefix / postfix 
    2. Use the result array to store prefix and final solution 
    """

    def product_except_self(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pre 
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post 
            post *= nums[i]

        return res 
