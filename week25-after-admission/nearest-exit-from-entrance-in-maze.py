class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.maze = maze
        self.entrance = tuple(entrance)
        return self.dis_nearest_exit()


    def dis_nearest_exit(self):
        que = deque([self.entrance])
        self.visited = {self.entrance}

        level = 0
        while que:
            for _ in range(len(que)):
                pos = que.popleft()
                if self.is_exit(pos):
                    return level
                
                for neighbor in self.get_neighbors(pos):
                    self.visited.add(neighbor)
                    que.append(neighbor)
            level += 1
        return -1
 
    def get_neighbors(self, pos):
        row, col = pos
        maze_height = len(self.maze)
        maze_width = len(self.maze[0])


        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        neighbors = []
        for dir_row, dir_col in directions:
            new_row = row + dir_row
            new_col = col + dir_col
            new_pos = (new_row, new_col)

            if not 0<=new_row<maze_height: continue
            if not 0<=new_col<maze_width: continue
            if self.maze[new_row][new_col] == "+": continue
            if new_pos in self.visited: continue

            neighbors.append(new_pos)

        return neighbors

    def is_exit(self, pos):
        row, col = pos
        maze_height = len(self.maze)
        maze_width = len(self.maze[0])

        if pos == self.entrance: return False
        elif row==0 or row==maze_height-1: return True
        elif col==0 or col==maze_width-1: return True
        else: return False

            
