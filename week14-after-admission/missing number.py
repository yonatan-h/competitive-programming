class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= i+1
            xor ^= nums[i]
        return xor
            

#1sub
#5min