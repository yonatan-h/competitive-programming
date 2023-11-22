class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_before = float('inf')
        best_profit = -float('inf')

        for price in prices:
            profit = price-smallest_before
            best_profit = max(best_profit, profit)
            smallest_before = min(smallest_before, price)

        return max(0,best_profit)
    