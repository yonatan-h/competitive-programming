class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return get_spiral_array(matrix)
        
def get_spiral_array(matrix):
    row_length = len(matrix[0])
    col_length = len(matrix)
    num_cells = row_length * col_length
    
    right = (0,1)
    down = (1,0)
    left = (0,-1)
    up = (-1, 0)
    
    directions = [right, down, left, up]
    
    untouched_row_length = row_length 
    untouched_col_length = col_length 
    
    position = [0,0]
    direction_index = 0 #right
    touched_cells = [] #empty at first
    
    turning_step = untouched_row_length
    
    
    while len(touched_cells) < num_cells:
        touched_cells.append(matrix[position[0]][position[1]])
        
        should_turn = len(touched_cells) == turning_step
        was_travelling_row = direction_index == 0 or direction_index == 2
        
        if should_turn:
            
            
            if was_travelling_row:
                untouched_col_length -= 1
                turning_step += untouched_col_length
            else:
                untouched_row_length -= 1
                turning_step += untouched_row_length
                        
            
            
            direction_index = (direction_index + 1)%len(directions)
            

        direction = directions[direction_index]
        position[0] += direction[0]
        position[1] += direction[1]
    
    return touched_cells

#60min
#1sub
        
        
        