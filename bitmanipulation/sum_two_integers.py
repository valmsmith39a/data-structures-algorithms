class SumTwoIntegers: 

    """
    Problem SumTwoIntegers 

    Key Insights: 
    1. Use bit manipulation XOR and left shift 

    Time Complexity: O(1) bc each integer contains 32 bits 
    Space Complexity: O(1) bc do not use additional data structures
    """

    def getSum(a: int, b: int) -> int:
        mask = 0xFFFFFFFF 
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
