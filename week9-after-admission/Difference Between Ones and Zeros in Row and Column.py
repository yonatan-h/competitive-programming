class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        [row_counts, col_counts] = count(grid)
        get_diff(grid, row_counts, col_counts)
        return grid
        
        
def count(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    row_counts = [ [0,0] for _ in range(height)]
    col_counts = [[0,0] for _ in range(width)]
    
    
    for row_num in range(len(matrix)):
        for col_num in range(len(matrix[0])):
            
            value = matrix[row_num][col_num]
            if value == 0 or value == 1: 
                row_counts[row_num][value] += 1
                col_counts[col_num][value] += 1
            
    return [row_counts, col_counts]

def get_diff(matrix, row_counts, col_counts):
    for row_num in range(len(matrix)):
        for col_num in range(len(matrix[0])):
            
            ones_row = row_counts[row_num][1]
            ones_col = col_counts[col_num][1]
            zeros_row = row_counts[row_num][0]
            zeros_col = col_counts[col_num][0]
            
            diff = ones_row + ones_col - zeros_row - zeros_col
            matrix[row_num][col_num] = diff
    
        
#1sub
#20min