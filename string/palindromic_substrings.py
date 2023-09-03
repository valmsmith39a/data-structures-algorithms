
class PalindromicSubstrings:
    """
    Problem: Palindromic Substrings (#647)

    Key Insights: 
    1. left, right pointers for even / odd length palindroms 

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def countSubstrings(self, s: str) -> int: 
        res = 0

        for i in range(len(s)):

            l = r = i 
            res += self.countPali(s, l, r)

            l = i 
            r = i + 1 
            res += self.countPali(s, l, r)

        return res 
    
    def countPali(self, s, l, r):
        res = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1 
            l -= 1
            r += 1 
        
        return res 
