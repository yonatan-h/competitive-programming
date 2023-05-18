class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        reps = list(range(n))

        for node1, node2 in edges:
            join_trees(node1, node2, reps)
        
        return find_rep(source, reps) == find_rep(destination, reps)


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

    


