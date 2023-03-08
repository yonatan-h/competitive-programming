class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)
        


def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    middle = None
    
    while left <= right:
        middle = (left + right)//2
        at_middle = nums[middle]
        
        if at_middle == target:
            return middle
        elif at_middle > target:
            right = middle -1
        else:
            left = middle + 1
            
    if target > nums[middle]: return middle+1
    else: return middle

#3sub
#10min