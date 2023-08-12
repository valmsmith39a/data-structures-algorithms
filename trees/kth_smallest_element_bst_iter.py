
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

class KthSmallestElementBSTIter:
    """
    Problem: Kth Smallest Element in BST (#230) 

    Iterative Solution 

    Key Insights: 
    1. For BST, left child key < current key < right child key 
    2. Traverse the BST in-order, collect the nodes 
    3. Short circuit when hit kth node 

                3 
             2      5
          1     4

        stack:  
        curr: 3, 2, 1, None, 1, None, 2, 4, None, 4, None, 3 
        n:    1, 2, 3, 4 
        k: 4
        answer: 3

    Time Complexity: 
    1. Best case: O(k)
    2. Worst Case: O(N), bc k = N, N: all the nodes in the tree 

    Space Complexity: 
    1. For balanced tree: O(log N), bc Height of tree = log N, N: number of nodes in the tree  
    2. Worst case (linked-list of nodes): O(N), N: number of nodes in the tree 
    """

    def kth_smallest(self, root: TreeNode, k: int) -> int:
        curr = root 
        stack = []
        n = 0

        while curr or stack: 
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k: 
                return curr.val 
            curr = curr.right 
            