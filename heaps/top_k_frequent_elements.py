from typing import List 

class TopKFrequentElements:
    """
    Problem: Top K Frequent Elements (#347) 

    Key Insights: 
    1. Can solve with Heap in O(n log n)
    2. Can also solve with Bucket Sort in O(n) time 
        a. HashMap to track count 
        b. frequency list to track frequency
            i. index is the frequency (so max number of times element appears is len(nums))
            ii. Each index has a list of numbers that has that frequency (count)

    Time Complexity: O(n) time
    Space Complexity: O(n) space 
    """
    def top_k_frequent(self, nums: List[int], k: int):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: 
                    return res 
