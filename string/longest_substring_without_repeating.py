
class LongestSubstringWithoutRepeatingChars:
    """
    Problem: Longest Substring Without Repeating Characters (#3)

    Key Insights: 
    1. Sliding window with left and right pointers 
    2. If char in char_set, move left pointer to the right
    and remove from char_set until char no longer in char_set 

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def len_of_longest_substring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
