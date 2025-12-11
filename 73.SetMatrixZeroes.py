'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.
Example 1: 
        +---+---+---+             +---+---+---+
        | 1 | 1 | 1 |             | 1 | 0 | 1 |
        +---+---+---+     ==>     +---+---+---+
        | 1 | 0 | 1 |             | 0 | 0 | 0 |
        +---+---+---+             +---+---+---+
        | 1 | 1 | 1 |             | 1 | 0 | 1 |
        +---+---+---+             +---+---+---+
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    
Example 2:
        +---+---+---+---+             +---+---+---+---+
        | 0 | 1 | 2 | 0 |             | 0 | 0 | 0 | 0 |
        +---+---+---+---+     ==>     +---+---+---+---+
        | 3 | 4 | 5 | 2 |             | 0 | 4 | 5 | 0 |
        +---+---+---+---+             +---+---+---+---+
        | 1 | 3 | 1 | 5 |             | 0 | 3 | 1 | 0 |
        +---+---+---+---+             +---+---+---+---+
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
Solution: We can use some extra-space to build 2 auxiliary arrays: 
            1. r_aux, to store the r-th index (on the rows) where we found a 0
            2. c_aux, to store the c-th index (on the columns) where we found a 0
        At the beginning both arrays are filled with 1's, and each time we find a 0 in matrix (matrix[r][c]==0) we write a 0 into the respective c_aux (c_aux[c]=0), 
        and r_aux (r_aux=0) 
        
                +---+---+---+---+
                | 0 | 1 | 1 | 0 |               
                +---+---+---+---+               
        
        +---+   +---+---+---+---+               +---+---+---+---+
        | 0 |   | 0 | 1 | 2 | 0 |               | 0 | 0 | 0 | 0 |
        +---+   +---+---+---+---+     ==>       +---+---+---+---+
        | 1 |   | 3 | 4 | 5 | 2 |               | 0 | 4 | 5 | 0 |
        +---+   +---+---+---+---+               +---+---+---+---+
        | 1 |   | 1 | 3 | 1 | 5 |               | 0 | 3 | 1 | 0 |
        +---+   +---+---+---+---+               +---+---+---+---+
We can avoid the extra space by modifiying the matrix itself along their columns at 0th row and their rows at 0th column. As well as before, we replace whatever value has with a 0. 
Since matrix[0][0] will overlaps for rows and columns, we are going to create a flag in order to know if the whole 0th column needs to be set to 0. 
    1. Then iterate over the matrix starting at 1 for both rows and columns
    2. Iterate only over 0th row and 0th column depending if the already have a 0     
        +---+---+---+               +---+---+---+---+           +---+---+---+---+   
        | 1 | 1 | 1 |               | F | 1 | 0 | 1 |           | F | 1 | 0 | 1 |            
        +---+---+---+     ==>       +---+---+---+---+           +---+---+---+---+
        | 1 | 0 | 1 |                   | 0 | 0 | 1 |      ==>      | 0 | 0 | 0 |           
        +---+---+---+                   +---+---+---+               +---+---+---+
        | 1 | 1 | 1 |                   | 1 | 1 | 1 |               | 1 | 0 | 1 |
        +---+---+---+                   +---+---+---+               +---+---+---+
'''
'''def setZeroes(matrix: list[list[int]]) -> None: #T: O(m*n), S: O(m+n)
    rows, columns = len(matrix), len(matrix[0])
    r_aux, c_aux = [1]*rows, [1]*columns
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                r_aux[r] = 0
                c_aux[c] = 0
    for r in range(rows):
        for c in range(columns):
            if r_aux[r] == 0 or c_aux[c] == 0:
                matrix[r][c] = 0'''

def setZeroes(matrix: list[list[int]]) -> None: #T: O(m*n), S: O(1)
    rows, columns = len(matrix), len(matrix[0])
    row_zero = False
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r>0:
                    matrix[r][0] = 0
                else:
                    row_zero=True
    for r in range(1,rows):
        for c in range(1,columns):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    if row_zero:
        for c in range(columns):
            matrix[0][c] = 0