from typing import Optional 

class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None

class IsSubtree:
    """
    Problem: Is Same Tree (#572) 

    Key Insights: 
    1. Use depth-first search to compare subtree with each subtree at each node in the tree.

    Time Complexity: 
    1. sameTree: O(min(r,s)), r: number of nodes root tree, s: number of nodes in subRoot tree
        a. Stop at the number of nodes in the smaller tree
    2. isSubtree: O(r)
    3. Overall: O(r * min(r, s)) 
        a. In worst case (tree is an unbalanced linked-list), would call is Subtree O(r) times. 
        b. For each isSubtree call, calling sameTree

    Space Complexity: 
    1. sameTree:
        a. average case (balanced tree): O(log min(r, s))
        b. worse case (linked-list): O(min(r, s))
    2. isSubtree: 
        a. average case (balanced tree): O(log r)
        b. worst case: O(r)
    3. Overall: 
        a. average case: O(max(log r, log min(r, s))) -> O(log r), bc log r will always be >= log min(r, s)
        b. worst case: O(r)
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True 
        if not root: return False

        if self.sameTree(root, subRoot):
            return True 
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        


    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        
        return False 
