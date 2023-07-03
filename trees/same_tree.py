from __future__ import annotations 
from typing import Optional

class SameTree:
    """
    Problem: Same Tree (#100)

    Key Insight:
    1. Depth-first search to compare each node 

    Time Complexity: O(n) time to traverse all the nodes 
    Space Complexity: O(log n) space - recursive call stack for balanced tree and O(n) space for imbalanced tree (single line left child nodes or right child nodes)
    """

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        