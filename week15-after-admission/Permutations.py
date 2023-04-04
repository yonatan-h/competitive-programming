class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        partial = []
        all_sols = []
        bit_set = 0
        permute(partial, bit_set, nums, all_sols)
        return all_sols



def permute(partial, bit_set, nums, all_sols):

    if len(partial) == len(nums):
        all_sols.append(partial[:])

    for i in range(len(nums)):
        shift = nums[i] + 10
        is_valid = (1<<shift & bit_set) == 0
        if is_valid:
            partial.append(nums[i])
            new_set = 1<<shift | bit_set
            permute(partial, new_set, nums, all_sols)
            partial.pop()




