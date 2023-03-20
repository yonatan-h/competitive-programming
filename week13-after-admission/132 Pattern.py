
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return is_132(nums)
 
def is_132(nums):
    min_before = nums[0]
    stack = [] #decreasing, (num, prev_min) pair
    for i in range(1, len(nums)):
        num = nums[i]

        while stack and num > stack[-1][0]:
            stack.pop()

        if stack:
            (prev_num, prev_prev_min) = stack[-1]
            if prev_num > num and prev_prev_min < num:
                    return True

        stack.append((num, min_before))
        min_before = min(min_before, num)
    
    return False


