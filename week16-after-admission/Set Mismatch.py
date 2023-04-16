class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        duplicate = None
        for i in range(len(nums)):
            while nums[i]-1 != i:
                to_i = nums[i]-1

                nums[i], nums[to_i] = nums[to_i], nums[i]
                if nums[i] == nums[to_i]:
                    duplicate = nums[i]
                    break
        
        replaced = None
        for i in range(len(nums)):
            if nums[i] == duplicate and i+1 != duplicate:
                replaced = i+1
        
        return [duplicate, replaced]
        
