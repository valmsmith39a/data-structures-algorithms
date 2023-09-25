
class ValidAnagram:
    """
    Problem: Valid Anagram (#242)

    Key insight: 
    1. Count the number of occurrences of each character in each string 

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1 
        
        for k in countS:
            if countS[k] != countT.get(k, 0):
                return False 
            
        return True 
        