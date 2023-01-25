class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        return get_attacker_positions(king, queens)


        
def get_all_directions():
    up = (-1, 0)
    right = (0,1)
    down = (1, 0)
    left = (0,-1)
    
    up_left = (-1,-1)
    up_right = (-1, 1)
    down_right = (1,1)
    down_left = (1,-1)
    
    return [up, right, down, left, up_left, up_right, down_right, down_left]


def is_in_direction(king_position, queen_position, direction):
    kx, ky = king_position
    qx, qy = queen_position
    dir_x, dir_y = direction
    
    change_x = kx - qx
    change_y = ky - qy

    #a + bi * c - di = ac + bd + (-ad+bc)i
    dot_product = change_x*dir_x + change_y*dir_y
    cross_product = change_x*dir_y - change_y*dir_x

    are_parallel = cross_product  == 0
    are_same_direction = dot_product > 0
    
    return are_parallel and are_same_direction

    

def get_distance(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    
    distance = abs(x1-x2) + abs(y1-y2)
    return distance
   
    
def get_attacker_positions(king_position, queen_positions):
    directions = get_all_directions()
    attacker_positions = []
    
    for direction in directions:
        
        nearest_queen_position = None
        nearest_distance = float('inf')
        
        for queen_position in queen_positions:
            print(queen_position)
            if not is_in_direction(king_position, queen_position, direction):
                continue
            distance = get_distance(king_position, queen_position)

            if distance < nearest_distance:
                nearest_queen_position = queen_position
                nearest_distance = distance
                
        if nearest_distance < float('inf'):
            attacker_positions.append(nearest_queen_position)
    
    return attacker_positions
            
     
            
#2sub
#60min