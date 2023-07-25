from typing import List

class PacificAtlantic:
    """
    Problem: Pacific Atlantic Water Flow (#417) 

    Key Insights: 
    1. Iterate through cells in first / last rows and first / last columns to determine which cells can flow to Pacific / Atlantic 
        a. cell height >= prev cell height => water can flow from cell to Pacific / Atlantic
    2. Depth-first search to find the cells that can flow to Pacific / Atlantic 
    
    Time Complexity: O(mn) time, bc visit each cell at most once  
    Space Complexity: O(mn) space, bc res could be all the cells 
    """

    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or 
                (r, c) in visited or
                heights[r][c] < prev_height):
                return 
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res 
