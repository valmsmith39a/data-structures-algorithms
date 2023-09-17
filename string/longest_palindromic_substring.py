
class LongestPalindromicSubstring:

    def longestPalindrome(self, s: str) -> str: 
        """
        Problem: Longest Palindromic Substring 

        Key Insight: 
        1. L, R pointers set to i,i and i,i+1 to handle odd / even length palindromes 
        Runtime: O(n^2)
        Space Complexity: O(n)
        
        """
        res = ""
        res_len = 0

        for i in range(len(s)):

            L = R = i 

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > res_len:
                    res = s[L:R+1]
                    res_len = R - L + 1

                L -= 1
                R += 1

            L, R = i, i + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > res_len: 
                    res = s[L:R+1]
                    res_len = R - L + 1

                L -= 1
                R += 1
            
            L, R = i, i + 1 

        return res 