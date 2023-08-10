class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None

class LowestCommonAncestorBST:
    """
    Problem: Lowest Common Ancestor of Binary Search Tree (#235)

    Key Insights: 
    1. Binary Search Tree: 
        a. All node values (keys) in the left subtree are less than the current node's value 
        b. All node values in the right subtree are greater than the current node's value 
        c. Nodes cannot have the same keys
    2. Find the node that splits the values 
        a. if both nodes are less than the current node, look left 
        b. if both nodes are greater than the current node, look right 
        c. if one is greater than and one is less than the current node, that is the lowest common ancestor. 
        d. if one node is ancestor of the other node, then that node is the lowest common ancestor 
    
    Time Complexity: 
    1. Average case: O(log n)
        a. For BST that is balanced, you only visit 1 node at each level. So the runtime is roughly the height of the tree, which is log n time.
    2. Worst case: O(n)
        a. For an unbalanced BST where every node is child of previous node to form a linked list, height of the tree is n 
    
    Space Complexity: O(1) 
    
    """
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:

            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            elif p.val > curr.val and q.val > curr.val: 
                curr = curr.right 
            else: 
                return curr 
