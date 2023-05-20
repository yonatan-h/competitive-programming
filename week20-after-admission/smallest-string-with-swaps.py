class Solution:
    def smallestStringWithSwaps(self, string: str, pairs: List[List[int]]) -> str:
        rep_indexes = defaultdict(lambda:None)
        for i in range(len(string)):
            find(i, rep_indexes)
            
        for i1, i2 in pairs:
            union(i1, i2, rep_indexes)


        groups = defaultdict(list)
        for node_index in rep_indexes:
            rep_index = find(node_index, rep_indexes)
            letter = string[node_index]
            groups[rep_index].append(letter)
        
        for rep_index in groups:
            groups[rep_index].sort()
            groups[rep_index].reverse()

        answer = []
        for i in range(len(string)):
            rep_index = find(i, rep_indexes)
            answer.append(groups[rep_index].pop())
            

        return "".join(answer)




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

def same_group(node1, node2, reps):
    return find(node1, reps) == find(node2, reps)
