class Solution:
    def minCostClimbingStairs(self, ind_costs: List[int]) -> int:
        ind_costs.append(0)
        costs = ind_costs[:]

        
        for i in range(len(costs)-2):
            cur = costs[i]  
            nex = costs[i+1]
            costs[i+2] = min(cur, nex) + ind_costs[i+2]
        
        return min(costs[-2], costs[-1])
        


