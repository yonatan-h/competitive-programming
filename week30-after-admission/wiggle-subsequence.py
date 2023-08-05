class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def longest_wiggle(index, go_up):
            best_child = 0
            for i in range(index+1, len(nums)):
                best_child = max(best_child, longest_wiggle(i, not go_up))
                if go_up and nums[i] <= nums[index]:
                    continue
                if not go_up and nums[i] >= nums[index]:
                    continue
            
            return best_child + 1
        
        return max(longest_wiggle(0, True), longest_wiggle(0, False))
        @cache