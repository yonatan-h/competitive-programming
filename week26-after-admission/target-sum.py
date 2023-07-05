class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        level_sums = defaultdict(int) 
        level_sums[0] = 1

        for num in nums:
            new_level_sums = defaultdict(int)

            for sign in (+1,-1):
                for level_sum in level_sums.keys():
                    new_level_sum = sign*num + level_sum
                    frequency = level_sums[level_sum]
                    new_level_sums[new_level_sum] += frequency 

            level_sums  = new_level_sums
            
        return level_sums[target]