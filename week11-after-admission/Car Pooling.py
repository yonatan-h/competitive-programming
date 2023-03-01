class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = defaultdict(int)
        for trip in trips:
            [ppl, start, dest ] = trip
            changes[start] += ppl
            changes[dest] -= ppl

        positions = list(changes.keys())
        positions.sort()

        running_ppl = 0
        for position in positions:
            running_ppl += changes[position]
            if running_ppl > capacity:
                return False

        return True 
    
#25min
#1sub