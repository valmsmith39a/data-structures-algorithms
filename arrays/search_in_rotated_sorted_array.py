from typing import List

class SearchInRotatedSortedArray: 
    """
    Problem: Search in Rotated Sorted Array (#33) 

    Key Insight: 
    1. Binary search 
    2. Figure out if the left side or right side is sorted 
    3. Figure out if the target is on the left side or right side 

    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    """

    def search(self, nums: List[int], target: int) -> int: 
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] == target: 
                return mid 

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1 
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else: 
                    right = mid - 1 

        return -1 
        