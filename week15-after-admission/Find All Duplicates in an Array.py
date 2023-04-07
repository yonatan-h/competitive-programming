class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()

        for i in range(len(nums)):
            while i != nums[i]-1:
                swapee = nums[i]-1
                if nums[i] == nums[swapee]:
                    duplicates.add(nums[i])
                    break
                else:
                    nums[i], nums[swapee] = nums[swapee], nums[i]
        
        return list(duplicates)
