from typing import List 

class MinimumInSortedArray:
    """
    Problem: Minimum In Sorted Array (#153)

    Key Insights: 
    1. if the mid value is greater than the right value, min value is on the right side of mid value 
    2. if the mid value is less than the right value, min value is on the left side of the mid value 

    Time Complexity: O(log n) 

    Space Complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int: 

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            
            if nums[mid] > nums[right]:
                left = mid + 1 
            else: 
                right = mid 

        return nums[left]
