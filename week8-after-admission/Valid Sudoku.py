class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return is_valid_sudoku(board)
        
        
def is_valid_sudoku(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    
    for row_num in range(height):
        if not is_valid_row(row_num, matrix):
            return False
        
    for col_num in range(width):
        if not is_valid_col(col_num, matrix):
            return False
    
    for row_num in [0,3,6]:
        for col_num in [0, 3, 6]:
            if not is_valid_3x3(row_num, col_num, matrix):
                return False
    
    return True
        
        
def is_valid_row(row_num, matrix):
    width = len(matrix[0])          
    nums = []
    for col_num in range(width):
        value = matrix[row_num][col_num]
        if value != ".": nums.append(value)
    
    return len(nums) == len(set(nums))
                
def is_valid_col(col_num, matrix):
    height = len(matrix)        
    nums = []
    for row_num in range(height):
        value = matrix[row_num][col_num]
        if value != ".": nums.append(value)
    
    return len(nums) == len(set(nums))


def is_valid_3x3(top_row_num, left_col_num, matrix):
    nums = []
    for row_num in range(top_row_num, top_row_num+3):
        for col_num in range(left_col_num, left_col_num+3):
            value = matrix[row_num][col_num]
            if value != ".": nums.append(value)
    
    return len(nums) == len(set(nums))
    
            
#20min
#1sub
        
    
    

        
        