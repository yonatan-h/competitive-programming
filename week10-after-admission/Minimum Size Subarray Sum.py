class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum - nums[left] >= target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum >= target:
                length = right - left + 1
                min_length = min(min_length, length)
        
        if min_length == float("inf"):
            return 0
        else:        
            return min_length
            
            
#25min
#1sub