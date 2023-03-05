# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur_node = head
        while cur_node:
            
            while cur_node.next and cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next

            cur_node = cur_node.next
        
        return head
#7min
#1sub
