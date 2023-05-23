class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = get_all_edges(points)
        sort_edges(edges)
        min_cost = connect_sorted(len(points), edges)
        return min_cost


def get_all_edges(points):
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = abs(x1-x2) + abs(y1-y2)
            edges.append((distance, tuple(points[i]), tuple(points[j])))
    return edges

def sort_edges(edges):
    edges.sort()
    edges.reverse()

def connect_sorted(num_points, sorted_edges):
    reps = defaultdict(lambda:None)
    num_connections = 0
    min_cost = 0
    while num_connections != num_points-1:
        distance, point1, point2 = sorted_edges.pop()
        if union(point1, point2, reps):
            num_connections += 1
            min_cost += distance

    return min_cost
    


def union(node1, node2, reps):
    rep1 = find(node1, reps)
    rep2 = find(node2, reps)

    new_connection = rep1 != rep2
    if new_connection:
        reps[rep2] = rep1
        return True
    else:
        return False 

    

def find(node, reps):
    if reps[node] == None:
        reps[node] = node
    if reps[node] == node:
        return node
    
    root = find(reps[node], reps)
    reps[root] = root
    return root
