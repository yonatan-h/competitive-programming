class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.same_label_counts = [None]*n
        self.visited = set()
        self.labels = labels
        self.adjlist = make_adjlist(edges)
        self.count_below(0)
        return self.same_label_counts
        

    def count_below( self,node):
        self.visited.add(node)

        my_count = defaultdict(int)
        my_label = self.labels[node]
        my_count[my_label] += 1

        for child in self.adjlist[node]:
            if child in self.visited: continue

            below_counts = self.count_below(child)
            add_to(my_count, below_counts)

        self.same_label_counts[node] = my_count[my_label]
        return my_count

        

def add_to(main, added):
    for key in added.keys():
        main[key] += added[key]

def make_adjlist(edges):
    adjlist = defaultdict(list)
    for node1, node2 in edges:
        adjlist[node1].append(node2)
        adjlist[node2].append(node1)
    return adjlist
