class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_row = len(matrix[0])
        def fall(row_num, col_num):
            if row_num >= len(matrix):return 0
            
            left = col_num - 1
            if left < 0: left = 0
            middle = col_num
            right = col_num + 1
            if right >= len_row: right = len_row-1
            
            left_sum = fall(row_num+1, left)
            middle_sum = fall(row_num+1, middle)
            right_sum = fall(row_num+1, right)
            return matrix[row_num][col_num] + min(left_sum, middle_sum, right_sum)
 
        
        best_sum = float('inf')
        for i in range(len_row):
            best_sum = min(best_sum, fall(0, i)) 
        
        return best_sum
                
        @cache