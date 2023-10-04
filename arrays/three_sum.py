from typing import List 

class ThreeSum:
    """
    Problem: Three Sum (#15) 

    Key Insights: 
    1. Use 2 pointers 
    2. Sort list 
    3. if s < 0, only way to make sum bigger is to move left pointer forward. 
    4. if s > 0, only way to make sum smaller is to move right pointer backward. 

    Time Complexity: O(n^2) 
    n - 1 + n - 2 + n - 3... + 1 = (n - 1) 

    Sum of first N numbers = N(N+1) / 2 
    (n -1)(n - 1 + 1) / 2 = (n^2 - n) / 2 => n^2 (the highest degree term)

    Space Complexity: O(n^2)
    
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1
            
            while left < right: 
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0: 
                    right -= 1 
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1 
                    right -= 1
        return res 
