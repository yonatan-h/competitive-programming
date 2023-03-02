class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater_elements = [-1]*len(nums)

        stack = []
        i = 0

        for i in range(len(nums)*2):
            rotating_i = i%len(nums)
            cur_num = nums[rotating_i]

            while stack and cur_num > nums[stack[-1]]:
                lesser_index = stack.pop()
                next_greater_elements[lesser_index] = cur_num
            stack.append(rotating_i)
        
        return next_greater_elements
            

#15min
#1sub

