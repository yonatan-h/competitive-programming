class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        self.grid1 = grid1
        self.grid2 = grid2

        num_sub_islands = 0

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if self.grid2[row][col] != 1: continue

                self.is_subset = True
                self.visit(row, col)

                if self.grid2[row][col] == 2:
                    num_sub_islands += 1

        return num_sub_islands



    def visit(self, row, col):
        if not (1 == self.grid2[row][col] == self.grid1[row][col]):
            self.is_subset = False

        self.grid2[row][col] = +2

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            row_in_bound = 0<= new_row< len(self.grid2)
            col_in_bound = 0<= new_col< len(self.grid2[0])

            if not (row_in_bound and col_in_bound): continue
            if self.grid2[new_row][new_col] != 1: continue

            
            self.visit(new_row, new_col)
        
        if not self.is_subset:
            self.grid2[row][col] = -2
        


