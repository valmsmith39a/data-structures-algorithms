from __future__ import annotations
from typing import Optional 

class MaxDepthBinaryTree:
    """
    Problem: Max Depth of Binary Tree (#104) 
    
    Key Insights:
    1. Max depth in this case is number of nodes from root to leaf node 
    2. Depth-first search from root node to deepest leaf node and return max of left / right branches + 1

    Time Complexity: O(n) time because need to traverse every single node 
    Space Complexity: O(log n) time for average case (fairly balanced tree) and O(n) time for unbalanced tree
    """

    def max_depth(self, root: Optional[TreeNode]):
        if root == None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
