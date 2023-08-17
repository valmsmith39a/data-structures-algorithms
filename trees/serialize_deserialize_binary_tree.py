
class SerializeDeserializeBinaryTree:
    """
    Problem: Serialize and Deserialize Binary Tree (#297) 

    Key Insights: 
    1. pre-order depth first search 

    Time Complexity: 
    1. Serialize / Deserialize: O(n)

    Space Complexity: O(n) space 
    1. values: O(n)
    2. recursive stack:
        a. average case: O(log n)
        b. worst case: O(n)
    """

    def serialize(self, root):

        res = []

        def dfs(node):

            if not node: 
                res.append("N")
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)

    def deserialize(self, data):

        values = data.split(",")
        self.i = 0

        def dfs():

            if values[self.i] == "N":
                self.i += 1
                return 
            
            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            
            return node 
        
        return dfs()

            