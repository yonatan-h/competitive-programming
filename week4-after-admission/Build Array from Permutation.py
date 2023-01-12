class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        permuted_array = [None]*len(nums)
        for num in nums:
            permuted_array[num] = nums[nums[num]]
        return permuted_array

#1sum
#1min