# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, first_node: Optional[ListNode]) -> List[int]:
        nums = []

        cur_node = first_node
        while cur_node:
            nums.append(cur_node.val)
            cur_node = cur_node.next
        
        next_greaters = [0]*len(nums)
        stack = []
        for right in range(len(nums)):
            while stack and nums[right] > nums[stack[-1]]:
                next_greaters[stack.pop()] = nums[right]
            
            stack.append(right)
        return next_greaters



            
                



        
