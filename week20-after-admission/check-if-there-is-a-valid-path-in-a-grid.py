class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        edges = get_edges(grid)

        reps = defaultdict(lambda : None)
        for node1, node2 in edges:
            union(node1, node2, reps)

        for start_node in edges[0]:
            for end_node in edges[-1]:
                if in_same_group(start_node, end_node, reps):
                    return True
        return False   

def get_edges(grid):
    edges = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = grid[row][col]

            top_node = (row, col+0.5)
            left_node = (row+0.5, col)
            right_node = (row+0.5, col+1)
            bottom_node = (row+1, col+0.5)

            if value == 1: edge = (left_node, right_node) 
            elif value == 2: edge = (top_node, bottom_node) 
            elif value == 3: edge = (left_node, bottom_node) 
            elif value == 4: edge = (right_node, bottom_node)
            elif value == 5: edge = (left_node, top_node) 
            elif value == 6: edge = (right_node, top_node)

            edges.append(edge)
    return edges


def find_root(node, reps):
    if reps[node] == None:
        reps[node] = node

    if reps[node] == node:
        return node
    
    root = find_root(reps[node], reps)
    reps[node] = root
    return root


def union(node1, node2, reps):
    root1 = find_root(node1, reps)
    root2 = find_root(node2, reps)

    reps[root2] = root1


def in_same_group(node1, node2, reps):
    root1 = find_root(node1, reps)
    root2 = find_root(node2, reps)

    return root1 == root2



            