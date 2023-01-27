class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return is_toeplitz(matrix)
        

def is_toeplitz(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    for row_num in range(height - 1):
        for col_num in range(width - 1):
            curr_val = matrix[row_num][col_num]
            next_val = matrix[row_num+1][col_num+1]
            
            if curr_val != next_val:
                return False
    return True

#1sub
#3min