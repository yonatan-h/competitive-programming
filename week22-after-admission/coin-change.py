class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        steps = defaultdict(lambda: float("inf"))
        def solve(remaining_amount):
            if remaining_amount == 0:
                steps[0] = 0
                return
            elif remaining_amount < 0:
                steps[remaining_amount] = float("inf")
                return
                

            for coin in coins:
                if remaining_amount-coin not in steps:
                    solve(remaining_amount-coin)
                
                old_steps = steps[remaining_amount]
                new_steps = 1 + steps[remaining_amount - coin]
                steps[remaining_amount] = min(old_steps, new_steps)

        solve(amount)
        if steps[amount] != float("inf"):
            return steps[amount]
        else:
            return -1

