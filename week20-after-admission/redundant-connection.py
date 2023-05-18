class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        reps = defaultdict(lambda : None)

    
        loop_edge = None

        for node1, node2 in edges:
            reps[node1] = reps[node1] or node1
            reps[node2] = reps[node2] or node2

            rep1 = find_rep(node1, reps)
            rep2 = find_rep(node2, reps)
            if rep1 == rep2:
                loop_edge = [node1, node2]

            join_trees(node1, node2, reps)
        
        return loop_edge

def find_rep(node, reps):
    child = node
    parent = reps[child]

    while child != parent:
        child = parent
        parent = reps[parent]
    
    return parent

def join_trees(node1, node2, reps):
    rep1 = find_rep(node1, reps)
    rep2 = find_rep(node2, reps)

    reps[rep2] = rep1

    