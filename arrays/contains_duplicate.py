from typing import List

class ContainsDuplicate:
    """
    Problem: Contains Duplicate (LeetCode #217)

    Key Insights:
    Store each number in a Set and if the number already exists, return True 

    Time Complexity: O(n) time: Iterate through the list once 
    Space Complexity: O(n) space: Possible to store all the numbers in the list, in the set.
    """

    def contains_duplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
