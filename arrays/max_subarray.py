from typing import List 

class MaxSubarray:
    """
    Problem: Maximum Subarray (#53)

    Key Insight: 
    1. max subarray sum at each index is either the current number or the current number + max subarray sum up to that index
    2. Kadane's algorithm (dynamic programming)

    Time Complexity: O(n) 

    Space Complexity: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int: 
        
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], nums[i] + current_max)
            global_max = max(current_max, global_max)

        return global_max
