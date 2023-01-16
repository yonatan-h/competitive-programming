class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        apply_twice_zeroing(nums)
        shift_zeros_away(nums)
        return nums
        
def apply_twice_zeroing(nums):
    for i in range(len(nums)-1):
        
        if nums[i] == nums[i+1]:
            nums[i]*= 2
            nums[i+1] = 0

def shift_zeros_away(nums):
    left = None
    
    for right in range(len(nums)):
        #on first encounter with zero, initialize left
        if left == None:
            if nums[right] == 0: left = right
            continue
        
        if nums[right] != 0:
            nums[left], nums[right] =  nums[right], nums[left]
            left += 1

#30min
#3sub