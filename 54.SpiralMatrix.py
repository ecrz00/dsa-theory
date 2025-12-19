'''
Given an m x n matrix, return all elements of the matrix in spiral order.
[ 1 ] --> [ 2 ] --> [ 3 ]
                      |
                      v
[ 4 ] --> [ 5 ]     [ 6 ]
  ^                   |
  |                   v
[ 7 ] <-- [ 8 ] <-- [ 9 ]
Approach: The idea is to place 4 pointers (one at the left column, one at the right-most column, one at the top-most row and another at the bottom-most row) and define 
4 different directions(0-> from left to right, 1 -> from top to bottom, 2 -> from right to left and 3 -> from bottom to top). Each time we traverse the matrix in one 
direction, we need to shorten the pointers, i.e., once we traverse the matrix from left to right, we increment the top pointer by one, so that row is not consider anymore. 
'''
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    rows,columns = len(matrix), len(matrix[0])
    top_r = 0
    bottom_r = rows-1
    left_c = 0
    right_c = columns-1
    dirr = 0
    res=[]
    while top_r <= bottom_r and left_c <= right_c:
        if dirr==0:
            for i in range(left_c, right_c+1):
                res.append(matrix[top_r][i])
            top_r+=1
            dirr = 1
        elif dirr==1:
            for i in range(top_r, bottom_r+1):
                res.append(matrix[i][right_c])
            right_c-=1
            dirr=2
        elif dirr == 2:
            for i in range(right_c, left_c-1,-1):
                res.append(matrix[bottom_r][i])
            bottom_r-=1
            dirr=3
        elif dirr == 3:
            for i in range(bottom_r, top_r-1, -1):
                res.append(matrix[i][left_c])
            left_c+=1
            dirr = 0
    return res