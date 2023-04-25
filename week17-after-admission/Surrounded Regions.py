class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #first row
        for col in range(len(board[0])):
            expand(0, col, board)

        #last row
        for col in range(len(board[0])):
            expand(len(board)-1, col, board)

        #first col
        for row in range(len(board)):
            expand(row, 0, board)

        #last col
        for row in range(len(board)):
            expand(row, len(board[0])-1, board)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "M":
                    board[row][col] = "O"

def expand(row, col, board):
    if board[row][col] != "O": return
    board[row][col] = "M" #for marked

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if not 0 <= new_row < len(board): continue
        if not 0 <= new_col <len(board[0]): continue

        expand(new_row, new_col, board)
