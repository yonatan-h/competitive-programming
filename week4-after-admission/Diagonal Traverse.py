class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_array_map = build_diagonal_arrays(mat)
        path_array = extract_path_array(diagonal_array_map)
        return path_array
        
def empty_list():
    return []

def build_diagonal_arrays(matrix):
    diagonal_array_map = defaultdict(empty_list)
    
    #build the diagonals from bottom left to top right
    for row_num in reversed(range(len(matrix))):
        for col_num in range(len(matrix[0])):
            value = matrix[row_num][col_num]
            diagonal_num = row_num + col_num
            
            diagonal_array_map[diagonal_num].append(value)
    return diagonal_array_map

def extract_path_array(diagonal_array_map):
    direction_up = True
    num_diagonals = len(diagonal_array_map)
    path_array = []
    
    for diagonal_num in range(num_diagonals):
        diagonal_array = diagonal_array_map[diagonal_num]
        
        if direction_up:
            path_array.extend(diagonal_array)
        else:
            diagonal_array.reverse()
            path_array.extend(diagonal_array)
        direction_up = not direction_up
        
    return path_array

#30min
#1sub