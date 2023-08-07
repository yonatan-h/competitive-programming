class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def traverse(target):
            if target == 0:
            for num in nums:
            counts = 0
                counts += traverse(target-num)
            
        @cache
            return counts
        
                return 1
            if target < 0:
                return 0
        return traverse(target)