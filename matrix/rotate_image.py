from typing import List

class RotateImage:
    """
    Problem: Rotate Image (#48)

    Problem Description:
    Given n x n 2D matrix, rotate the image by 90 degrees (clockwise)
    Must rotate the image in-place (do not allocate another 2D matrix)

    Key Insights: 
    1. Rotate values counter clockwise, ex left col to top col
    2. Save value in top call to topLeft for each iteration 

    Steps:
    1. Use l, r, top, bottom pointers and move with +/- i
    2. Save values in top row top left cell in each iteration
    3. Rotate values counter clockwise 
        a. left col to top row 
        b. bottom row to left col 
        c. right col to bottom row 
        d. topLeft to right col 
    4. Increment l pointer, decrement r pointer 
    5. Do this rotation r - l times (n - 1)    

    Time Complexity: 
    O(n^2) time: Traverse every cell 
    O(1) space: Only create topLeft variable to store value from top row 
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            top, bottom = l, r

            for i in range(r - l):
                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1
        