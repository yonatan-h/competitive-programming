class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        
        current_max = -1
        
        for i in reversed(range(len(nums))):
            num = nums[i]
            nums[i] = current_max
            
            current_max = max(current_max, num)
            
        return nums

#1sub
#5min