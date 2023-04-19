class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbor_count = defaultdict(int)
        pair_set = set()

        for pair in roads:
            pair_set.add(tuple(sorted(pair)))
            city1, city2 = pair
            neighbor_count[city1] += 1
            neighbor_count[city2] += 1
        
        most_popular = list(neighbor_count.items())
        most_popular = [(c, n) for (n, c) in most_popular ]

        max_rank = 0
        for i in range(len(most_popular)):
            for j in range(i+1, len(most_popular)):
                c1, n1 = most_popular[i]
                c2, n2 = most_popular[j]

                rank = c1 + c2
                if tuple(sorted([n1,n2])) in pair_set:
                    rank -= 1
                if rank > max_rank: max_rank = rank
        return max_rank


        
        