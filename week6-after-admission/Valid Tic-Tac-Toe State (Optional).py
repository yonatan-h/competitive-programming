class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        return is_valid_state(board)
        
        


def is_valid_state(board):
    num_Xs, num_Os = count_x_and_o(board)
    x_has_won = has_won(board, "X")
    o_has_won = has_won(board, "O")


    if x_has_won or o_has_won:
        if x_has_won and o_has_won:
            return False

        if x_has_won and num_Xs != num_Os +1:
            return False

        if o_has_won and num_Xs != num_Os:
            return False

    else:
        if num_Os > num_Xs:
            return False
        
        if num_Xs - num_Os > 1:
            return False
        
    return True


        
        
        

def count_x_and_o(board):
    num_Xs = 0
    num_Os = 0
    
    for row in board:
        for cell in row:
            
            if cell == "X":
                num_Xs += 1
            elif cell == "O":
                num_Os += 1
                
    return (num_Xs, num_Os)

def has_won(board, player):
    #row0
    if board[0][0] == board[0][1] == board[0][2] == player: return True
    
    #row1
    if board[1][0] == board[1][1] == board[1][2] == player: return True

    #row2
    if board[2][0] == board[2][1] == board[2][2] == player: return True
    

    #col0
    if board[0][0] == board[1][0] == board[2][0] == player: return True

    #col1
    if board[0][1] == board[1][1] == board[2][1] == player: return True  

    #col2
    if board[0][2] == board[1][2] == board[2][2] == player: return True 


    #diag1
    if board[0][0] == board[1][1] == board[2][2] == player: return True

    #diag2
    if board[2][0] == board[1][1] == board[0][2] == player: return True

        
        

def count_x_and_o(board):
    num_Xs = 0
    num_Os = 0
    
    for row in board:
        for cell in row:
            
            if cell == "X":
                num_Xs += 1
            elif cell == "O":
                num_Os += 1
                
    return (num_Xs, num_Os)

def has_won(board, player):
    #row0
    if board[0][0] == board[0][1] == board[0][2] == player: return True
    
    #row1
    if board[1][0] == board[1][1] == board[1][2] == player: return True

    #row2
    if board[2][0] == board[2][1] == board[2][2] == player: return True
    

    #col0
    if board[0][0] == board[1][0] == board[2][0] == player: return True

    #col1
    if board[0][1] == board[1][1] == board[2][1] == player: return True  

    #col2
    if board[0][2] == board[1][2] == board[2][2] == player: return True 


    #diag1
    if board[0][0] == board[1][1] == board[2][2] == player: return True

    #diag2
    if board[2][0] == board[1][1] == board[0][2] == player: return True


#6sub
#40min