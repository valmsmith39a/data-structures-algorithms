from typing import List 

class MaximumProductSubarray:
    """
    Problem: Maximum Product Subarray (#152)

    Key Insights: 
    1. Compute current_max_product at each index 
    2. Must track current_min_product as well because if it's a large negative number and current number is negative number, then this would be the current_max_product 
    3. current_max_product is max(current number, current number * current_max_product, current number * current_min_product) 

    Time Complexity: O(n)

    Space Complexity: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0 

        current_max = nums[0] 
        current_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            temp_max = current_max 
            current_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_min = min(nums[i], nums[i] * temp_max, nums[i] * current_min)
            global_max = max(current_max, global_max)

        return global_max 
