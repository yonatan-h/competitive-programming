class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ > target:
                right -= 1
            elif sum_ < target:
                left += 1
            else:
                return [left+1, right+1]

#20min
#1sub
        
        
        
