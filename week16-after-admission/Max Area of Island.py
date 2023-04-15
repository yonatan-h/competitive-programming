class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.visited = set()
        self.grid = grid

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 0: continue
                if (row, col) in self.visited: continue
                
                self.cur_area = 0
                self.visit(row, col)
                max_area = max(max_area, self.cur_area)

        print(len(self.visited))
        return max_area



    def visit(self, row, col):
        self.visited.add((row, col))
        self.cur_area += 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            row_in_bound = 0<= new_row< len(self.grid)
            col_in_bound = 0<= new_col< len(self.grid[0])

            if not (row_in_bound and col_in_bound): continue
            if (new_row, new_col) in self.visited: continue
            if self.grid[new_row][new_col] == 0: continue
            
            self.visit(new_row, new_col)


