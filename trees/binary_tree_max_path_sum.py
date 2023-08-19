
class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

class BinaryTreeMaxPathSum:
    """
    Problem: Binary Tree Max Path Sum (#124)

    Key Insights: 
    1. Find max path sum at each node 
        a. Split path (get max path sum using left child and right child) 
        b. Don't split (get the max path sum using left child or right child)
    2. Global max could be the path where we don't split 
    3. Return the max of split path values to parent node 

    Time Complexity: O(n) time bc traverse through all the nodes 
    Space Complexity: O(h) space because recursive call stack is the height of the tree
        a. height of tree could be n nodes in worst case (skewed tree)
        b. height of tree could be log n nodes in average case (balanced tree)
    """

    def maxPathSum(self, root: TreeNode) -> int:

        self.global_max = root.val

        def dfs(root):
            
            if not root:
                return 0
            
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            self.global_max = max(self.global_max, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)

        return self.global_max
