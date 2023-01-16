class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return binary_matrix_search(target, matrix)

def get_value(index, matrix):
    row_size = len(matrix[0])
    
    row_num = index//row_size
    col_num = index % row_size
    
    value = matrix[row_num][col_num]
    return value
    

def binary_matrix_search(target, matrix):
    left = 0
    num_cells = len(matrix)*len(matrix[0])
    right = num_cells-1
    
    while left <= right:
        middle = (left + right)//2
        middle_num = get_value(middle, matrix)
        
        if target == middle_num:
            return True
        elif target < middle_num:
            right = middle-1
        else:
            left = middle+1
    return False

#30min
#3sub