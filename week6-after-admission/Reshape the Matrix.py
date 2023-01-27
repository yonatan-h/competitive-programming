 


def get_row_col(index, width):
    row_num = index//width
    col_num = index%width
    return (row_num, col_num)
    
def make_empty_matrix(width, height):
    matrix = []
    
    for row_num in range(height):
        matrix.append([None]*width)
        
    return matrix

def reshape(original_matrix, height, width):
    original_width = len(original_matrix[0])
    original_height = len(original_matrix)

    if original_height * original_width != width * height:
        return original_matrix

    new_matrix = make_empty_matrix(width, height)
    
    
    
    total_cells = width*height
    for cell_index in range(total_cells):
            from_row, from_col = get_row_col(cell_index, original_width)
            to_row, to_col = get_row_col(cell_index, width)

            value = original_matrix[from_row][from_col]
            new_matrix[to_row][to_col] = value
            
    return new_matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return reshape(mat, r, c)
        
 


def get_row_col(index, width):
    row_num = index//width
    col_num = index%width
    return (row_num, col_num)
    
def make_empty_matrix(width, height):
    matrix = []
    
    for row_num in range(height):
        matrix.append([None]*width)
        
    return matrix

def reshape(original_matrix, height, width):
    original_width = len(original_matrix[0])
    original_height = len(original_matrix)

    if original_height * original_width != width * height:
        return original_matrix

    new_matrix = make_empty_matrix(width, height)
    
    
    
    total_cells = width*height
    for cell_index in range(total_cells):
            from_row, from_col = get_row_col(cell_index, original_width)
            to_row, to_col = get_row_col(cell_index, width)

            value = original_matrix[from_row][from_col]
            new_matrix[to_row][to_col] = value
            
    return new_matrix

#3sub
#15min