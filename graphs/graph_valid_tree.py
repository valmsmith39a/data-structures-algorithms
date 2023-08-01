from typing import List 

class GraphValidTree:
    """
    Problem: Graph Valid Tree (#261)

    Key Insight: 
    1. If can DFS through all the nodes with no cycle, then have a valid tree 

    Time Complexity: O(n) time, cycle through all the nodes once (in a tree, V = E, so simplifies to O(n)) 

    Space Complexity: O(n) space 
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 
        
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False 

            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue 
                if not dfs(j, i):
                    return False 
            return True 
        
        return dfs(0, -1) and n == len(visited)

