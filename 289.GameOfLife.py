'''
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:
    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. 
In this process, births and deaths occur simultaneously. Given the current state of the board, update the board to reflect its next state.

Example 1: 
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        +---+---+---+           +---+---+---+
        | 0 | 1 | 0 |           | 0 | 0 | 0 |
        +---+---+---+           +---+---+---+
        | 0 | 0 | 1 |           | 1 | 0 | 1 |
        +---+---+---+     =>    +---+---+---+
        | 1 | 1 | 1 |           | 0 | 1 | 1 |
        +---+---+---+           +---+---+---+
        | 0 | 0 | 0 |           | 0 | 1 | 0 |
        +---+---+---+           +---+---+---+
Example 2:
    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]
        +---+---+           +---+---+
        | 1 | 1 |           | 1 | 1 |
        +---+---+     =>    +---+---+
        | 1 | 0 |           | 1 | 1 |
        +---+---+           +---+---+
Solution: We can avoid the extra-space modifying the matrix. So, we can build a code, like a truth table, to keep track of what the original value was and what it became.
For example:
    --------------------
    |Starts Ends  Value|
    |  0     0      0  |
    |  1     0      1  |
    |  0     1      2  |
    |  1     1      3  |
    -------------------- 
This way, we know if a cell was alive or dead at the moment of determine whether another cell would be alive or not.  '''
'''def gameOfLife(board: list[list[int]]) -> None: #T: O(n*m) & S: O(n*m)
    rows, columns = len(board), len(board[0])
    deads, lives = [],[]
    LIVE = 1
    DEAD = 0
    def checkNeighbors(r: int, c:int):
        l_count = 0
        isLive = False
        if board[r][c] == LIVE:
             isLive = True
        for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
            row, col = r+r_off, c+c_off
            if 0<=row<rows and 0<=col<columns and board[row][col]: #if is a valid position
                    l_count += 1
        if l_count < 2 and isLive:
            deads.append((r,c))
        elif l_count>3 and isLive:
            deads.append((r,c))
        elif l_count==3 and not isLive:
                lives.append((r,c))
    for r in range(rows):
        for c in range(columns):
            checkNeighbors(r,c)
    for dead in deads:
        r,c = dead
        board[r][c] = DEAD
    for live in lives:
        r,c = live
        board[r][c] = LIVE
    print(board)'''
def gameOfLife(board: list[list[int]]) -> None: #T: O(n*m) S: O(1) 
    rows, columns = len(board), len(board[0])
    def checkNeighbors(r: int, c:int):
        l_count = 0
        for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
            row, col = r+r_off, c+c_off
            if 0<=row<rows and 0<=col<columns and board[row][col] in [1,3 ]: #if is a valid position
                    l_count += 1
        if board[r][c]:
            if l_count in [2,3]:
                board[r][c] = 3
        elif l_count==3:
            board[r][c] = 2
    for r in range(rows):
        for c in range (columns):
            checkNeighbors(r,c)
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2,3]:
                board[r][c] = 1
    
                
    