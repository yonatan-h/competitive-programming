class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, nums: List[int]) -> int:
        nums.sort()
        nums[0] = 1
        nums.append(nums[-1])
        max_num = -float("inf")
        for i in range(len(nums)-1):
            num = nums[i]
            next_num = nums[i+1]

            if next_num > num:
                nums[i+1] = num+1
            
            max_num = max(nums[i], max_num)
        
        return max_num

    