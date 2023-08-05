from typing import List 

class NumberConnectedComponents:
    """
    Problem: Number of Connected Components in Undirected Graph (#323)

    Key Insights: 
    1. Use Union Find algorithm 
    2. Path compression to optimize find fn and Union by rank to optimize union fn 

    Time Complexity: O(v + e), v: vertices, e: edges, traverse all the nodes and edges  
    Space Complexity: O(v) space, to maintain the par and rank lists 

    Background: 
    1. Union Find
        a. 1964 by Bernard A Galler Michael J Fischer 
    2. Path compression: 
        a. Jump to the grandparent of the node 
    3. Union by Rank: 
        a. rank: height of each tree, height: number of edges between the root and deepest leaf node 
        b. Ensures trees representing the sets are balanced and do not become too deep (which would increase run-time to traverse to root node)
    """

    def count_components(self, n: int, edges: List[List[int]]):
        # Each node begins with itself as the root
        par = [i for i in range(n)]

        # Rank is upper bound of height of each tree for each node 
        rank = [0] * n 

        def find(n1):
            res = n1 
            while res != par[res]:
                # Path compression optimization 
                par[res] = par[par[res]]
                res = par[res]
            return res 
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0 
            
            # Union by rank optimization 
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else: 
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n 
        
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res 
    