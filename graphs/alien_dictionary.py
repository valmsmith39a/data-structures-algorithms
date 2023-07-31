from typing import List

class AlienDictionary:
    """
    Problem: Alien Dictionary(#269)

    Key Insights:
    1. Compare words, if character not the same, add to adjacency list 
    2. Traverse using post-order DFS

    Context: 
    Topological Sort: 
    1. For Directed Acyclic Graph only (no cycles)
    2. For every directed edge (u, v), u comes before v 
    3. Must do a post-order DFS traversal: process the character (add to res) after DFS has visited all descendent nodes 

    Time Complexity: O(n), n is number of characters in all the words
    Space Complexity: O(n) space, n is number of characters in all the words 
    """

    def alien_order(self, words: List[str]) -> str: 
        adj = { c:set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break 
        
        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True 
            visited[c] = False 
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)