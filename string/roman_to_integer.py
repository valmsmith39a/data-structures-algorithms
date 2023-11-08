class RomanToInteger: 
    """
    Problem: Roman to Integer 

    Key Insights: 
    1. Work backwards 
    2. If current character >= prev character then sum, else subtract 

    Time Complexity: O(n) 
    Space Complexity: O(1)
    """

    def roman_to_int(s: str) -> int:
        roman_values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else: 
                total += value 
            prev_value = value 

        return total 
    