class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        nums = [-2] + nums + [-1]
        stack = []
        min_sums = 0

        for i in range(len(nums)):
            while stack and  nums[i] < nums[stack[-1]]:
                popped_index = stack.pop()

                with_right = i - popped_index
                with_left = popped_index - stack[-1]
                
                num_subarrays = with_right * with_left
                min_sums += nums[popped_index] * num_subarrays

            stack.append(i)

        return (min_sums) % ((10 **9) + 7)

                
 #40min
#5sub
