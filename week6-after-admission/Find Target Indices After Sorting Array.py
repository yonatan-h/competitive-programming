class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        indexes = []
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                indexes.append(i)
        return indexes
    
#10min
#1sub