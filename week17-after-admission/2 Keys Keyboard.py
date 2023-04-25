class Solution:
    def minSteps(self, num: int) -> int:
        if num == 1: return 0
        
        min_cost = float("inf")#Copy then paste pasting 1 num times
        for factor1, factor2 in get_factor_pairs(num):
            if factor1 == 1: continue #you never paste 0 times

            #pastesXfactor1-1 + copy the factor2 + costFactor2
            cost = (factor1-1) + 1 + self.minSteps(factor2)
            min_cost = min(min_cost, cost)

        return min_cost


def get_factor_pairs(num):
    pairs = []
    for factor in range(1, int(num**0.5)+1):
        if num%factor == 0:
            pairs.append((factor, num//factor))
            pairs.append((num//factor, factor))
    return pairs