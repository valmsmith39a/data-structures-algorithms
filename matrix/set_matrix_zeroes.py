from typing import List

class SetMatrixZeroes:
    """
    Problem: Set Matrix Zeroes (#73) 

    Problem Description: 
    Given an m x n integer matrix, if an element is 0, set its 
    entire row and columns to 0's

    Must be done *in place*.

    Key Insights: 
    1. Use first row to indicate which columns must be 0s.
    2. Use first column (except the first cell) to indicate which rows must be 0s.
        a. Use an extra cell to indicate if the first row must be 0s. 
        This is because the first cell is used in step 1 to tell if the 
        first column must be 0s. 
    
    Time Complexity: O(mn) time because need to traverese all the cells of the matrix
    Space Complexity: O(1) space because of the extra cell rowZero - we don't count memory of the initial matrix    
    """

    def set_zeros(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False 

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0: 
                        matrix[r][0] = 0
                    else: 
                        rowZero = True 

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
