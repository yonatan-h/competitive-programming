class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        max_seconds = max(tickets)
        total_seconds = 0

        for _ in range(max_seconds):
            for i in range(len(tickets)):
                if tickets[i]:
                    total_seconds += 1
                    tickets[i] -= 1

                if tickets[k] == 0:
                    return total_seconds

#20min
#4sub