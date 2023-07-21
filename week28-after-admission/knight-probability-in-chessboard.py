class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        @cache
        def mark(steps_left, x, y):

            state = (steps_left, x, y)

            if not is_in_bound(x,y):
                return 0
            
            if steps_left == 0:
                steps_moved = k-steps_left
                return 1/(8**steps_moved)

            
            probability = 0
            for next_tile in get_next_tiles(x,y):
                probability += mark(steps_left-1, next_tile[0], next_tile[1])

            return probability

        
        
        def get_next_tiles(x,y):
            return [
                (x+2,y+1),
                (x+2,y-1),

                (x-2,y+1),
                (x-2,y-1),

                (x+1,y+2),
                (x-1,y+2),

                (x+1,y-2),
                (x-1,y-2),
            ]
        
        def is_in_bound(x,y):
            return 0<=x<n and 0<=y<n
        
        return mark(k, row, column)

