
class LongestRepeatingCharReplacement:
    """
    Problem: Longest Repeating Character Replacement (#424)

    Key Insights: 
    1. Track count of characters
    2. window length - max count = the number of characters to replace.
    3. window length - max count must be <= k
    4. If it's window length - max count > k, need to move left pointer, decrement

    Time Complexity: O(n) time 
    Space Complexity: O(n) space
    """

    def character_replacement(self, s: str, k: int):
        count = {}
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k: 
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
    