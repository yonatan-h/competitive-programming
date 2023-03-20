class Solution:
    def shortestSubarray(self, nums: List[int], target: int) -> int:
        return find_shortest(nums, target)
from collections import deque



def find_shortest(nums, target):
    prefix = build_prefix(nums)
    window = deque()
    min_length = float("inf")

    for i in range(len(prefix)):

        def is_increasing():
            right_index = window[-1]
            right_prefix = prefix[right_index]
            cur_prefix = prefix[i]
            return cur_prefix > right_prefix

        while window and not is_increasing():
            window.pop()


        window.append(i)


        def can_shrink():
            right_index = window[-1]
            right_prefix = prefix[right_index]
            left_index = window[1]
            left_prefix = prefix[left_index]

            sum_after_shrink = right_prefix - left_prefix
            return sum_after_shrink >= target
        
        while len(window)>1 and can_shrink():
            window.popleft()
        
        
        right_index = window[-1]
        bf_left_index = window[0]

        def has_ge_sum():
            bf_left_prefix = prefix[bf_left_index]
            right_prefix = prefix[right_index]
            window_sum =  right_prefix - bf_left_prefix
            return window_sum >= target

        if has_ge_sum():
            length = right_index - bf_left_index
            min_length = min(min_length, length)
        

        
    if min_length == float("inf"):
        return -1
    else:
        return min_length

        
def build_prefix(nums):
    prefix = [0]
    running = 0
    for num in nums:
        running += num
        prefix.append(running)
    return prefix


#8sub




