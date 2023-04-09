class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = None
        for num in nums:
            if nums[abs(num)-1] < 0:
                duplicate = abs(num)
                break
            else:
                nums[abs(num)-1] *= -1
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        
        return duplicate



        
        
