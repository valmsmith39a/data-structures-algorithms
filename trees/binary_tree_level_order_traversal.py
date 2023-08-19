import collections 
from typing import List, Optional

class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

class BinaryTreeLevelOrderTraversal:
    """
    Problem: Binary Tree Level Order Traversal 

    Key Insights:
    1. Use a queue
    2. Collect values in each level in a list  

    Time Complexity: O(n) time bc traverse through all the nodes in the tree 
    Space Complexity: O(n) space
        1. Collect all the values of the nodes in the tree 
        2. q can have at most n / 2 values O(n/2) -> O(n)
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)
            if level:
                res.append(level)

        return res 
