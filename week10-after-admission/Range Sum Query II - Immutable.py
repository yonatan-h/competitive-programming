class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rect_sum = build_rect_sum(matrix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.rect_sum[row2+1][col2+1]
        top_left = self.rect_sum[row1][col1]
        top_right = self.rect_sum[row1][col2+1]
        bottom_left = self.rect_sum[row2+1][col1]
        
        return bottom_right - top_right - bottom_left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def build_rect_sum(matrix):
    rect_sum = []
    for _ in range(len(matrix)+1):
        row = [0]*(len(matrix[0])+1)
        rect_sum.append(row)
    print(rect_sum)
    for row_num in range(len(matrix)):
        for col_num in range(len(matrix[0])):
            row_num_rect = row_num + 1
            col_num_rect = col_num + 1
            
            value = matrix[row_num][col_num]
            top_sum = rect_sum[row_num_rect-1][col_num_rect]
            left_sum = rect_sum[row_num_rect][col_num_rect-1]
            top_left_sum = rect_sum[row_num_rect-1][col_num_rect-1]
            
            rect_sum[row_num_rect][col_num_rect] = value + top_sum + left_sum - top_left_sum
    
    return rect_sum

#20min
#1sub
            