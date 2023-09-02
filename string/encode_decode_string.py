from typing import List

class EncodeDecodeString:
    """
    Problem: Encode Decode String (#271) 

    Key Insights:
    1. Encode using count of word + # delimiter 

    Time Complexity: O(N) for both encode / decode 
    Space Complexity: O(N) for both encode / decode 
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 
    
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length 
        return res 
        