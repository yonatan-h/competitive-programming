class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        break_index_to_right = get_break_to_right(nums)
        break_index_to_left = get_break_to_left(nums)
        
        return break_index_to_right == break_index_to_left
        
        
def get_break_to_right(nums):
    
    for i in range(len(nums)-1):
        current_num = nums[i]
        next_num = nums[i+1]
        
        if current_num >= next_num:
            return i
    return float('inf')

def get_break_to_left(nums):
    
    for i in reversed(range(1, len(nums))):
        current_num = nums[i]
        previous_num = nums[i-1]
        
        if previous_num <= current_num:
            return i
    return -float('inf')
    
    
    
#1sub
#10min