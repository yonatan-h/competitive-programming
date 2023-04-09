class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        flood(sr, sc, image[sr][sc], color, set(), image)
        return image


def in_bound(row, col, image):
    row_in_bound = 0 <= row < len(image)
    col_in_bound = 0 <= col < len(image[0])
    return row_in_bound and col_in_bound

def flood(row, col, color, to_color, visited, image):
    visited.add((row, col))

    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if not in_bound(new_row, new_col, image):
            continue
        
        if image[new_row][new_col] != color:
            continue

        if (new_row, new_col) in visited:
            continue
        
        flood(new_row, new_col, color, to_color, visited, image)
    
    image[row][col] = to_color
        


