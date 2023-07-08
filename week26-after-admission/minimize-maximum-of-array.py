class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        peak = 0
        total = 0

        for i in range(len(nums)):
            num = nums[i]
            total += num
            average = total/(i+1)
            peak = max(peak, math.ceil(average))
        
        return peak

