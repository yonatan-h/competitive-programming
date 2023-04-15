class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        row, col = click
        value = board[row][col]

        if value == "E":
            reveal_empty(board, row, col)
        elif value == "M":
            reveal_bomb(board, row, col)
        
        return board

def get_directions():
    directions = [
        (0,1), (0,-1), (1,0), (-1,0),
        (1,1), (-1,1), (-1,-1), (1,-1)
        ]
    return directions

def in_bound(board, row, col):
    row_in_bound = 0 <= row < len(board)
    col_in_bound =  0 <= col < len(board[0])
    return row_in_bound and col_in_bound

def surrounding_bombs(board, row, col):
    bomb_count = 0
    for direction in get_directions():
        new_row = row + direction[0]
        new_col = col + direction[1]
        if not in_bound(board, new_row, new_col):
            continue
        if board[new_row][new_col] == "M":
            bomb_count += 1

    return bomb_count


def reveal_empty(board, start_row, start_col):
    
    def recursive_reveal(row, col):
        bomb_count = surrounding_bombs(board, row, col)
        if bomb_count > 0:
            board[row][col] = str(bomb_count)
            return 

        board[row][col] = "B"

        for direction in get_directions():
            new_row = row + direction[0]
            new_col = col + direction[1]

            if not in_bound(board, new_row, new_col):
                continue

            is_visited = (new_row, new_col) in visited
            if is_visited: continue

            is_empty = board[new_row][new_col] == "E"
            if not is_empty: continue

            recursive_reveal(new_row, new_col)
    
    visited = set()
    recursive_reveal(start_row, start_col)


def reveal_bomb(board, row, col):
    board[row][col] = "X"
    

