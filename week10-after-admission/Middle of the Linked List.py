# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #find the length
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next
            
        length = length // 2
        
        current = head
        
        while length:
            length -= 1 
            current = current.next
            
        return current

#10min
#3sub
