class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        for i in range(len(nums)+1):

            if i not in nums_set:
                return i

#1sub
#5min