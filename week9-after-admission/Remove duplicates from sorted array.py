class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        for seeker in range(len(nums)):
            if nums[holder] != nums[seeker]:
                holder += 1
                nums[holder] = nums[seeker]
                
        unique_length = holder+1
        return unique_length