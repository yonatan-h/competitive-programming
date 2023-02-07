class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        return count_magic_squares(grid)
          
def count_magic_squares(matrix):
    width = len(matrix[0])
    height = len(matrix)
    
    if width < 3 or height < 3:
        return 0
    
    magic_sqare_count = 0
    for row_num in range(height-2):
        for col_num in range(width-2):
            
            if is_magic_square(row_num, col_num, matrix):
                magic_sqare_count += 1
                
    return magic_sqare_count
                
            
def are_between_1_and_9(nums):
    for num in nums:
        if not 1 <= num <= 9:
            return False
    return True
        
def are_n_distinct_numbers(nums, n):
    are_distinct_numbers = len(set(nums)) == n
    return are_distinct_numbers
    
    
def is_magic_square(top_row_num, left_col_num, matrix):

    #renamed just to shorten them
    row = top_row_num 
    col = left_col_num
    
    tl = matrix[row][col] #topleft
    t = matrix[row][col+1] #top
    tr = matrix[row][col+2] #topright

    
    l = matrix[row+1][col] #left
    m = matrix[row+1][col+1] #middle
    r = matrix[row+1][col+2] #right

    
    bl = matrix[row+2][col] #bottom left
    b = matrix[row+2][col+1] #bottom
    br = matrix[row+2][col+2] #bottomright
    
    
    nums = [tl,t,tr, l,m,r, bl,b,br]
    
    if not are_n_distinct_numbers(nums, 9):
        return False
    
    if not are_between_1_and_9(nums):
        return False
    
    row1_sum = tl+t+tr
    are_magic_rows = row1_sum == l+m+r == bl+b+br
    are_magic_cols = tl+l+bl == t+m+b == tr+r+br == row1_sum
    are_magic_diagonals = tl+m+br == bl+m+tr == row1_sum
    
    return are_magic_rows and are_magic_cols and are_magic_diagonals
    
#4sub
#45min  