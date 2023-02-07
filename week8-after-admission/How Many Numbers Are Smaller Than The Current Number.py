class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        unique_nums = list(counts.keys())
        unique_nums.sort()
        
        cumulative_before = 0
        for num in unique_nums:
            count = counts[num] 
            
            counts[num] = cumulative_before
            cumulative_before += count
            
            
        for i in range(len(nums)):
            num = nums[i]
            nums[i] = counts[num]
        
        return nums
            
#4sub
#20min