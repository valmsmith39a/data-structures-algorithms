from typing import List 

class ContainerWithMostWater:
    """
    Problem: Container with Most Water (#11)  

    Key Insights: 
    1. 2 pointer 
    2. Move pointer with smaller height because hope to find a taller height 

    Time Complexity: O(n) time 
    Space Complexity: O(1) space
    """

    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        left, right = 0, len(height) - 1

        while left < right: 
            width = right - left 
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1 
            else: 
                right -= 1 

        return max_area
