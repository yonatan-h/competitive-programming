# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, first_node: Optional[ListNode], n: int) -> Optional[ListNode]:

        head = ListNode()
        head.next = first_node

        behind = head
        front = head

        for _ in range(n):
            front = front.next
        
        while front.next:
            front = front.next
            behind = behind.next

        behind.next = behind.next.next

        return head.next
        

