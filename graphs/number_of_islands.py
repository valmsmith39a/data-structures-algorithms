from typing import List 

class NumberOfIslands:
    """
    Problem: Number of Islands (#200)

    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Key Insight: 
    1. Traverse the graph using depth first search and flip all the 1s to 0s 

    Time Complexity: O(mn) time 
    Space Complexity: O(mn) space, bc of the recursive call stack. In the worst case, all the cells are '1's
    """

    def numberOfIslands(self, grid: List[List[int]]) -> int: 

        if not grid: 
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r > ROWS - 1 or c > COLS - 1 or 
                grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_of_islands += 1

        return num_of_islands
