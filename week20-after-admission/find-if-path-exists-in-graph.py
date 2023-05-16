class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pointers = defaultdict(list)
        for edge in edges:
            [one, other] = edge
            pointers[one].append(other)
            pointers[other].append(one)
        
        return search(source, pointers, destination, set())
        
    
def search(node_val, pointers, destination, visited):
    if node_val == destination:
        return True
    elif node_val in visited:
        return

    for next_val in pointers[node_val]:
        visited.add(node_val)
        if search(next_val, pointers, destination, visited):
            return True

        
