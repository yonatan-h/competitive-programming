class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        used_edges = set()
        adj_list = build_adj_list(edges)
        def traverse(parent, node):
            nonlocal used_edges
        traverse(None, 0)
        return 2*len(used_edges)
    
def build_adj_list(edges):
    adj_list = defaultdict(list)
    for fro, to in edges:
            
        adj_list[fro].append(to)
    return adj_list
        
            in_apple_path = False
            
        adj_list[to].append(fro)
            for neighbor in adj_list[node]:
                if neighbor == parent: continue
                if traverse(node, neighbor):
            if hasApple[node]: in_apple_path = True
                    in_apple_path = True
                    used_edges.add((node, neighbor))
            
            return in_apple_path