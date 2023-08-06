            return root
        
        def union(point1, point2):
            root1 = find_root(point1)
            root2 = find_root(point2)
            parents[root2] = root1
            if row in row_leaders:
                union(stone, row_leaders[row])
            if col in col_leaders:
                union(stone, col_leaders[col])
        
        roots = set()
        
        for stone in stones:
            parents[stone] = stone
            stone = (row, col)
            row, col = stone
        for stone in stones:
            stone = tuple(stone)
            row_leaders[row] = stone
            col_leaders[col] = stone
        for stone in stones:
            row, col = stone
            stone = tuple(stone)
            roots.add(find_root(stone))
        
        return len(stones) - len(roots)
        
        
            parents[point] = root
            
            root= find_root(parent)
                return parent
            if parent == point:
            parent = parents[point]
        def find_root(point):
        col_leaders = {}
        row_leaders = {}
          