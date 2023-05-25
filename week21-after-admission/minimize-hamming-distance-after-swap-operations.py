class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        reps = defaultdict(lambda: None)
        for index1, index2  in allowedSwaps:
            union(index1, index2, reps)
        
        frequencies = count_frequencies(source, reps)

        difference_count = 0
        for i in range(len(source)):
            num1 = source[i]
            num2 = target[i]


            rep_i = find(i, reps)
            if frequencies[rep_i][num2] > 0:
                frequencies[rep_i][num2] -= 1
            else:
                difference_count += 1
                
        
        return difference_count

        
        

 

def count_frequencies(source, reps):
    counts = defaultdict(lambda : defaultdict(int)) #values are Counters
    for i in range(len(source)):
        num = source[i]
        rep_i = find(i, reps)
        counts[rep_i][num] += 1
    return counts

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
    if root1 == root2: return
    reps[root2] = root1