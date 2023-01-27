class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return find_largest_local(grid)
        

def find_maximum_local(row_start, col_start, grid):
    max_value = -float('inf')
    
    for row_offset in range(3):
        for col_offset in range(3):
            
            row_num = row_start + row_offset
            col_num = col_start + col_offset
            
            value = grid[row_num][col_num]
            max_value = max(max_value, value)
            
    return max_value

def find_largest_local(grid):
    max_local_matrix = []
    
    edge = len(grid)-2
    for row_num in range(edge):
        row = []
        
        for col_num in range(edge):
            max_value = find_maximum_local(row_num, col_num, grid)
            row.append(max_value)

        max_local_matrix.append(row)
        
    return max_local_matrix
        
            
        
#2sub
#30min