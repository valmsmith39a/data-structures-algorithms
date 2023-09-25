from collections import defaultdict
from typing import List 

class GroupAnagrams: 
    """
    Problem: Group Anagrams (#49) 

    Key Insights: 
    1. Use count of characters as dictionary key 

    Time Complexity: O(m * n), m: number of strings, n: max number of characters in string
    Space Complexity: O(m * n)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        
        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26 

            for c in s: 
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
