class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        num_subsets = 0
        target = 0
        for num in nums:
            target = target | num

        def count(index, cumulative):
            nonlocal num_subsets
            if cumulative == target:
                num_subsets += 1
 
            for i in range(index+1, len(nums)):
                new_cumulative = nums[i] | cumulative
                count(i, new_cumulative)
        count(-1, 0)
        return num_subsets