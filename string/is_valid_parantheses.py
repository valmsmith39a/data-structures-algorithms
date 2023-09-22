
class IsValidParantheses:
    """
    Problem: Is Valid Parantheses (#20)

    Key Insights: 
    1. stack of open parantheses 
    2. map of closed to open parantheses 
    
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = { ")": "(", "]": "[", "}": "{" }

        for c in s: 
            if c in closed_to_open:
                if stack and stack[-1] == closed_to_open[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        return True if not stack else False 
        