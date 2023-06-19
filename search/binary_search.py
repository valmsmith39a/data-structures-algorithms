from typing import List 

class BinarySearch:
    """
    This class implements Binary Search.

    Problem:
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

    Key Insight:
    Search for the target by recursively dividing the list in half 
    and look for the target in either the left or the right half.
    Each iteration reduces the search space by 1/2. 

    Time Complexity: 
    O(log n) time: Eliminates 1/2 of elements in each iteration.

    Space Complexity: 
    0(log n) space (recursive approach): Each iteration removes 1/2 of elements.
    O(1) (iterative approach): No elements stored. 
    """

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        return self.search_recursive(nums, target, 0, len(nums) - 1)

    def search_recursive(self, nums: List[int], target: int, left: int, right: int):

        if (left > right):
            return -1

        mid = left + (right - left) // 2       

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.search_recursive(nums, target, left, mid)
        else:
            return self.search_recursive(nums, target, mid + 1, right)

    def search_iterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid 
            else:
                left = mid + 1

        # Target not found 
        return -1 
