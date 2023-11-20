class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = defaultdict(int)
        for birth, death in logs:
            changes[birth] += 1
            changes[death] -= 1
        
        times = list(changes.keys())
        times.sort()

        best_popn = 0
        best_year = 0

        cur_popn = 0
        for time in times:
            change = changes[time]
            cur_popn += change
            if cur_popn > best_popn:
                best_popn = cur_popn
                best_year = time
        
        return best_year
        