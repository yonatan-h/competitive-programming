class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotate_matrix(matrix)
        
import math

def rotate_position(position, width, height):
    row_num, col_num = position[0], position[1]
    height -= 1
    width -= 1
    
    x = col_num - width/2
    y = height/2 - row_num
    
    rotated_x = y
    rotated_y = -x
    
    new_col_num = width/2 + rotated_x
    new_row_num = height/2 - rotated_y

    new_position = (int(new_row_num), int(new_col_num))
    
    return new_position

def domino_hop_rotate(starting_position, matrix):
    width = len(matrix[0])
    height = len(matrix[0])

    pos1 = starting_position
    pos2 = rotate_position(pos1, width, height)
    pos3 = rotate_position(pos2, width, height)
    pos4 = rotate_position(pos3, width, height)
    
    val1 = matrix[pos1[0]][pos1[1]]
    val2 = matrix[pos2[0]][pos2[1]]
    val3 = matrix[pos3[0]][pos3[1]]
    val4 = matrix[pos4[0]][pos4[1]]
    
    matrix[pos2[0]][pos2[1]] = val1
    matrix[pos3[0]][pos3[1]] = val2
    matrix[pos4[0]][pos4[1]] = val3
    matrix[pos1[0]][pos1[1]] = val4
    
    
def rotate_matrix(matrix):
    unique_quarter_width = len(matrix[0])//2
    unique_quarter_height = math.ceil(len(matrix)/2)
    
    for row_num in range(unique_quarter_height):
        for col_num in range(unique_quarter_width):
            position = (row_num, col_num)
            domino_hop_rotate(position, matrix)
    return matrix

#1sub
#30min