
class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

class ValidateBST:
    """
    Problem: Is Valid Binary Search Tree (#98) 

    Key Insights: 
    1. Depth-First Search with left and right boundaries 

    Time Complexity: 
    O(n) time, n: number of nodes in the tree  

    Space Complexity: 
    1. Average case (balanced tree): O(log n) space (height of the binary search tree)
    2. Worst case (skewed tree): O(n) space, n: number of nodes in tree 
    """

    def is_valid_bst(self, root: TreeNode) -> bool:

        def is_valid(node, left, right):
            if not node:
                return True 
            
            if not (node.val > left and node.val < right):
                return False 

            return (is_valid(node.left, left, node.val) and 
                    is_valid(node.right, node.val, right))
        
        return is_valid(root, float("-inf"), float("inf"))
