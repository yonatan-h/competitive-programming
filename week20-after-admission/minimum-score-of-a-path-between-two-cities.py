class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        reps = defaultdict(lambda: None)

        for city1, city2, distance in roads:
            union(city1, city2, reps)
        
        min_distance = float("inf")
        for city1, city2, distance in roads:
            if find(city1, reps) == find(city2, reps) == find(1, reps):
                min_distance = min(min_distance, distance)

        return min_distance



def find(node, reps):
    if reps[node] == None:
        reps[node] = node
    if node == reps[node]:
        return node
    
    root = find(reps[node], reps)
    reps[node] = root
    return root

def union(node1, node2, reps):
    root1 = find(node1, reps)
    root2 = find(node2, reps)

    reps[root2] = root1

